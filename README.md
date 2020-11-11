Datadog Kubernetes Security Rules
--


1) Rule - User attempt clusterrolebinding to cluster-admin

    2) Tested on AKS

    3) Sample commands used to test:

    `kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=jenks`  
    `kubectl delete clusterrolebinding root-cluster-admin-binding`

2) Rule - Clusterrole or role created with verb or resource wildcard  
  
    2) Tested on AKS  
    
    3) Sample commands used to test:
    
    `kubectl create role jenks_test --verb=create --resource=pods`  
    `kubectl create clusterrole jenks_test --verb=create --resource=pods`  
