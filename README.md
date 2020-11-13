Datadog Kubernetes Security Rules
--


1) Rule - User attempt clusterrolebinding to cluster-admin

    2) Tested on AKS

    3) Sample commands used to test:

    `kubectl create clusterrolebinding root-cluster-admin-binding --clusterrole=cluster-admin --user=jenks`  
    `kubectl delete clusterrolebinding root-cluster-admin-binding`
    
    4) Requires the json parser in the sample pipeline

2) Rule - Clusterrole or role created with verb or resource wildcard  
  
    2) Tested on AKS  
    
    3) Sample commands used to test:
    
    `kubectl create role jenks_test --verb=create --resource=pods`  
    `kubectl create clusterrole jenks_test --verb=create --resource=pods`  

    4) 4) Requires the json parser in the sample pipeline and the string builder processors  
Utility
--

dd_secmon_util.py - will list security rules in an account or pull a rules JSON.  It has been written for use
only and very minimally tested.  

* Get a rule - `python3 dd_secmon_util.py -g "Apache HTTP requests from security scanner"`  
* List rules - `python3 dd_secmon_util.py -l`  

Need to add ability to put rules in another account.  
