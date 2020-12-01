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

dd_secmon_util.py - will list security rules in an account, pull a rule's JSON or add a rule based on pulled JSON from 
Get a rule.  It has been written for use only and very minimally tested.    

* Get a rule - `python3 dd_secmon_util.py -g "Apache HTTP requests from security scanner"`  
* List rules - `python3 dd_secmon_util.py -l`  
* Add a rule (from JSON pulled from Get a rule above)- `python3 dd_secmon_util.py -a "Apache HTTP requests from security scanner"`  
