# IAM

Ensures the right people do the right job within the right set of permissions.

1. Create indentities related to people, users, APIs or services. 
2. Authentication factors: Each entity has it's own characteristics unique to it's identity. If this match with the identity they are trying to access, the user is confirmed. Examples are username, password, pin, certificates, biometric...
3. Roles: Each identity has specific roles that defines the scope under it functions.

## IAM features

Give permissions of resources to other people without sharing accounts or passwords.
Grant role-based acces to users
Enable multi-factor authorization
Enable and manage permissions and access policies

## Terminology

Resource: Objects within a service: roles, groups, policies, users.
Identities: Users permitted and authorised to perform roles or actions
Entities: Subset of resources for authentication purpouses. 
Principals: A person or app asking to use resources after signin in.

# Security through policies

## Types

Identity policies: attached to identities.
Resource: attached to resources and define who is authorithed and how it is authorised.
Session: determines access to resources for limited time.

# Security through network management

Layered model:

1. Network Security Groups: Deny all unless allowd. Every traffic is denied if there is not an allowing rule. No need for deny rules.

2. NACLs: Rules to protects specific instanes of an VPC. They contain deny rules. 

3. Vendor specific: Specific tools provided by the cloud computing provider. AWS offers DNS and network firewall for example.

# Security through storage management

Geographical boundaries
Role-based authotrisation
Data Encryption

Types of storage are Relational Database Service RDS, Simple Storage Service S3, Redis...


# Additional Concepts

## Disaster Revcovery and Backup

Cold DR: Cheapest, simpliest approach. High Recovery Time Objective. Simple data storage and machine snapshots. All snapshots must be recovered to restore business operations

Warm DR: Almost in real time sync. The medium cost. Recobery Time Objective is the time It takes to configure the DR site to become operational

Hot DR: Parallel work between in-site and DR. Near to 0 RTO. Expensive. Service is rapidly shifted to the DR site.


## Security through Monitoring and Logging.

Real-Time logging: All identities and resources logged in real-time
Monitoring and Logging API calls: Logging for recording API calls made to the cloud infrastructure.
Credemtial Reports: User account logs. Logs the account, last time used, password last change data, password last used date...

For AWS we get some components for this issues:

IAM logs acces management and makes credential reports
CloudTrail logs all API calls made to AWS resources
CloudWatch monitors the entire infrastructure and informs about status changes for ensuring better resource utilisation
GuardDuty ensures continuous monitoring of any possible malicious activity and unathourised behaviour.

## Updates and Patching

Essential feature that allows us to update and patch our infrastructure. "Automated & Scheduled Patch Management" ensures that these updates are routinely applied.

In AWS is made through Systems Manager.
