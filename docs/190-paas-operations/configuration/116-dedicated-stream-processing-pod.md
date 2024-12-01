---
layout: cluedin
nav_order: 16
parent: Configuration
grand_parent: PaaS operations
permalink: /paas-operations/config/dedicated-stream-processing-pod
title: Dedicated Stream Processing Pod
tags: ["deployment", "kubernetes", "web", "frontend"]
headerIcon: "paas"
---
Provides a dedicated pod which only processes streams.

**Prerequisites**
- Access to your Kubernetes cluster
- Helm installed

## Deployment
Take the current deployment for `cluedin-server-processing`.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: cluedin
    release: <replace-with-release-name>
    role: processing-streams
  name: <replace-with-release-name>-processing-streams
  namespace: cluedin
spec:
  replicas: 1
  selector:
    matchLabels:
      app: cluedin
      release: <replace-with-release-name>
      role: processing-streams
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: cluedin
        release: <replace-with-release-name>
        role: processing-streams
    spec:
      containers:
      - envFrom:
        - configMapRef:
            name: <replace-with-release-name>-server
        - configMapRef:
            name: <replace-with-release-name>-server-processing-streams
        - configMapRef:
            name: c<replace-with-release-name>server-crawling-disable
        - secretRef:
            name: <replace-with-release-name>-sql-connectionstrings
        image: cluedin/cluedin-server:<replace-with-current-cluedin-version-tag>
        imagePullPolicy: Always
        livenessProbe:
          failureThreshold: 3
          httpGet:
            path: /health/liveness
            port: 9000
            scheme: HTTP
          initialDelaySeconds: 300
          periodSeconds: 20
          successThreshold: 1
          timeoutSeconds: 5
        name: cluedin-processing
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
        readinessProbe:
          failureThreshold: 15
          httpGet:
            path: /health/liveness
            port: 9000
            scheme: HTTP
          initialDelaySeconds: 180
          periodSeconds: 30
          successThreshold: 1
          timeoutSeconds: 5
        resources:
          limits:
            cpu: "4"
            memory: 6Gi
          requests:
            cpu: "4"
            memory: 6Gi
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /components
          name: components
      dnsPolicy: ClusterFirst
      imagePullSecrets:
      - name: docker-registry-key
      initContainers:
      - image: cluedin/nuget-installer:develop
        imagePullPolicy: IfNotPresent
        name: initcomponents
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /components
          name: components
        - mountPath: /packages/packages.txt
          name: packages-volume
          subPath: packages.txt
        - mountPath: /packages/nuget.config
          name: nuget-volume
          subPath: nuget.config
      - args:
        - service
        - <replace-with-release-name>-redis
        - -n
        - cluedin
        image: groundnuty/k8s-wait-for:v1.3
        imagePullPolicy: Always
        name: wait-redis
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      - args:
        - service
        - <replace-with-release-name>-sqlserver
        - -n
        - cluedin
        image: groundnuty/k8s-wait-for:v1.3
        imagePullPolicy: Always
        name: wait-sqlserver
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      nodeSelector:
        beta.kubernetes.io/os: linux
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
      volumes:
      - emptyDir: {}
        name: components
      - configMap:
          defaultMode: 420
          name: <replace-with-release-name>-server-packages
        name: packages-volume
      - name: nuget-volume
        secret:
          defaultMode: 420
          secretName: <replace-with-release-name>-server-nuget
```

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
    release: <replace-with-release-name>
  name: <replace-with-release-name>-server-processing-streams
  namespace: cluedin
```