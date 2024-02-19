---
layout: cluedin
title: Entity Type
parent: Development
nav_order: 210
has_children: false
permalink: /development/entity-type
tags: ["development","entities","entity-types"]
---


An Entity Type is your way to tell a Clue its base object type. This could be any of the inbuilt Entity Types from CluedIn, or it could be custom types as well. A Clue can only have one type, but an entity may have decided its type based off different entity types from many Clues. For example, if one Clue was of type "/Infrastructure/Contact" and one was "Person", then the final Entity will choose one of these types - you cannot have more than one Entity Type. 

Why do Entity Types have a "/" in them? CluedIn has a nested hierarchy of Entity Types that will separate the types by a forward slash. This hierarchy could be something such as "/Sales/Deal", indicating that the "Deal" type is a child of the "Sale" entity type. We sometimes refer to these as "Namespaces".

By choosing certain Entity Types, CluedIn will do some automatic processing on that data. For example, if you add a custom Entity Type of "/Car", then by default, CluedIn will most likely do absolutely no "smarts" on this entity. This is simply due to the fact that the CluedIn processing server will only listen to certain Entity Types and run extra processing on it. Your custom data will be persisted and made available - there is no issues with adding new types. If you would like to add "smarts" into the CluedIn processing server to handle your new Entity Type and either clean, validate, enrich or other - then you will need to add new Processors, based off the IProcessing interface.

You can access all the default Entity Types using the Static EntityType class. Think of Entity Types like Domain Objects. 

Here is the list of supported Entity Types in a base install of CluedIn:

```csharp
namespace CluedIn.Core.Data
{
    public partial class EntityType
    {
        private static readonly IDictionary<string, EntityTypeSettings> SettingsCache = new ConcurrentDictionary<string, EntityTypeSettings>();

        public static readonly TemporalEntityType           Temporal            = new TemporalEntityType();
        public static readonly GeographyEntityType          Geography           = new GeographyEntityType();
        public static readonly LocationEntityType           Location            = new LocationEntityType();
        public static readonly ProviderEntityType           Provider            = new ProviderEntityType();

        public static readonly InfrastructureEntityType     Infrastructure      = new InfrastructureEntityType();

        public static readonly EntityType                   Person              = "/Person";
        public static readonly OrganizationEntityType       Organization        = new OrganizationEntityType();

        public static readonly FilesEntityType              Files               = new FilesEntityType();
        public static readonly DocumentsEntityType          Documents           = new DocumentsEntityType();
        public static readonly EntityType                   Document            = "/Document";
        public static readonly ImagesEntityType             Images              = new ImagesEntityType();

        public static readonly MailEntityType               Mail                = new MailEntityType();
        public static readonly MarketingEntityType          Marketing           = new MarketingEntityType();
        public static readonly EntityType                   Project             = "/Project";
        public static readonly EntityType                   Topic               = "/Topic";
        public static readonly EntityType                   Tag                 = "/Tag";
        public static readonly CommentEntityType            Comment             = new CommentEntityType();
        public static readonly EntityType                   Announcement        = "/Announcement";
        public static readonly EntityType                   Partner             = "/Partner";
        public static readonly EntityType                   Discussion          = "/Discussion";
        public static readonly EntityType                   Note                = "/Note";
        public static readonly EntityType                   PressRelease        = "/PressRelease";
        public static readonly EntityType                   Account             = "/Account";
        public static readonly EntityType                   Activity            = "/Activity";
        public static readonly EntityType                   Form                = "/Form";
        public static readonly EntityType                   Process             = "/Process";
        public static readonly EntityType                   ProcessStage        = "/ProcessStage";
        public static readonly EntityType                   Question            = "/Question";
        public static readonly ListEntityType               List                = new ListEntityType();
        public static readonly EntityType                   News                = "/News";
        public static readonly EntityType                   FAQ                 = "/FAQ";
        public static readonly EntityType                   Task                = "/Task";
        public static readonly EntityType                   Skill               = "/Skill";
        public static readonly IssueEntityType              Issue               = new IssueEntityType();
        public static readonly CalendarEntityType           Calendar            = new CalendarEntityType();
        public static readonly SourceCodeEntityType         SourceCode          = new SourceCodeEntityType();
        public static readonly PlanningEntityType           Planning            = new PlanningEntityType();
        public static readonly SalesEntityType              Sales               = new SalesEntityType();
        public static readonly EntityType                   Component           = "/Component"; // TODO: Change to Software Component
        public static readonly EntityType                   Channel             = "/Channel";
        public static readonly EntityType                   Product             = "/Product";

        public static readonly EntityType                   Enquiry             = "/Enquiry";
        public static readonly EntityType                   Idea                = "/Idea";
        public static readonly EntityType                   Link                = "/Links";
        public static readonly EntityType                   Certification       = "/Certification";
        public static readonly EntityType                   Unknown             = "/Unknown";
        public static readonly EntityType                   Card                = "/Card";
        public static readonly EntityType                   Template            = "/Template";
        public static readonly EntityType                   Industry            = "/Industry";
        public static readonly EntityType                   PhoneNumber         = "/PhoneNumber";
        public static readonly EntityType                   PhoneCall           = "/PhoneCall";
        public static readonly EntityType                   Sms                 = "/Sms";
        public static readonly EntityType                   VoiceMail           = "/VoiceMail";

        public static readonly WebEntityType                Web                 = new WebEntityType();
        public static readonly AccountingEntityType         Accounting          = new AccountingEntityType();
        public static readonly SupportEntityType            Support             = new SupportEntityType();
        public static readonly PaymentEntityType            Payment             = new PaymentEntityType();
        public static readonly FinanceEntityType            Finance             = new FinanceEntityType();
        public static readonly ConfigurationEntityType      Configuration       = new ConfigurationEntityType();
        public static readonly HumanResourcesEntityType     HR                  = new HumanResourcesEntityType();

        public static EntityType FromFileCategory(FileCategory category)
        {
            switch (category)
            {
                case FileCategory.Audio:
                    return EntityType.Documents.Audio;

                case FileCategory.Video:
                    return EntityType.Documents.Video;

                case FileCategory.PlainText:
                    return EntityType.Documents.PlainText;

                case FileCategory.TextDocument:
                    return EntityType.Documents.Document;

                case FileCategory.Presentation:
                    return EntityType.Documents.Presentation;

                case FileCategory.Spreadsheet:
                    return EntityType.Documents.Spreadsheet;

                case FileCategory.ImageBitmap:
                    return EntityType.Images.Image;

                case FileCategory.Diagram:
                    return EntityType.Documents.Diagram;

                case FileCategory.CompressedFileArchive:
                    return EntityType.Files.CompressedFileArchive;

                case FileCategory.Win32Executable:
                    break;
            }

            return null;
        }

        public class TemporalEntityType : HierarichalEntityType
        {
            public readonly EntityType Date       = "/Temporal/Date";
            public readonly EntityType Week       = "/Temporal/Week";
            public readonly EntityType Quarter    = "/Temporal/Quarter";
            public readonly EntityType Month      = "/Temporal/Month";
            public readonly EntityType Year       = "/Temporal/Year";
            public readonly EntityType Decade     = "/Temporal/Decade";
            public readonly EntityType Century    = "/Temporal/Century";
            public readonly EntityType Millennium = "/Temporal/Millennium";

            protected override EntityType BaseType { get { return "/Temporal"; } }
        }

        public class InfrastructureEntityType : HierarichalEntityType
        {
            public readonly EntityType User                         = "/Infrastructure/User";
            public readonly EntityType Location                     = "/Infrastructure/Location";
            public readonly EntityType Contact                      = "/Infrastructure/Contact";
            public readonly EntityType License                      = "/Infrastructure/License";
            public readonly EntityType Policy                       = "/Infrastructure/Policy";
            public readonly EntityType Application                  = "/Infrastructure/Application";
            public readonly EntityType Domain                       = "/Infrastructure/Domain";
            public readonly EntityType Printer                      = "/Infrastructure/Printer";
            public readonly EntityType Folder                       = EntityType.Create("/Infrastructure/Folder", settings => settings.IsEntityContainer = true);
            public readonly EntityType Cloud                        = "/Infrastructure/Cloud";
            public readonly EntityType Tenant                       = "/Infrastructure/Tenant";
            public readonly EntityType Site                         = EntityType.Create("/Infrastructure/Site", settings => settings.IsEntityContainer = true);
            public readonly EntityType Position                     = "/Infrastructure/Position"; // TODO
            public readonly InfrastructureGroupEntityType Group     = new InfrastructureGroupEntityType();
            public readonly InfrastructureHostEntityType Host       = new InfrastructureHostEntityType();
            public readonly EntityType DirectoryItem                = "/Infrastructure/DirectoryItem";
            public readonly EntityType NetworkAddress               = "/Infrastructure/NetworkAddress";

            protected override EntityType BaseType { get { return "/Infrastructure"; } }
        }

        public class InfrastructureGroupEntityType : HierarichalEntityType
        {
            public readonly EntityType Security     = "/Infrastructure/Group/Security";
            public readonly EntityType Distribution = "/Infrastructure/Group/Distribution";

            protected override EntityType BaseType { get { return "/Infrastructure/Group"; } }
        }

        public class InfrastructureHostEntityType : HierarichalEntityType
        {
            public readonly EntityType Server       = "/Infrastructure/Host/Server";
            public readonly EntityType Computer     = "/Infrastructure/Host/Computer";
            public readonly EntityType Laptop       = "/Infrastructure/Host/Laptop";

            protected override EntityType BaseType { get { return "/Infrastructure/Host"; } }
        }

        public class CommentEntityType : HierarichalEntityType
        {
            public readonly EntityType Social       = "/Comment/Social";

            protected override EntityType BaseType { get { return "/Comment"; } }
        }

        public class OrganizationEntityType : HierarichalEntityType
        {
            public readonly EntityType Competitor   = "/Organization/Competitor";
            public readonly EntityType Department   = "/Organization/Department";
            public readonly EntityType Unit         = "/Organization/Unit";

            protected override EntityType BaseType { get { return "/Organization"; } }
        }

        public class IssueEntityType : HierarichalEntityType
        {
            public readonly EntityType Type         = "/Issue/Type";
            public readonly EntityType Resolution   = "/Issue/Resolution";

            protected override EntityType BaseType { get { return "/Issue"; } }
        }

        public class CalendarEntityType : HierarichalEntityType
        {
            public readonly EntityType Event        = "/Calendar/Event";
            public readonly EntityType Meeting      = "/Calendar/Meeting";

            protected override EntityType BaseType { get { return "/Calendar"; } }
        }

        public class SourceCodeEntityType : HierarichalEntityType
        {
            public readonly EntityType Repository       = EntityType.Create("/SourceCode/Repository", settings => settings.IsEntityContainer = true);
            public readonly EntityType Solution         = EntityType.Create("/SourceCode/Solution", settings => settings.IsEntityContainer = true);
            public readonly EntityType Project          = EntityType.Create("/SourceCode/Project", settings => settings.IsEntityContainer = true);
            public readonly EntityType Library          = "/SourceCode/Library";
            public readonly EntityType Branch           = "/SourceCode/Branch";
            public readonly EntityType PullRequest      = "/SourceCode/PullRequest";
            public readonly EntityType File             = "/SourceCode/File";
            public readonly EntityType ChangeSet        = "/SourceCode/ChangeSet";
            public readonly EntityType Build            = "/SourceCode/Build";
            public readonly EntityType Deployment       = "/SourceCode/Deployment";
            public readonly EntityType DeploymentStatus = "/SourceCode/DeploymentStatus";

            protected override EntityType BaseType { get { return "/SourceCode"; } }
        }

        public class PlanningEntityType : HierarichalEntityType
        {
            public readonly EntityType ProjectPlan  = EntityType.Create("/Planning/ProjectPlan", settings => settings.IsEntityContainer = true);
            public readonly EntityType Iteration    = EntityType.Create("/Planning/Iteration", settings => settings.IsEntityContainer = true);
            public readonly EntityType KanbanBoard  = EntityType.Create("/Planning/KanbanBoard", settings => settings.IsEntityContainer = true);
            public readonly EntityType Workspace    = EntityType.Create("/Planning/Workspace", settings => settings.IsEntityContainer = true);
            public readonly EntityType Proposal     = "/Planning/Proposal";

            public readonly PlanningScrumEntityType Scrum = new PlanningScrumEntityType();

            protected override EntityType BaseType { get { return "/Planning"; } }
        }

        public class PlanningScrumEntityType : HierarichalEntityType
        {
            public readonly EntityType Sprint               = "/Planning/Scrum/Sprint";
            public readonly EntityType BacklogItem          = "/Planning/Scrum/BacklogItem";
            public readonly EntityType Epic                 = "/Planning/Scrum/Epic";
            public readonly EntityType SprintReview         = "/Planning/Scrum/SprintReview";
            public readonly EntityType SprintRetrospective  = "/Planning/Scrum/SprintRetrospective";
            public readonly EntityType DefinitionOfDone     = "/Planning/Scrum/DefinitionOfDone";

            protected override EntityType BaseType { get { return "/Planning/Scrum"; } }
        }

        public class SalesEntityType : HierarichalEntityType
        {
            public readonly EntityType Sale         = "/Sales/Sale";
            public readonly EntityType Contract     = "/Sales/Contract";
            public readonly EntityType Deal         = "/Sales/Deal";
            public readonly EntityType Quote        = "/Sales/Quote";
            public readonly EntityType Lead         = "/Sales/Lead";
            public readonly EntityType Opportunity  = "/Sales/Opportunity";
            public readonly EntityType Order        = "/Sales/Order";

            protected override EntityType BaseType { get { return "/Sales"; } }
        }

        public class SupportEntityType : HierarichalEntityType
        {
            public readonly EntityType Entitlement  = "/Support/Entitlement";
            public readonly EntityType Ticket       = "/Support/Ticket";

            protected override EntityType BaseType { get { return "/Support"; } }
        }

        public class LocationEntityType : HierarichalEntityType
        {
            public readonly EntityType Address      = "/Location/Address";

            protected override EntityType BaseType { get { return "/Location"; } }
        }

        public class GeographyEntityType : HierarichalEntityType
        {
            public readonly EntityType Country      = "/Geography/Country";
            public readonly EntityType City         = "/Geography/City";
            public readonly EntityType State        = "/Geography/State";
            public readonly EntityType TimeZone     = "/Geography/TimeZone";
            public readonly EntityType Territory    = "/Geography/Territory";

            protected override EntityType BaseType { get { return "/Geography"; } }
        }

        public class FilesEntityType : HierarichalEntityType
        {
            public readonly EntityType File                     = "/Files/File";
            public readonly EntityType Directory                = EntityType.Create("/Files/Directory", settings => settings.IsEntityContainer = true);
            public readonly EntityType CompressedFileArchive    = EntityType.Create("/Files/CompressedFileArchive", settings => settings.IsEntityContainer = true);

            protected override EntityType BaseType { get { return "/Files"; } }
        }

        public class DocumentsEntityType : HierarichalEntityType
        {
            public readonly EntityType Database     = "/Document/Database";
            public readonly EntityType PlainText    = "/Document/PlainText";
            public readonly EntityType Document     = "/Document/Document";
            public readonly EntityType Presentation = "/Document/Presentation";
            public readonly EntityType Spreadsheet  = "/Document/Spreadsheet";
            public readonly EntityType Audio        = "/Document/Audio";
            public readonly EntityType Video        = "/Document/Video";
            public readonly EntityType Diagram      = "/Document/Diagram";

            protected override EntityType BaseType { get { return "/Document"; } }
        }

        public class ImagesEntityType : HierarichalEntityType
        {
            public readonly EntityType Image        = "/Image";
            public readonly EntityType Album        = EntityType.Create("/Album", settings => settings.IsEntityContainer = true);
            public readonly EntityType Diagram      = "/Image/Diagram";
            public readonly EntityType Photograph   = "/Image/Photograph";

            protected override EntityType BaseType { get { return "/Image"; } }
        }

        public class ProviderEntityType : HierarichalEntityType
        {
            public readonly EntityType Root         = "/Provider/Root";

            protected override EntityType BaseType { get { return "/Provider"; } }
        }

        public class MailEntityType : HierarichalEntityType
        {
            public readonly EntityType Folder       = EntityType.Create("/Mail/Folder", settings => settings.IsEntityContainer = true);
            public readonly EntityType Thread       = EntityType.Create("/Mail/Thread", settings => settings.IsEntityContainer = true);
            public readonly EntityType Attachment   = "/Mail/Attachment";
            public readonly EntityType Task = "/Mail/Task"; //
            [Obsolete]
            public readonly EntityType Event        = "/Mail/Event"; // TODO: Remove this

            protected override EntityType BaseType { get { return "/Mail"; } }
        }

        public class MarketingEntityType : HierarichalEntityType
        {
            public readonly EntityType Campaign = "/Marketing/Campaign";
            public readonly EntityType Goal     = "/Marketing/Goal";
            public readonly EntityType Ad       = "/Marketing/Ad";
            public readonly EntityType Persona  = "/Marketing/Persona"; // TODO: Remove this

            protected override EntityType BaseType { get { return "/Marketing"; } }
        }

        public class WebEntityType : HierarichalEntityType
        {
            public readonly EntityType Site = EntityType.Create("/Web/Site", settings => settings.IsEntityContainer = true);
            public readonly EntityType Page = "/Web/Page";

            protected override EntityType BaseType { get { return "/Web"; } }
        }

        public class AccountingEntityType : HierarichalEntityType
        {
            public readonly EntityType Year         = "/Accounting/Year";
            public readonly EntityType Period       = "/Accounting/Period";
            public readonly EntityType CostCenter   = EntityType.Create("/Accounting/CostCenter", settings => settings.IsEntityContainer = true);
            public readonly EntityType Group        = EntityType.Create("/Accounting/Group", settings => settings.IsEntityContainer = true);

            protected override EntityType BaseType { get { return "/Accounting"; } }
        }

        public class ListEntityType : HierarichalEntityType
        {
            public readonly EntityType Item         = "/List/ListItem";
            private readonly EntityType baseType    = EntityType.Create("/List", settings => settings.IsEntityContainer = true);

            protected override EntityType BaseType => baseType;
        }

        public class PaymentEntityType : HierarichalEntityType
        {
            public readonly PaymentCardEntityType Card = new PaymentCardEntityType();

            protected override EntityType BaseType => "/Payment";

            public class PaymentCardEntityType : HierarichalEntityType
            {
                public readonly EntityType CreditCard       = "/Payment/Card/CreditCard";
                public readonly EntityType DebitCard        = "/Payment/Card/DebitCard";
                public readonly EntityType ChargeCard       = "/Payment/Card/ChargeCard";
                public readonly EntityType ATMCard          = "/Payment/Card/ATMCard";
                public readonly EntityType StoreValueCard   = "/Payment/Card/StoreValueCard";
                public readonly EntityType GiftCard         = "/Payment/Card/GiftCard";
                public readonly EntityType StoreCard        = "/Payment/Card/StoreCard";

                protected override EntityType BaseType => "/Payment/Card";
            }
        }

        public class FinanceEntityType : HierarichalEntityType
        {
            public readonly EntityType BankAccount  = "/Finance/BankAccount";

            protected override EntityType BaseType => "/Finance";
        }

        public class ConfigurationEntityType : HierarichalEntityType
        {
            public readonly EntityType Setting  = "/Configuration/Setting";

            protected override EntityType BaseType => "/Configuration";
        }

        public class HumanResourcesEntityType : HierarichalEntityType
        {
            public readonly EntityType WorkSchedule = "/HR/WorkSchedule";

            protected override EntityType BaseType => "/HR";
        }

        public abstract class HierarichalEntityType
        {
            protected abstract EntityType BaseType { get; }

            public static bool operator ==(EntityType type1, HierarichalEntityType type2)
            {
                return type1 == (EntityType)type2;
            }

            public static bool operator !=(EntityType type1, HierarichalEntityType type2)
            {
                return type1 != (EntityType)type2;
            }

            public static bool operator ==(HierarichalEntityType type1, EntityType type2)
            {
                return ((EntityType)type1) == type2;
            }

            public static bool operator !=(HierarichalEntityType type1, EntityType type2)
            {
                return ((EntityType)type1) != type2;
            }

            public static implicit operator EntityType(HierarichalEntityType type)
            {
                return type.BaseType;
            }

            public static implicit operator string(HierarichalEntityType type)
            {
                return type.BaseType;
            }

            public override string ToString()
            {
                return ((EntityType)this).ToString();
            }

            public override int GetHashCode()
            {
                return ((EntityType)this).GetHashCode();
            }

            public override bool Equals(object obj)
            {
                return this.BaseType.Equals(obj);
            }
        }
    }
}	
```