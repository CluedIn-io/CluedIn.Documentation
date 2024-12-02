---
layout: cluedin
nav_order: 16
parent: Configuration
grand_parent: PaaS operations
permalink: /paas-operations/config/dedicated-stream-processing-pod
title: Dedicated stream processing pod
tags: ["deployment", "kubernetes", "web", "frontend"]
headerIcon: "paas"
---
## On this page
{: .no_toc .text-delta }
- TOC
{:toc}

In this article, you'll find instructions for creating a dedicated pod that only processes streams.

**Prerequisites**
- Access to your Kubernetes cluster
- Helm installed

## Config Map
Create the following config map, note the important environment variable `CLUEDIN_appSettings__Streams_Processing_Enabled: "true"`.

```yaml
apiVersion: v1
kind: ConfigMap
data:
  ASPNETCORE_ENVIRONMENT: verbose
  CLUEDIN_appSettings__Agent_Enabled: "false"
  CLUEDIN_appSettings__ClueProcessing_FuzzyEntityMatching_Enabled: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ArchiveMetricsValues: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ClueProcessing: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_IProcessing_Clues: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_MergeEntities: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_MeshData: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_Metrics_ArchiveMetricsValuesCommand: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ParentsProcessing: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ParentsProcessing_ParentIds: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ProcessEdges: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ProcessEntityMetrics: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_ProcessGlobalMetrics: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_SaveEntity: "false"
  CLUEDIN_appSettings__ClueProcessing_Subscribe_SendMail: "false"
  CLUEDIN_appSettings__ClueProcessing_SubscribeSeperateQueues: "true"
  CLUEDIN_appSettings__JobServer_Enabled: "true"
  CLUEDIN_appSettings__Logging_Targets_Exceptions: "false"
  CLUEDIN_appSettings__Metrics_Enabled: "false"
  CLUEDIN_appSettings__Metrics_Accuracy_Enabled: "false"
  CLUEDIN_appSettings__Metrics_Completeness_Enabled: "false"
  CLUEDIN_appSettings__Metrics_Connectivity_Enabled: "false"
  CLUEDIN_appSettings__Metrics_DataClassificationType_Enabled: "false"
  CLUEDIN_appSettings__Metrics_Relevance_Enabled: "false"
  CLUEDIN_appSettings__SeqUrl: ""
  CLUEDIN_appSettings__Streams_ExportShadowEntities: "false"
  CLUEDIN_appSettings__Streams_Processing_Enabled: "true"
metadata:
  labels:
    app: cluedin
    release: cluedin-platform
  name: cluedin-server-processing-streams
  namespace: cluedin
```

## Deployment
Take the current deployment for `cluedin-server-processing` as shown below.

1. Change name to `cluedin-server-processing-streams`
2. Replace configmap reference `cluedin-server-processing` with `cluedin-server-processing-streams`
3. Then deploy

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluedin-server-processing-streams
  namespace: cluedin
  labels:
    app: cluedin
    app.kubernetes.io/instance: cluedin-platform
    app.kubernetes.io/managed-by: Helm
    app.kubernetes.io/name: application
    helm.sh/chart: application-2.3.0
    release: cluedin-platform
    role: processing
  annotations:
    deployment.kubernetes.io/revision: '42'
    meta.helm.sh/release-name: cluedin-platform
    meta.helm.sh/release-namespace: cluedin
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cluedin
      app.kubernetes.io/instance: cluedin-platform
      app.kubernetes.io/name: application
      role: processing
  template:
    metadata:
      labels:
        app: cluedin
        app.kubernetes.io/instance: cluedin-platform
        app.kubernetes.io/managed-by: Helm
        app.kubernetes.io/name: application
        helm.sh/chart: application-2.3.0
        release: cluedin-platform
        role: processing
    spec:
      volumes:
        - name: components
          persistentVolumeClaim:
            claimName: cluedin-init-data
      initContainers:
        - name: wait-cluedin-sqlserver
          image: cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3
          args:
            - service
            - cluedin-sqlserver
            - '-n'
            - cluedin
          imagePullPolicy: IfNotPresent
        - name: wait-init-sqlserver-job
          image: cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3
          args:
            - job
            - init-sqlserver-job
            - '-n'
            - cluedin
          imagePullPolicy: IfNotPresent
        - name: wait-init-neo4j-job
          image: cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3
          args:
            - job
            - init-neo4j-job
            - '-n'
            - cluedin
          imagePullPolicy: IfNotPresent
        - name: wait-init-cluedin-job
          image: cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3
          args:
            - job
            - init-cluedin-job
            - '-n'
            - cluedin
          imagePullPolicy: IfNotPresent
        - name: wait-cluedin-redis-master
          image: cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3
          args:
            - service
            - cluedin-redis-master
            - '-n'
            - cluedin
          imagePullPolicy: IfNotPresent
        - name: wait-cluedin-elasticsearch
          image: cluedinprod.azurecr.io/groundnuty/k8s-wait-for:v1.3
          args:
            - service
            - cluedin-elasticsearch
            - '-n'
            - cluedin
          imagePullPolicy: IfNotPresent
      containers:
        - name: cluedin-processing
          image: cluedinprod.azurecr.io/cluedin/cluedin-server:2024.07
          ports:
            - containerPort: 9000
              protocol: TCP
            - containerPort: 9001
              protocol: TCP
            - containerPort: 9003
              protocol: TCP
            - containerPort: 9006
              protocol: TCP
            - containerPort: 9007
              protocol: TCP
          envFrom:
            - configMapRef:
                name: cluedin-server
            - configMapRef:
                name: cluedin-server-processing-streams
            - configMapRef:
                name: cluedin-server-crawling-disable
          env:
            - name: MSSQL_HOST
              value: cluedin-sqlserver
            - name: CLUEDIN_APPSETTINGS__MESSAGING_CONSUMER_PREFETCHCOUNT
              value: '4'
            - name: MSSQL_PORT
              value: '1433'
            - name: MSSQL_TIMEOUT
              value: '150'
            - name: MSSQL_CLIENTUSER_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: cluedin-sqlserver-clientuser-secret
                  key: password
            - name: CLUEDIN_CONNECTIONSTRINGS__AUTHENTICATIONSTORE
              value: >-
                Initial Catalog=DataStore.Db.Authentication;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool
                Size=200;Pooling=True;;MultipleActiveResultSets=True;
            - name: CLUEDIN_CONNECTIONSTRINGS__AUDITLOG
              value: >-
                Initial Catalog=DataStore.Db.AuditLog;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__BLOBSTORAGE
              value: >-
                Initial Catalog=DataStore.Db.BlobStorage;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__CONFIGURATIONSTORE
              value: >-
                Initial Catalog=DataStore.Db.Configuration;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__CLUEDINENTITIES
              value: >-
                Initial Catalog=DataStore.Db.OpenCommunication;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__TOKENSTORE
              value: >-
                Initial Catalog=DataStore.Db.TokenStore;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__TRAINING
              value: >-
                Initial Catalog=DataStore.Db.Training;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__EXTERNALSEARCH
              value: >-
                Initial Catalog=DataStore.Db.ExternalSearch;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__LOCKING
              value: >-
                Initial Catalog=DataStore.Db.OpenCommunication;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__ML_LOGGING
              value: >-
                Initial Catalog=DataStore.Db.ML-Logging;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__METRICS
              value: >-
                Initial Catalog=DataStore.Db.Metrics;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__MICROSERVICES
              value: >-
                Initial Catalog=DataStore.Db.MicroServices;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__CLEANCACHE
              value: >-
                Initial Catalog=DataStore.Db.CleanCache;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: MSSQL_SA_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: cluedin-sqlserver-secret
                  key: sapassword
            - name: >-
                CLUEDIN_CONNECTIONSTRINGS__STREAMS_COMMON_SQLCACHECONNECTIONSTRING
              value: >-
                Initial Catalog=DataStore.Db.OpenCommunication;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=sa;Password=$(MSSQL_SA_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__INVITATIONSTORE
              value: >-
                Initial Catalog=DataStore.Db.WebApp;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=sa;Password=$(MSSQL_SA_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__STREAMLOG
              value: >-
                Initial Catalog=DataStore.Db.StreamLog;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: CLUEDIN_CONNECTIONSTRINGS__STREAMCACHE
              value: >-
                Initial Catalog=DataStore.Db.StreamCache;Data
                Source=$(MSSQL_HOST),$(MSSQL_PORT);Encrypt=false;User
                Id=clientUser;Password=$(MSSQL_CLIENTUSER_PASSWORD);connection
                timeout=$(MSSQL_TIMEOUT);Max Pool Size=200;Pooling=True;;
            - name: RABBITMQ_CLUEDIN_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: cluedin-rabbitmq
                  key: rabbitmq-password
            - name: CLUEDIN_CONNECTIONSTRINGS__MESSAGEBUS
              value: >-
                amqp://cluedin:$(RABBITMQ_CLUEDIN_PASSWORD)@cluedin-rabbitmq:5672
            - name: CLUEDIN_CONNECTIONSTRINGS__MESSAGEBUSMANAGEMENT
              value: >-
                host=cluedin-rabbitmq:15672;username=cluedin;password=$(RABBITMQ_CLUEDIN_PASSWORD)
            - name: CLUEDIN_CONNECTIONSTRINGS__SIGNALRSCALEOUT
              value: >-
                amqp://cluedin:$(RABBITMQ_CLUEDIN_PASSWORD)@cluedin-rabbitmq:5672
            - name: NEO4J_NEO4J_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: cluedin-neo4j-secrets
                  key: neo4j-password-encoded
            - name: CLUEDIN_CONNECTIONSTRINGS__GRAPHSTORE_READ
              value: http://neo4j:$(NEO4J_NEO4J_PASSWORD)@cluedin-neo4j:7474
            - name: CLUEDIN_CONNECTIONSTRINGS__GRAPHSTORE_WRITE
              value: http://neo4j:$(NEO4J_NEO4J_PASSWORD)@cluedin-neo4j:7474
            - name: REDIS_REDIS_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: cluedin-redis
                  key: redis-password
            - name: CLUEDIN_CONNECTIONSTRINGS__CACHESTORE
              value: >-
                cluedin-redis-master:6379,password=$(REDIS_REDIS_PASSWORD),ssl=false,abortConnect=false,connectRetry=0,connectTimeout=20000,syncTimeout=20000,keepAlive=30
            - name: CLUEDIN_CONNECTIONSTRINGS__ETAGSTORE
              value: >-
                cluedin-redis-master:6379,password=$(REDIS_REDIS_PASSWORD),ssl=false,abortConnect=false,connectRetry=0,connectTimeout=20000,syncTimeout=20000,keepAlive=30
            - name: CLUEDIN_CONNECTIONSTRINGS__JOBSTORE
              value: >-
                cluedin-redis-master:6379,password=$(REDIS_REDIS_PASSWORD),ssl=false,abortConnect=false,connectRetry=0,connectTimeout=20000,syncTimeout=20000,keepAlive=30
            - name: CLUEDIN_CONNECTIONSTRINGS__DATAPROTECTIONPERSISTENCE
              value: >-
                cluedin-redis-master:6379,password=$(REDIS_REDIS_PASSWORD),ssl=false,abortConnect=false,connectRetry=0,connectTimeout=20000,syncTimeout=20000,keepAlive=30
            - name: ELASTICSEARCH_ELASTIC_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: elasticsearch-credentials
                  key: password
            - name: CLUEDIN_CONNECTIONSTRINGS__SEARCHSTORE
              value: >-
                http://elastic:$(ELASTICSEARCH_ELASTIC_PASSWORD)@cluedin-elasticsearch:9200
            - name: CLUEDIN_APPSETTINGS__EMAILUSERNAME
              valueFrom:
                secretKeyRef:
                  name: cluedin-email
                  key: EmailUserName
            - name: CLUEDIN_APPSETTINGS__EMAILPASSWORD
              valueFrom:
                secretKeyRef:
                  name: cluedin-email
                  key: EmailPassword
            - name: CLUEDIN_APPSETTINGS__EMAILSERVER
              valueFrom:
                secretKeyRef:
                  name: cluedin-email
                  key: EmailHost
            - name: CLUEDIN_APPSETTINGS__EMAILPORT
              valueFrom:
                secretKeyRef:
                  name: cluedin-email
                  key: EmailHostPort
            - name: CLUEDIN_APPSETTINGS__EMAILSERVERSSL
              valueFrom:
                secretKeyRef:
                  name: cluedin-email
                  key: EmailEnableSsl
          resources:
            limits:
              cpu: '7'
              memory: 25G
            requests:
              cpu: '1'
              memory: 2Gi
          volumeMounts:
            - name: components
              mountPath: /components
          livenessProbe:
            httpGet:
              path: /health/liveness
              port: 9000
              scheme: HTTP
            initialDelaySeconds: 30
            timeoutSeconds: 30
            periodSeconds: 20
            successThreshold: 1
            failureThreshold: 30
          readinessProbe:
            httpGet:
              path: /health/readiness
              port: 9000
              scheme: HTTP
            initialDelaySeconds: 30
            timeoutSeconds: 30
            periodSeconds: 20
            successThreshold: 1
            failureThreshold: 30
          imagePullPolicy: IfNotPresent
          securityContext:
            capabilities:
              add:
                - SYS_PTRACE
            runAsUser: 0
            runAsNonRoot: false
            allowPrivilegeEscalation: true
      restartPolicy: Always
      terminationGracePeriodSeconds: 30
      dnsPolicy: ClusterFirst
      nodeSelector:
        kubernetes.cluedin.com/pooltype: processing
      serviceAccountName: cluedin-serviceaccount
      serviceAccount: cluedin-serviceaccount
      securityContext: {}
      imagePullSecrets:
        - name: acr-registry-key
      schedulerName: default-scheduler
      tolerations:
        - key: kubernetes.cluedin.com/pool
          operator: Equal
          value: processing
          effect: NoSchedule
  strategy:
    type: Recreate
  revisionHistoryLimit: 10
  progressDeadlineSeconds: 600
```