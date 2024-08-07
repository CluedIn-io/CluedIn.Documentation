---
layout: cluedin
title: Switching a Datastore Provider
parent: Development
nav_order: 090
has_children: false
permalink: /development/switching-datastore-provider
tags: ["development","data-stores"]
published: false
---


CluedIn ships with many different datastore implementations. This gives you a choice on what system will host your data. It may be that you would rather use PostGres or MySQL than SQL Server for the Relational Store. It maybe that you would like to use a cloud SQL provider via PAAS. The Datastore abstraction layer allows you to support this change. 

To change your implementation of a particular store requires two pieces:

1: Implementing the IDataStore interface and the specific provider interface you would like to implement e.g. IRelationalDataStore. 

2: Injecting your new implementation into the Container of CluedIn. 

```csharp

using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.Entity.Core;
using System.Data.Entity.Infrastructure;
using System.Data.SqlClient;
using System.Linq;
using System.Linq.Expressions;
using System.Security;
using System.Threading.Tasks;

using CluedIn.Core;
using CluedIn.Core.Accounts;
using CluedIn.Core.Data;
using CluedIn.Core.DataStore;
using CluedIn.Core.Processing;
using CluedIn.DataStore.Exceptions;

using EntityFramework.Extensions;

namespace CluedIn.DataStore.Relational.PrimaryDataStore
{
    public class PrimaryRelationalDataStore<T> : EntityDataStore<T>, IPrimaryEntityDataStore<T>
        where T : Entity
    {
        public PrimaryRelationalDataStore([NotNull] ApplicationContext context)
            : base(context, DataShardType.Data)
        {
        }

       /// <summary>Creates the connection manager.</summary>
        /// <typeparam name="TConnection">The type of the connection.</typeparam>
        /// <param name="organization">The organization.</param>
        /// <returns>The connection manager.</returns>
        public override IDataStoreConnectionManager<TConnection> CreateConnectionManager<TConnection>(IOrganization organization)
        {
            return (IDataStoreConnectionManager<TConnection>)new RelationalConnectionManager<PrimaryDataStoreModel>(organization);
        }

        public override IProcessedEntity GetProcessedEntityById(ExecutionContext context, Guid id)
        {
            return this.GetById(context, id);
        }

        public override TQuery CreateQuery<TQuery>(ExecutionContext context)
        {
            throw new NotSupportedException();
        }

        public override T GetByEntityCode(ExecutionContext context, IEntityCode entityCode)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var simple = dataContext.Set<SimpleEntityCode>().Where(c => c.Code == entityCode.Key).Select(c => c.Entity).FirstOrDefault();

                var result = simple != null ? (T)simple.ToEntity(this.Context, context) : null;

                if (result == null)
                    return null;

                if (!this.VerifyContextOrganization(result, context))
                    throw new UnauthorizedAccessException();

                return result;
            }
        }

        public override bool EntityWithEntityCodeExists(ExecutionContext context, IEntityCode entityCode)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                return dataContext.Set<SimpleEntityCode>().Any(c => c.Code == entityCode.Key);
            }
        }

        public override IDictionary<IEntityCode, bool> EntitiesWithEntityCodesExists(ExecutionContext context, IEnumerable<IEntityCode> entityCodes)
        {
            var codes = entityCodes.Select(c => c.Key).ToList();

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var existingCodes = dataContext.Set<SimpleEntityCode>()
                                        .Where(c => codes.Contains(c.Code))
                                        .Select(c => c.Code)
                                        .ToHashSet();

                return entityCodes.ToDictionary(c => c, c => existingCodes.Contains(c.Key));
            }
        }

        public override bool EntityWithIdExists(ExecutionContext context, Guid id)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                return dataContext.Set<SimpleEntityCode>().Any(c => c.EntityId == id);
            }
        }

        /// <summary>Creates the data store.</summary>
        /// <param name="context">The context.</param>
        public override void CreateDataStore(ExecutionContext context)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
                dataContext.Database.CreateIfNotExists();
        }

        /// <summary>Deletes the data store.</summary>
        /// <param name="context">The context.</param>
        public override void DeleteDataStore(ExecutionContext context)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                try
                {
                    dataContext.Database.Delete();
                }
                catch (Exception ex)
                {
                    throw new UnableToDeleteDataStoreException(ex);
                }
            }
        }

        /// <summary>Gets the entity by identifier.</summary>
        /// <param name="context">The context.</param>
        /// <param name="id">The identifier.</param>
        /// <returns>The entity with the specified id.</returns>
        public override T GetById(ExecutionContext context, Guid id)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var simple = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).FirstOrDefault(e => e.Id == id);

                return simple != null ? (T)simple.ToEntity(this.Context, context) : null;
            }
        }

        /// <summary>Queries the data store.</summary>
        /// <param name="context">The context.</param>
        /// <param name="predicate">The predicate.</param>
        /// <returns>The results of the query.</returns>
        public override IEnumerable<T> Select(ExecutionContext context, Expression<Func<T, bool>> predicate)
        {
            throw new NotSupportedException();
        }

        /// <summary>Queries the data store asynchronously.</summary>
        /// <param name="context">The context.</param>
        /// <param name="predicate">The predicate.</param>
        /// <returns>The results of the query.</returns>
        public override async Task<IEnumerable<T>> SelectAsync(ExecutionContext context, Expression<Func<T, bool>> predicate)
        {
            return await Task.FromResult(default(IEnumerable<T>));
        }

        /// <inheritdoc />
        public override bool Any(ExecutionContext context, Expression<Func<T, bool>> predicate)
        {
            throw new NotImplementedException();
        }

        /// <summary>Inserts the specified context.</summary>
        /// <param name="context">The context.</param>
        /// <param name="entity">The entity.</param>
        public override void Insert(ExecutionContext context, T entity)
        {
            this.VerifyEntityContext(entity, context);

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var entry = SimpleEntity.FromEntity(entity);
                dataContext.Set<SimpleEntity>().Attach(entry);

                foreach (var code in entry.EntityCodes)
                {
                    dataContext.Set<SimpleEntityCode>().Attach(code);
                    dataContext.Entry(code).State = EntityState.Added;
                }

                dataContext.Entry(entry).State = EntityState.Added;
                dataContext.Set<SimpleEntity>().Add(entry);

                //foreach (var edge in entity.IncomingEdges)
                //{
                //    InsertRelationshipInternal(entity, edge, dataContext);
                //}

                //foreach (var edge in entity.OutgoingEdges)
                //{
                //    InsertRelationshipInternal(entity, edge, dataContext);
                //}

                dataContext.SaveChanges();
            }
        }

        /// <summary>Inserts the specified object.</summary>
        /// <param name="context">The context.</param>
        /// <param name="objects">The objects.</param>
        public override void Insert(ExecutionContext context, IEnumerable<T> objects)
        {
            if (!objects.All(o => this.VerifyEntityContext(o, context)))
                throw new SecurityException("Cannot insert data for a different security context.");

            foreach (var o in objects)
            {
                this.Insert(context, o);
            }
        }

        /// <summary>Inserts or updates the specified objects.</summary>
        /// <param name="context">The context.</param>
        /// <param name="entity">The object.</param>
        public override void InsertOrUpdate(ExecutionContext context, T entity)
        {
            this.VerifyEntityContext(entity, context);

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                Action action = () =>
                {
                    var entry = SimpleEntity.FromEntity(entity);

                    var existing = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).Any(e => e.Id == entity.Id);

                    if (existing)
                    {
                        dataContext.Set<SimpleEntityCode>().Where(c => c.EntityId == entity.Id).Delete();

                        entry = dataContext.Set<SimpleEntity>().Attach(entry);
                        dataContext.Entry(entry).State = EntityState.Modified;
                    }
                    else
                    {
                        entry = dataContext.Set<SimpleEntity>().Attach(entry);
                        dataContext.Entry(entry).State = EntityState.Added;
                        dataContext.Set<SimpleEntity>().Add(entry);
                    }

                    foreach (var code in entry.EntityCodes)
                    {
                        dataContext.Set<SimpleEntityCode>().Attach(code);
                        dataContext.Entry(code).State = EntityState.Added;
                    }

                    dataContext.SaveChanges();
                };

                action.ExecuteWithRetry(
                    isTransient: ex =>
                        {
                            if (ex is UpdateException)
                                return SqlExceptionHelper.IsDuplicateViolation((UpdateException)ex);

                            if (ex is DbUpdateException)
                                return SqlExceptionHelper.IsDuplicateViolation((DbUpdateException)ex);

                            if (ex is SqlException)
                                return SqlExceptionHelper.IsDuplicateViolation((SqlException)ex);

                            if (ex is ConstraintException)
                                return true;

                            return false;
                        });
            }
        }

        public override void Save()
        {
            throw new NotImplementedException();
        }

        public override Task SaveAsync()
        {
            throw new NotImplementedException();
        }

        /// <summary>Inserts or updates the specified objects.</summary>
        /// <param name="context">The context.</param>
        /// <param name="objects">The objects.</param>
        public override void InsertOrUpdate(ExecutionContext context, IEnumerable<T> objects)
        {
            if (!objects.All(o => this.VerifyEntityContext(o, context)))
                throw new SecurityException("Cannot insert or update data for a different security context.");

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                foreach (var o in objects)
                {
                    dataContext.Set<T>().Add(o);
                }

                dataContext.SaveChanges();
            }
        }

        /// <summary>Updates the specified object.</summary>
        /// <param name="context">The context.</param>
        /// <param name="entity">The object.</param>
        public override void Update(ExecutionContext context, T entity)
        {
            this.VerifyEntityContext(entity, context);

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var entry = SimpleEntity.FromEntity(entity);
                entry = dataContext.Set<SimpleEntity>().Attach(entry);
                dataContext.Entry(entry).State = EntityState.Modified;
                dataContext.SaveChanges();
            }
        }

        /// <summary>Deletes the specified context.</summary>
        /// <param name="context">The context.</param>
        /// <param name="entity">The entity.</param>
        public override void Delete(ExecutionContext context, T entity)
        {
            this.VerifyEntityContext(entity, context);

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var entry = SimpleEntity.FromEntity(entity);
                dataContext.Set<SimpleEntity>().Attach(entry);
                dataContext.Set<SimpleEntity>().Remove(entry);
                dataContext.SaveChanges();
            }
        }

        /// <summary>Deletes the specified object.</summary>
        /// <param name="context">The context.</param>
        /// <param name="objects">The objects.</param>
        public override void Delete(ExecutionContext context, IEnumerable<T> objects)
        {
            if (!objects.All(o => this.VerifyEntityContext(o, context)))
                throw new SecurityException("Cannot delete data for a different security context.");

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                foreach(var obj in objects)
                    this.Delete(context, obj);

                dataContext.SaveChanges();
            }
        }

        /// <summary>Queries the data store.</summary>
        /// <param name="context">The context.</param>
        /// <param name="predicate">The predicate.</param>
        /// <returns>The results of the query.</returns>
        public virtual decimal? GetUsage(ExecutionContext context, Expression<Func<T, decimal?>> predicate)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
                return this.FilterEntitySet(dataContext.Set<T>(), context).Sum(predicate);
        }

        /// <summary>Deletes the object with the specified id.</summary>
        /// <param name="context">The context.</param>
        /// <param name="id">The identifier.</param>
        public override void DeleteById(ExecutionContext context, Guid id)
        {
            this.DeleteById(context, id, null);
        }

        /// <summary>Deletes the by identifier.</summary>
        /// <param name="context">The context.</param>
        /// <param name="id">The identifier.</param>
        /// <param name="version">The version.</param>
        public override void DeleteById(ExecutionContext context, Guid id, int? version)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                this.FilterEntitySet(dataContext.Set<SimpleEntityEdge>(), context).Where(e => e.FromEntityId == id).Delete();
                this.FilterEntitySet(dataContext.Set<SimpleEntityEdge>(), context).Where(e => e.ToEntityId == id).Delete();
                this.FilterEntitySet(dataContext.Set<SimpleEntityCode>(), context).Where(e => e.EntityId == id).Delete();
                this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).Where(e => e.Id == id).Delete();
                dataContext.SaveChanges();
            }
        }

        /// <summary>Deletes all objects.</summary>
        /// <param name="context">The context.</param>
        /// <param name="canBeSystemContext">if set to <c>true</c> [can be system context].</param>
        public override void DeleteAll(ExecutionContext context, bool canBeSystemContext = false)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).SelectMany(e => e.IncomingEdges).Delete();
                this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).SelectMany(e => e.OutgoingEdges).Delete();
                this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).SelectMany(e => e.EntityCodes).Delete();
                this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).Delete();
            }
        }

        /// <summary>
        /// Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources.
        /// </summary>
        public override void Dispose()
        {
        }

        protected virtual bool VerifyEntityContext<TEntity>(TEntity entity, ExecutionContext context)
        {
            if (context.Organization == context.ApplicationContext.System.Organization)
                return true;

            if (!this.VerifyContextOrganization(entity, context))
                return false;

            if (!this.VerifyContextUser(entity, context))
                return false;

            return true;
        }

        protected virtual IQueryable<TEntity> FilterEntitySet<TEntity>(DbSet<TEntity> set, ExecutionContext context) where TEntity : class
        {
            if (context.Organization == context.ApplicationContext.System.Organization)
                return set;

            IQueryable<TEntity> filter = set;

            filter = this.FilterByContextOrganization(filter, context);
            filter = this.FilterByContextUser(filter, context);

            return filter;
        }

        protected virtual IQueryable<SimpleEntity> FilterEntitySet(DbSet<SimpleEntity> set, ExecutionContext context)
        {
            if (context.Organization == context.ApplicationContext.System.Organization)
                return set;

            IQueryable<SimpleEntity> filter = set;

            filter = this.FilterByContextOrganization(filter, context);
            filter = this.FilterByContextUser(filter, context);

            return filter;
        }

        /**********************************************************************************************************
         * 
         **********************************************************************************************************/

        protected virtual bool VerifyContextOrganization<TEntity>(TEntity entity, ExecutionContext context)
        {
            var f = entity as IOrganizationContextFilteredEntity;

            if (f == null)
                return true;

            if (f.OrganizationId != context.Organization.Id)
            {
                throw new SecurityException("Cannot access data from a different security context");
            }

            return true;
        }

        protected virtual bool VerifyContextUser<TEntity>(TEntity entity, ExecutionContext context)
        {
            if (context.Identity == null)
                return true;

            var f = entity as IUserContextFilteredEntity;

            if (f == null)
                return true;

            if (f.UserId != context.Identity.UserId)
            {
                throw new SecurityException("Cannot access data from a different security context");
            }

            return true;
        }

        protected virtual IQueryable<TEntity> FilterByContextOrganization<TEntity>(IQueryable<TEntity> set, ExecutionContext context)
        {
            return set;
        }

        protected virtual IQueryable<SimpleEntity> FilterByContextOrganization(IQueryable<SimpleEntity> set, ExecutionContext context)
        {
            return set.Where(e => e.OrganizationId == context.Organization.Id);
        }

        protected virtual IQueryable<TEntity> FilterByContextUser<TEntity>(IQueryable<TEntity> set, ExecutionContext context)
        {
            return set;
        }

        //////////////////////////////////////////////////////////////////////////////

        //////////////////////////////////////////////////////////////////////////////

        public T GetByEntityCode(ExecutionContext context, IEnumerable<IEntityCode> codes, bool? ignoreDuplicates)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var keys = codes.Select(c => c.Key);

                var simple = dataContext.Set<SimpleEntityCode>().Where(c => keys.Any(i => i == c.Code)).Select(c => c.Entity).FirstOrDefault();

                var result = simple != null ? (T)simple.ToEntity(this.Context, context) : null;

                if (result == null)
                    return null;

                if (!this.VerifyContextOrganization(result, context))
                    throw new UnauthorizedAccessException();

                return result;
            }
        }

        public IEnumerable<T> GetEntitiesByEntityCodes(ExecutionContext context, IEnumerable<IEntityCode> codes)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var keys = codes.Select(c => c.Key);

                var simple = dataContext.Set<SimpleEntityCode>().Where(c => keys.Any(i => i == c.Code)).Select(c => c.Entity);

                var result = simple.Select(e => (T)e.ToEntity(this.Context, context)).ToList();

                foreach (var r in result)
                {
                    if (!this.VerifyContextOrganization(r, context))
                        throw new UnauthorizedAccessException();
                }

                return result;
            }
        }

        public Guid? GetEntityIdByEntityCode(ExecutionContext context, IEntityCode code)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var simple = dataContext.Set<SimpleEntityCode>().Where(c => c.Code == code.Key).Select(c => c.Entity).FirstOrDefault();

                var result = simple != null ? (T)simple.ToEntity(this.Context, context) : null;

                if (result == null)
                    return null;

                if (!this.VerifyContextOrganization(result, context))
                    throw new UnauthorizedAccessException();

                return result.Id;
            }
        }

        public IEnumerable<T> GetEntities(ExecutionContext context, int page, int take)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var result = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).Skip((page - 1) * take).Take(take);

                foreach (var entry in result)
                    yield return (T)entry.ToEntity(this.Context, context);
            }
        }

        public IEnumerable<T> GetEntities(ExecutionContext context, EntityType entityType)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var result = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).Where(e => e.EntityType == entityType.Code);

                foreach (var entry in result)
                    yield return (T)entry.ToEntity(this.Context, context);
            }
        }

        public IEnumerable<T> GetEntities(ExecutionContext context, EntityType entityType, int page, int take)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var result = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context).Where(e => e.EntityType == entityType.Code).Skip((page - 1) * take).Take(take);

                foreach (var entry in result)
                    yield return (T)entry.ToEntity(this.Context, context);
            }
        }

        public IEnumerable<DuplicateEntityGrouping> GetDuplicateEntities(ExecutionContext context)
        {
            return new DuplicateEntityGrouping[0];
        }

        public IEnumerable<DuplicateEntityGrouping> GetDuplicateEntities(ExecutionContext context, Entity entity)
        {
            return new DuplicateEntityGrouping[0];
        }

        public IEnumerable<Entity> FindByNames(ExecutionContext context, IEnumerable<EntityType> entityTypes, IEnumerable<string> names, int maxResults)
        {
            return new Entity[0];
        }

        public IEnumerable<EntityEdge> GetIncomingRelationships(ExecutionContext context, Guid id)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<EntityEdge> GetIncomingRelationships(ExecutionContext context, Guid id, int page, int take)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<EntityEdge> GetOutgoingRelationships(ExecutionContext context, Guid id)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<EntityEdge> GetOutgoingRelationships(ExecutionContext context, Guid id, int page, int take)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<Entity> GetIncomingRelationshipEndpoints(ExecutionContext context, Guid id, string edgeType, int page, int take)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var result = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context)
                    .Where(e => e.Id == id)
                    .SelectMany(e => e.IncomingEdges)
                    .Where(e => e.EdgeType == edgeType)
                    .Skip(page * 20)
                    .Take(take);

                foreach (var entry in result)
                    yield return (T)entry.FromEntity.ToEntity(this.Context, context);
            }
        }

        public IEnumerable<Entity> GetIncomingRelationshipEndpoints(
            ExecutionContext context,
            Guid id,
            string edgeType,
            string entityType,
            int page,
            int take)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var result = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context)
                    .Where(e => e.Id == id)
                    .SelectMany(e => e.IncomingEdges)
                    .Where(e => e.EdgeType == edgeType && e.FromEntity.EntityType == entityType)
                    .Skip(page * 20)
                    .Take(take);

                foreach (var entry in result)
                    yield return (T)entry.FromEntity.ToEntity(this.Context, context);
            }
        }

        public IEnumerable<Entity> GetOutgoingRelationshipEndpoints(ExecutionContext context, Guid id, string edgeType, int page, int take)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                var result = this.FilterEntitySet(dataContext.Set<SimpleEntity>(), context)
                    .Where(e => e.Id == id)
                    .SelectMany(e => e.OutgoingEdges)
                    .Where(e => e.EdgeType == edgeType)
                    .Skip(page * 20)
                    .Take(take);

                foreach (var entry in result)
                    yield return (T)entry.FromEntity.ToEntity(this.Context, context);
            }
        }

        public bool HasRelationship(ExecutionContext context, T first, T second, string relationshipType)
        {
            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                return this.FilterEntitySet(dataContext.Set<SimpleEntityEdge>(), context)
                    .Any(e => e.FromEntityId == first.Id && e.ToEntityId == second.Id && e.EdgeType == relationshipType);
            }
        }

        public void InsertRelationship(ExecutionContext context, T contextEntity, EntityEdge edge)
        {
            this.InsertRelationship(context, contextEntity, edge, null);
        }

        public void InsertRelationship(ExecutionContext context, T contextEntity, EntityEdge edge, bool? ignoreDuplicates = null)
        {
            this.VerifyEntityContext(contextEntity, context);

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                InsertRelationshipInternal(contextEntity, edge, dataContext);
                dataContext.SaveChanges();
            }
        }

        private static void InsertRelationshipInternal(T contextEntity, EntityEdge edge, DbContext dataContext)
        {
            if (edge.FromReference.IsReferenceTo(contextEntity))
            {
                var ids = dataContext.Set<SimpleEntity>().Where(e => e.EntityCodes.Any(c => c.Code == edge.ToReference.Code.Key)).Select(e => e.Id);

                foreach (var id in ids)
                {
                    var entry = new SimpleEntityEdge()
                                    {
                                        FromEntityId = contextEntity.Id,
                                        ToEntityId = id,
                                        EdgeType = edge.EdgeType,
                                        EdgeData = null
                                    };
                    dataContext.Set<SimpleEntityEdge>().Add(entry);
                }
            }
            else if (edge.ToReference.IsReferenceTo(contextEntity))
            {
                var ids = dataContext.Set<SimpleEntity>().Where(e => e.EntityCodes.Any(c => c.Code == edge.FromReference.Code.Key)).Select(e => e.Id);

                foreach (var id in ids)
                {
                    var entry = new SimpleEntityEdge()
                                    {
                                        ToEntityId = contextEntity.Id,
                                        FromEntityId = id,
                                        EdgeType = edge.EdgeType,
                                        EdgeData = null
                                    };
                    dataContext.Set<SimpleEntityEdge>().Add(entry);
                }
            }
            else if ((contextEntity.IsDeleted != null && contextEntity.IsDeleted.Value) || contextEntity.ProcessedData.OriginEntityCode.Type.Is("/Deleted"))
            {
                return;
            }
            else
            {
                throw new ArgumentException("The edge to be inserted doesn't reference the context entity. ContextEntity: {0} Edge: {1}".FormatWith(contextEntity.ProcessedData.OriginEntityCode, edge), nameof(edge));
            }
        }

        public void DeleteRelationship(ExecutionContext context, T entity, EntityEdge edge)
        {
            this.VerifyEntityContext(entity, context);

            using (var dataContext = context.CreateDbContext<PrimaryDataStoreModel>())
            {
                if (edge.FromReference.IsReferenceTo(entity))
                {
                    dataContext.Set<SimpleEntityEdge>().Where(e => e.FromEntityId == entity.Id && e.EdgeType == edge.EdgeType && e.ToEntity.EntityCodes.Any(c => c.Code == edge.ToReference.Code.Key)).Delete();
                    dataContext.SaveChanges();
                }
                else if (edge.ToReference.IsReferenceTo(entity))
                {
                    dataContext.Set<SimpleEntityEdge>().Where(e => e.ToEntityId == entity.Id && e.EdgeType == edge.EdgeType && e.FromEntity.EntityCodes.Any(c => c.Code == edge.ToReference.Code.Key)).Delete();
                    dataContext.SaveChanges();
                }
                else if ((entity.IsDeleted != null &&  entity.IsDeleted.Value) || entity.ProcessedData.OriginEntityCode.Type.Is("/Deleted"))
                {
                    return; // Ignore
                }
                else
                    throw new ArgumentException("The edge to be inserted doesn't reference the context entity. ContextEntity: {0} Edge: {1}".FormatWith(entity.ProcessedData.OriginEntityCode, edge), nameof(edge));
            }
        }

        public EntityAggregatedParents GetCachedParents(ExecutionContext context, Guid id)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<EntityAggregatedParents> GetCachedParents(ExecutionContext context, IEnumerable<Guid> ids)
        {
            throw new NotImplementedException();
        }

        public void Update(ExecutionContext context, EntityAggregatedParents entityParents)
        {
            throw new NotImplementedException();
        }

        //////////////////////////////////////////////////////////////////////////////
    }
}
```

You will then need to update your container.config to include the switch to tell the Entity Framework to use your other database.

```xml
   		<connectionStrings>
            <add name="MyContext" providerName="MySql.Data.MySqlClient" 
                connectionString="server=localhost;port=3306;database=mycontext;uid=root;password=********"/>
        </connectionStrings>
        <entityFramework>
            <defaultConnectionFactory type="System.Data.Entity.Infrastructure.SqlConnectionFactory, EntityFramework"/>
            <providers>
                <provider invariantName="MySql.Data.MySqlClient" 
                    type="MySql.Data.MySqlClient.MySqlProviderServices, MySql.Data.Entity.EF6"/>
                <provider invariantName="System.Data.SqlClient" 
                    type="System.Data.Entity.SqlServer.SqlProviderServices, EntityFramework.SqlServer"/>
            </providers>
        </entityFramework>
```
