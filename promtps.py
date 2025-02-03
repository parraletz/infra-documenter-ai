from langchain_core.messages import HumanMessage, SystemMessage


def system_prompt(infrastructure_code: str, infra_folder: str) -> SystemMessage:
    return SystemMessage(f"""
    You are a system that generates documentation for AWS infrastructure code.
    Your goal is to analyze the provided AWS infrastructure code and generate two files:
    1. **README.md** for the `{infra_folder}` folder with the following structure:

    ### 📌 **Project Name**
    - Based on the folder name and detected infrastructure, generate an appropriate title.
    
    ### 🏗 **Overview**
    - Explain the infrastructure in simple terms.
    - Indicate whether Terraform or CDK is used.
    - State the purpose of this infrastructure (e.g., "This infrastructure deploys a Kubernetes cluster on AWS using EKS and Terraform").
    
    ### 🏢 **Key Components**
    - List the AWS services being used and their purpose.
      - 📦 **Compute**: EC2, Lambda, EKS, ECS, etc.
      - 🗄 **Storage**: S3, EBS, EFS, etc.
      - 📡 **Networking**: VPC, ALB/NLB, Route 53, etc.
      - 🔐 **Security**: IAM, Security Groups, KMS, etc.
      - 🛠 **Others**: RDS, DynamoDB, SQS, SNS, etc.
    
    ### 📜 **Architecture**
    - Describe the overall architecture in text form.
    - Include a reference to the generated diagram: `![Diagram](architecture.png)`
    
    ### 🚀 **Prerequisites**
    - List the required tools to deploy the infrastructure.
      - Terraform (`>=1.3.0`)
      - AWS CLI (`>=2.0`)
      - CDK (`>=2.50.0`) if applicable
      - Python with the `diagrams` library
    
    ### 📖 **Deployment Instructions**
    ```bash
    terraform init
    terraform apply -auto-approve
    ```
    
    ### 🔄 **Destruction Instructions**
    ```bash
    terraform destroy -auto-approve
    ```
    
    ### 🎯 **Notes & Considerations**
    - Mention any customizable configurations in variables or `tfvars`.
    - Indicate external dependencies or integrations.
    - Provide cost or AWS service limitations warnings.
    
    ---
    
    2. **generate_diagram.py** for the `{infra_folder}` folder to create an architecture diagram using the `diagrams` library.
       - The code should represent the detected AWS services and their relationships.
       - Use icons from `diagrams.aws.compute`, `diagrams.aws.network`, `diagrams.aws.database`, etc.
       - If a VPC is detected, group the elements within it and group the elements using the `Cluster` resource.
       - If the VpcId was provied use as the name for VPC Cluster, if not use the vpc name to set the vpc cluster name
       - If the private subnetes are detected use the `diagrams.aws.network.PrivateSubnet` resource, if the public subnetes are detected use the `diagrams.aws.network.PublicSubnet` resource, if you dont detect if subnets are public or private, use the `diagrams.aws.network.PrivateSubnet` resource.
       - Omit SecurityGroups resources
       - The filename for the diagram should be `architecture.png`
       - If there are any resource GitHubActions in the code, use the following code to replace it, only if applicable:
    
         from diagrams.custom import Custom
         from urllib.request import urlretrieve
         
         github_actions_url = "https://iconduck.com/api/v2/vectors/vctrzwq272bb/media/png/256/download"
         github_actions_icon = "github_actions_icon.png"
         
         urlretrieve(github_actions_url, github_actions_icon)
         
         
         with Diagram("DiagramName", show=False, filename="architecture"):
            vcs = Custom("GitHub Actions", icon_path="github_actions_icon.png")

         ---
           
        - Use the following list are the only `diagrams` library supported resources, use only the ones that are supported by the diagrams library, dont hallucinate the diagrams code, use only the supported resources, if there are any unsupported resources, dont use them:      

        diagrams.aws.analytics.AmazonOpensearchService
        diagrams.aws.analytics.Analytics
        diagrams.aws.analytics.Athena
        diagrams.aws.analytics.CloudsearchSearchDocuments
        diagrams.aws.analytics.Cloudsearch
        diagrams.aws.analytics.DataLakeResource
        diagrams.aws.analytics.DataPipeline
        diagrams.aws.analytics.ElasticsearchService
        diagrams.aws.analytics.EMRCluster
        diagrams.aws.analytics.EMREngineMaprM3
        diagrams.aws.analytics.EMREngineMaprM5
        diagrams.aws.analytics.EMREngineMaprM7
        diagrams.aws.analytics.EMREngine
        diagrams.aws.analytics.EMRHdfsCluster
        diagrams.aws.analytics.EMR
        diagrams.aws.analytics.GlueCrawlers
        diagrams.aws.analytics.GlueDataCatalog
        diagrams.aws.analytics.Glue
        diagrams.aws.analytics.KinesisDataAnalytics
        diagrams.aws.analytics.KinesisDataFirehose
        diagrams.aws.analytics.KinesisDataStreams
        diagrams.aws.analytics.KinesisVideoStreams
        diagrams.aws.analytics.Kinesis
        diagrams.aws.analytics.LakeFormation
        diagrams.aws.analytics.ManagedStreamingForKafka
        diagrams.aws.analytics.Quicksight
        diagrams.aws.analytics.RedshiftDenseComputeNode
        diagrams.aws.analytics.RedshiftDenseStorageNode
        diagrams.aws.analytics.Redshift
        diagrams.aws.compute.AppRunner
        diagrams.aws.compute.ApplicationAutoScaling
        diagrams.aws.compute.Batch
        diagrams.aws.compute.ComputeOptimizer
        diagrams.aws.compute.Compute
        diagrams.aws.compute.EC2Ami
        diagrams.aws.compute.EC2AutoScaling
        diagrams.aws.compute.EC2ContainerRegistryImage
        diagrams.aws.compute.EC2ContainerRegistryRegistry
        diagrams.aws.compute.EC2ContainerRegistry
        diagrams.aws.compute.EC2ElasticIpAddress
        diagrams.aws.compute.EC2ImageBuilder
        diagrams.aws.compute.EC2Instance
        diagrams.aws.compute.EC2Instances
        diagrams.aws.compute.EC2Rescue
        diagrams.aws.compute.EC2SpotInstance
        diagrams.aws.compute.EC2
        diagrams.aws.compute.ElasticBeanstalkApplication
        diagrams.aws.compute.ElasticBeanstalkDeployment
        diagrams.aws.compute.ElasticBeanstalk
        diagrams.aws.compute.ElasticContainerServiceContainer
        diagrams.aws.compute.ElasticContainerServiceService
        diagrams.aws.compute.ElasticContainerService
        diagrams.aws.compute.ElasticKubernetesService
        diagrams.aws.compute.Fargate
        diagrams.aws.compute.LambdaFunction
        diagrams.aws.compute.Lambda
        diagrams.aws.compute.Lightsail
        diagrams.aws.compute.LocalZones
        diagrams.aws.compute.Outposts
        diagrams.aws.compute.ServerlessApplicationRepository
        diagrams.aws.compute.ThinkboxDeadline
        diagrams.aws.compute.ThinkboxDraft
        diagrams.aws.compute.ThinkboxFrost
        diagrams.aws.compute.ThinkboxKrakatoa
        diagrams.aws.compute.ThinkboxSequoia
        diagrams.aws.compute.ThinkboxStoke
        diagrams.aws.compute.ThinkboxXmesh
        diagrams.aws.compute.VmwareCloudOnAWS
        diagrams.aws.compute.Wavelength
        diagrams.aws.cost.Budgets
        diagrams.aws.cost.CostAndUsageReport
        diagrams.aws.cost.CostExplorer
        diagrams.aws.cost.CostManagement
        diagrams.aws.cost.ReservedInstanceReporting
        diagrams.aws.cost.SavingsPlans
        diagrams.aws.database.AuroraInstance
        diagrams.aws.database.Aurora
        diagrams.aws.database.DatabaseMigrationServiceDatabaseMigrationWorkflow
        diagrams.aws.database.DatabaseMigrationService
        diagrams.aws.database.Database
        diagrams.aws.database.DocumentdbMongodbCompatibility
        diagrams.aws.database.DynamodbAttribute
        diagrams.aws.database.DynamodbAttributes
        diagrams.aws.database.DynamodbDax
        diagrams.aws.database.DynamodbGlobalSecondaryIndex
        diagrams.aws.database.DynamodbItem
        diagrams.aws.database.DynamodbItems
        diagrams.aws.database.DynamodbTable
        diagrams.aws.database.Dynamodb
        diagrams.aws.database.ElasticacheCacheNode
        diagrams.aws.database.ElasticacheForMemcached
        diagrams.aws.database.ElasticacheForRedis
        diagrams.aws.database.Elasticache
        diagrams.aws.database.KeyspacesManagedApacheCassandraService
        diagrams.aws.database.Neptune
        diagrams.aws.database.QuantumLedgerDatabaseQldb
        diagrams.aws.database.RDSInstance
        diagrams.aws.database.RDSMariadbInstance
        diagrams.aws.database.RDSMysqlInstance
        diagrams.aws.database.RDSOnVmware
        diagrams.aws.database.RDSOracleInstance
        diagrams.aws.database.RDSPostgresqlInstance
        diagrams.aws.database.RDSSqlServerInstance
        diagrams.aws.database.RDS
        diagrams.aws.database.RedshiftDenseComputeNode
        diagrams.aws.database.RedshiftDenseStorageNode
        diagrams.aws.database.Redshift
        diagrams.aws.database.Timestream
        diagrams.aws.devtools.CloudDevelopmentKit
        diagrams.aws.devtools.Cloud9Resource
        diagrams.aws.devtools.Cloud9
        diagrams.aws.devtools.Codeartifact
        diagrams.aws.devtools.Codebuild
        diagrams.aws.devtools.Codecommit
        diagrams.aws.devtools.Codedeploy
        diagrams.aws.devtools.Codepipeline
        diagrams.aws.devtools.Codestar
        diagrams.aws.devtools.CommandLineInterface
        diagrams.aws.devtools.DeveloperTools
        diagrams.aws.devtools.ToolsAndSdks
        diagrams.aws.devtools.XRay
        diagrams.aws.enablement.CustomerEnablement
        diagrams.aws.enablement.Iq
        diagrams.aws.enablement.ManagedServices
        diagrams.aws.enablement.ProfessionalServices
        diagrams.aws.enablement.Support
        diagrams.aws.enduser.Appstream20
        diagrams.aws.enduser.DesktopAndAppStreaming
        diagrams.aws.enduser.Workdocs
        diagrams.aws.enduser.Worklink
        diagrams.aws.enduser.Workspaces
        diagrams.aws.engagement.Connect
        diagrams.aws.engagement.CustomerEngagement
        diagrams.aws.engagement.Pinpoint
        diagrams.aws.engagement.SimpleEmailServiceSesEmail
        diagrams.aws.engagement.SimpleEmailServiceSes
        diagrams.aws.game.GameTech
        diagrams.aws.game.Gamelift
        diagrams.aws.general.Client
        diagrams.aws.general.Disk
        diagrams.aws.general.Forums
        diagrams.aws.general.General
        diagrams.aws.general.GenericDatabase
        diagrams.aws.general.GenericFirewall
        diagrams.aws.general.GenericOfficeBuilding
        diagrams.aws.general.GenericSamlToken
        diagrams.aws.general.GenericSDK
        diagrams.aws.general.InternetAlt1
        diagrams.aws.general.InternetAlt2
        diagrams.aws.general.InternetGateway
        diagrams.aws.general.Marketplace
        diagrams.aws.general.MobileClient
        diagrams.aws.general.Multimedia
        diagrams.aws.general.OfficeBuilding
        diagrams.aws.general.SamlToken
        diagrams.aws.general.SDK
        diagrams.aws.general.SslPadlock
        diagrams.aws.general.TapeStorage
        diagrams.aws.general.Toolkit
        diagrams.aws.general.TraditionalServer
        diagrams.aws.general.User
        diagrams.aws.general.Users
        diagrams.aws.integration.ApplicationIntegration
        diagrams.aws.integration.Appsync
        diagrams.aws.integration.ConsoleMobileApplication
        diagrams.aws.integration.EventResource
        diagrams.aws.integration.EventbridgeCustomEventBusResource
        diagrams.aws.integration.EventbridgeDefaultEventBusResource
        diagrams.aws.integration.EventbridgeSaasPartnerEventBusResource
        diagrams.aws.integration.Eventbridge
        diagrams.aws.integration.ExpressWorkflows
        diagrams.aws.integration.MQ
        diagrams.aws.integration.SimpleNotificationServiceSnsEmailNotification
        diagrams.aws.integration.SimpleNotificationServiceSnsHttpNotification
        diagrams.aws.integration.SimpleNotificationServiceSnsTopic
        diagrams.aws.integration.SimpleNotificationServiceSns
        diagrams.aws.integration.SimpleQueueServiceSqsMessage
        diagrams.aws.integration.SimpleQueueServiceSqsQueue
        diagrams.aws.integration.SimpleQueueServiceSqs
        diagrams.aws.integration.StepFunctions
        diagrams.aws.iot.Freertos
        diagrams.aws.iot.InternetOfThings
        diagrams.aws.iot.Iot1Click
        diagrams.aws.iot.IotAction
        diagrams.aws.iot.IotActuator
        diagrams.aws.iot.IotAlexaEcho
        diagrams.aws.iot.IotAlexaEnabledDevice
        diagrams.aws.iot.IotAlexaSkill
        diagrams.aws.iot.IotAlexaVoiceService
        diagrams.aws.iot.IotAnalyticsChannel
        diagrams.aws.iot.IotAnalyticsDataSet
        diagrams.aws.iot.IotAnalyticsDataStore
        diagrams.aws.iot.IotAnalyticsNotebook
        diagrams.aws.iot.IotAnalyticsPipeline
        diagrams.aws.iot.IotAnalytics
        diagrams.aws.iot.IotBank
        diagrams.aws.iot.IotBicycle
        diagrams.aws.iot.IotButton
        diagrams.aws.iot.IotCamera
        diagrams.aws.iot.IotCar
        diagrams.aws.iot.IotCart
        diagrams.aws.iot.IotCertificate
        diagrams.aws.iot.IotCoffeePot
        diagrams.aws.iot.IotCore
        diagrams.aws.iot.IotDesiredState
        diagrams.aws.iot.IotDeviceDefender
        diagrams.aws.iot.IotDeviceGateway
        diagrams.aws.iot.IotDeviceManagement
        diagrams.aws.iot.IotDoorLock
        diagrams.aws.iot.IotEvents
        diagrams.aws.iot.IotFactory
        diagrams.aws.iot.IotFireTvStick
        diagrams.aws.iot.IotFireTv
        diagrams.aws.iot.IotGeneric
        diagrams.aws.iot.IotGreengrassConnector
        diagrams.aws.iot.IotGreengrass
        diagrams.aws.iot.IotHardwareBoard
        diagrams.aws.iot.IotHouse
        diagrams.aws.iot.IotHttp
        diagrams.aws.iot.IotHttp2
        diagrams.aws.iot.IotJobs
        diagrams.aws.iot.IotLambda
        diagrams.aws.iot.IotLightbulb
        diagrams.aws.iot.IotMedicalEmergency
        diagrams.aws.iot.IotMqtt
        diagrams.aws.iot.IotOverTheAirUpdate
        diagrams.aws.iot.IotPolicyEmergency
        diagrams.aws.iot.IotPolicy
        diagrams.aws.iot.IotReportedState
        diagrams.aws.iot.IotRule
        diagrams.aws.iot.IotSensor
        diagrams.aws.iot.IotServo
        diagrams.aws.iot.IotShadow
        diagrams.aws.iot.IotSimulator
        diagrams.aws.iot.IotSitewise
        diagrams.aws.iot.IotThermostat
        diagrams.aws.iot.IotThingsGraph
        diagrams.aws.iot.IotTopic
        diagrams.aws.iot.IotTravel
        diagrams.aws.iot.IotUtility
        diagrams.aws.iot.IotWindfarm
        diagrams.aws.management.AmazonDevopsGuru
        diagrams.aws.management.AmazonManagedGrafana
        diagrams.aws.management.AmazonManagedPrometheus
        diagrams.aws.management.AmazonManagedWorkflowsApacheAirflow
        diagrams.aws.management.AutoScaling
        diagrams.aws.management.Chatbot
        diagrams.aws.management.CloudformationChangeSet
        diagrams.aws.management.CloudformationStack
        diagrams.aws.management.CloudformationTemplate
        diagrams.aws.management.Cloudformation
        diagrams.aws.management.Cloudtrail
        diagrams.aws.management.CloudwatchAlarm
        diagrams.aws.management.CloudwatchEventEventBased
        diagrams.aws.management.CloudwatchEventTimeBased
        diagrams.aws.management.CloudwatchRule
        diagrams.aws.management.Cloudwatch
        diagrams.aws.management.Codeguru
        diagrams.aws.management.CommandLineInterface
        diagrams.aws.management.Config
        diagrams.aws.management.ControlTower
        diagrams.aws.management.LicenseManager
        diagrams.aws.management.ManagedServices
        diagrams.aws.management.ManagementAndGovernance
        diagrams.aws.management.ManagementConsole
        diagrams.aws.management.OpsworksApps
        diagrams.aws.management.OpsworksDeployments
        diagrams.aws.management.OpsworksInstances
        diagrams.aws.management.OpsworksLayers
        diagrams.aws.management.OpsworksMonitoring
        diagrams.aws.management.OpsworksPermissions
        diagrams.aws.management.OpsworksResources
        diagrams.aws.management.OpsworksStack
        diagrams.aws.management.Opsworks
        diagrams.aws.management.OrganizationsAccount
        diagrams.aws.management.OrganizationsOrganizationalUnit
        diagrams.aws.management.Organizations
        diagrams.aws.management.PersonalHealthDashboard
        diagrams.aws.management.Proton
        diagrams.aws.management.ServiceCatalog
        diagrams.aws.management.SystemsManagerAppConfig
        diagrams.aws.management.SystemsManagerAutomation
        diagrams.aws.management.SystemsManagerDocuments
        diagrams.aws.management.SystemsManagerInventory
        diagrams.aws.management.SystemsManagerMaintenanceWindows
        diagrams.aws.management.SystemsManagerOpscenter
        diagrams.aws.management.SystemsManagerParameterStore
        diagrams.aws.management.SystemsManagerPatchManager
        diagrams.aws.management.SystemsManagerRunCommand
        diagrams.aws.management.SystemsManagerStateManager
        diagrams.aws.management.SystemsManager
        diagrams.aws.management.TrustedAdvisorChecklistCost
        diagrams.aws.management.TrustedAdvisorChecklistFaultTolerant
        diagrams.aws.management.TrustedAdvisorChecklistPerformance
        diagrams.aws.management.TrustedAdvisorChecklistSecurity
        diagrams.aws.management.TrustedAdvisorChecklist
        diagrams.aws.management.TrustedAdvisor
        diagrams.aws.management.WellArchitectedTool
        diagrams.aws.media.ElasticTranscoder
        diagrams.aws.media.ElementalConductor
        diagrams.aws.media.ElementalDelta
        diagrams.aws.media.ElementalLive
        diagrams.aws.media.ElementalMediaconnect
        diagrams.aws.media.ElementalMediaconvert
        diagrams.aws.media.ElementalMedialive
        diagrams.aws.media.ElementalMediapackage
        diagrams.aws.media.ElementalMediastore
        diagrams.aws.media.ElementalMediatailor
        diagrams.aws.media.ElementalServer
        diagrams.aws.media.KinesisVideoStreams
        diagrams.aws.media.MediaServices
        diagrams.aws.migration.ApplicationDiscoveryService
        diagrams.aws.migration.CloudendureMigration
        diagrams.aws.migration.DatabaseMigrationService
        diagrams.aws.migration.DatasyncAgent
        diagrams.aws.migration.Datasync
        diagrams.aws.migration.MigrationAndTransfer
        diagrams.aws.migration.MigrationHub
        diagrams.aws.migration.ServerMigrationService
        diagrams.aws.migration.SnowballEdge
        diagrams.aws.migration.Snowball
        diagrams.aws.migration.Snowmobile
        diagrams.aws.migration.TransferForSftp
        diagrams.aws.ml.ApacheMxnetOnAWS
        diagrams.aws.ml.AugmentedAi
        diagrams.aws.ml.Comprehend
        diagrams.aws.ml.DeepLearningAmis
        diagrams.aws.ml.DeepLearningContainers
        diagrams.aws.ml.Deepcomposer
        diagrams.aws.ml.Deeplens
        diagrams.aws.ml.Deepracer
        diagrams.aws.ml.ElasticInference
        diagrams.aws.ml.Forecast
        diagrams.aws.ml.FraudDetector
        diagrams.aws.ml.Kendra
        diagrams.aws.ml.Lex
        diagrams.aws.ml.MachineLearning
        diagrams.aws.ml.Personalize
        diagrams.aws.ml.Polly
        diagrams.aws.ml.RekognitionImage
        diagrams.aws.ml.RekognitionVideo
        diagrams.aws.ml.Rekognition
        diagrams.aws.ml.SagemakerGroundTruth
        diagrams.aws.ml.SagemakerModel
        diagrams.aws.ml.SagemakerNotebook
        diagrams.aws.ml.SagemakerTrainingJob
        diagrams.aws.ml.Sagemaker
        diagrams.aws.ml.TensorflowOnAWS
        diagrams.aws.ml.Textract
        diagrams.aws.ml.Transcribe
        diagrams.aws.ml.Translate
        diagrams.aws.mobile.Amplify
        diagrams.aws.mobile.APIGatewayEndpoint
        diagrams.aws.mobile.APIGateway
        diagrams.aws.mobile.Appsync
        diagrams.aws.mobile.DeviceFarm
        diagrams.aws.mobile.Mobile
        diagrams.aws.mobile.Pinpoint
        diagrams.aws.network.APIGatewayEndpoint
        diagrams.aws.network.APIGateway
        diagrams.aws.network.AppMesh
        diagrams.aws.network.ClientVpn
        diagrams.aws.network.CloudMap
        diagrams.aws.network.CloudFrontDownloadDistribution
        diagrams.aws.network.CloudFrontEdgeLocation
        diagrams.aws.network.CloudFrontStreamingDistribution
        diagrams.aws.network.CloudFront
        diagrams.aws.network.DirectConnect
        diagrams.aws.network.ElasticLoadBalancing
        diagrams.aws.network.ElbApplicationLoadBalancer
        diagrams.aws.network.ElbClassicLoadBalancer
        diagrams.aws.network.ElbNetworkLoadBalancer
        diagrams.aws.network.Endpoint
        diagrams.aws.network.GlobalAccelerator
        diagrams.aws.network.InternetGateway
        diagrams.aws.network.Nacl
        diagrams.aws.network.NATGateway
        diagrams.aws.network.NetworkFirewall
        diagrams.aws.network.NetworkingAndContentDelivery
        diagrams.aws.network.PrivateSubnet
        diagrams.aws.network.Privatelink
        diagrams.aws.network.PublicSubnet
        diagrams.aws.network.Route53HostedZone
        diagrams.aws.network.Route53
        diagrams.aws.network.RouteTable
        diagrams.aws.network.SiteToSiteVpn
        diagrams.aws.network.TransitGateway
        diagrams.aws.network.VPCCustomerGateway
        diagrams.aws.network.VPCElasticNetworkAdapter
        diagrams.aws.network.VPCElasticNetworkInterface
        diagrams.aws.network.VPCFlowLogs
        diagrams.aws.network.VPCPeering
        diagrams.aws.network.VPCRouter
        diagrams.aws.network.VPCTrafficMirroring
        diagrams.aws.network.VPC
        diagrams.aws.network.VpnConnection
        diagrams.aws.network.VpnGateway
        diagrams.aws.quantum.Braket
        diagrams.aws.quantum.QuantumTechnologies
        diagrams.aws.robotics.RobomakerCloudExtensionRos
        diagrams.aws.robotics.RobomakerDevelopmentEnvironment
        diagrams.aws.robotics.RobomakerFleetManagement
        diagrams.aws.robotics.RobomakerSimulator
        diagrams.aws.robotics.Robomaker
        diagrams.aws.robotics.Robotics
        diagrams.aws.satellite.GroundStation
        diagrams.aws.satellite.Satellite
        diagrams.aws.security.AdConnector
        diagrams.aws.security.Artifact
        diagrams.aws.security.CertificateAuthority
        diagrams.aws.security.CertificateManager
        diagrams.aws.security.CloudDirectory
        diagrams.aws.security.Cloudhsm
        diagrams.aws.security.Cognito
        diagrams.aws.security.Detective
        diagrams.aws.security.DirectoryService
        diagrams.aws.security.FirewallManager
        diagrams.aws.security.Guardduty
        diagrams.aws.security.IdentityAndAccessManagementIamAccessAnalyzer
        diagrams.aws.security.IdentityAndAccessManagementIamAddOn
        diagrams.aws.security.IdentityAndAccessManagementIamAWSStsAlternate
        diagrams.aws.security.IdentityAndAccessManagementIamAWSSts
        diagrams.aws.security.IdentityAndAccessManagementIamDataEncryptionKey
        diagrams.aws.security.IdentityAndAccessManagementIamEncryptedData
        diagrams.aws.security.IdentityAndAccessManagementIamLongTermSecurityCredential
        diagrams.aws.security.IdentityAndAccessManagementIamMfaToken
        diagrams.aws.security.IdentityAndAccessManagementIamPermissions
        diagrams.aws.security.IdentityAndAccessManagementIamRole
        diagrams.aws.security.IdentityAndAccessManagementIamTemporarySecurityCredential
        diagrams.aws.security.IdentityAndAccessManagementIam
        diagrams.aws.security.InspectorAgent
        diagrams.aws.security.Inspector
        diagrams.aws.security.KeyManagementService
        diagrams.aws.security.Macie
        diagrams.aws.security.ManagedMicrosoftAd
        diagrams.aws.security.ResourceAccessManager
        diagrams.aws.security.SecretsManager
        diagrams.aws.security.SecurityHubFinding
        diagrams.aws.security.SecurityHub
        diagrams.aws.security.SecurityIdentityAndCompliance
        diagrams.aws.security.ShieldAdvanced
        diagrams.aws.security.Shield
        diagrams.aws.security.SimpleAd
        diagrams.aws.security.SingleSignOn
        diagrams.aws.security.WAFFilteringRule
        diagrams.aws.security.WAF
        diagrams.aws.storage.Backup
        diagrams.aws.storage.CloudendureDisasterRecovery
        diagrams.aws.storage.EFSInfrequentaccessPrimaryBg
        diagrams.aws.storage.EFSStandardPrimaryBg
        diagrams.aws.storage.ElasticBlockStoreEBSSnapshot
        diagrams.aws.storage.ElasticBlockStoreEBSVolume
        diagrams.aws.storage.ElasticBlockStoreEBS
        diagrams.aws.storage.ElasticFileSystemEFSFileSystem
        diagrams.aws.storage.ElasticFileSystemEFS
        diagrams.aws.storage.FsxForLustre
        diagrams.aws.storage.FsxForWindowsFileServer
        diagrams.aws.storage.Fsx
        diagrams.aws.storage.MultipleVolumesResource
        diagrams.aws.storage.S3GlacierArchive
        diagrams.aws.storage.S3GlacierVault
        diagrams.aws.storage.S3Glacier
        diagrams.aws.storage.SimpleStorageServiceS3BucketWithObjects
        diagrams.aws.storage.SimpleStorageServiceS3Bucket
        diagrams.aws.storage.SimpleStorageServiceS3Object
        diagrams.aws.storage.SimpleStorageServiceS3
        diagrams.aws.storage.SnowFamilySnowballImportExport
        diagrams.aws.storage.SnowballEdge
        diagrams.aws.storage.Snowball
        diagrams.aws.storage.Snowmobile
        diagrams.aws.storage.StorageGatewayCachedVolume
        diagrams.aws.storage.StorageGatewayNonCachedVolume
        diagrams.aws.storage.StorageGatewayVirtualTapeLibrary
        diagrams.aws.storage.StorageGateway
        diagrams.aws.storage.Storage
        
    - Use the following example to create a diagram:
    
    ```python
        from urllib.request import urlretrieve

        from diagrams import Cluster, Diagram
        from diagrams.aws.compute import EC2
        from diagrams.aws.network import ElbApplicationLoadBalancer
        from diagrams.custom import Custom

        github_actions_url = (
            "https://iconduck.com/api/v2/vectors/vctrzwq272bb/media/png/256/download"
        )
        github_actions_icon = "github_actions_icon.png"

        urlretrieve(github_actions_url, github_actions_icon)

        with Diagram("Pandape Gateway Infrastructure", show=False, filename="architecture"):
            vcs = Custom("GitHub Actions", icon_path="github_actions_icon.png")

            with Cluster("VPC"):
                with Cluster("Public Subnet"):
                    app_lb = ElbApplicationLoadBalancer("Application Load Balancer")

                with Cluster("EC2 Instances"):
                    with Cluster("Private Subnet"):
                        ec2_instances = [EC2("Instance 1"), EC2("Instance 2")]

                    app_lb >> ec2_instances
                    vcs >> ec2_instances
    ```

    
    **AWS Infrastructure Code for `{infra_folder}`:**
    ```
    {infrastructure_code}
    ```
    
    Generate only the markdown file and the diagram code.
    """)


def human_prompt(infrastructure_code: str, infra_folder: str) -> HumanMessage:
    return HumanMessage(f"""
     Analyze the following AWS infrastructure code (written in Terraform/CDK) and generate two files, one for the diagram and one for the README, 
     
     {infrastructure_code}
     """)
