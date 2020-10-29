Datadog Kubernetes Security Rules
--


1) Rule - User attempt clusterrolebinding to cluster-admin

2) Tested on AKS

3) Commands used to test:

`kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=jenks`  
`kubectl delete clusterrolebinding root-cluster-admin-binding`
