# Cloud Security

The essential concept to be protected is Data. There is 3 funamental categories of Data.

Condifential: Critical data for an organization. Exposure can damage operability and reputation of an organization. High risk. Personal identifiable information, for example.
Internal: Medium risk data for an organization. Exposure can damage operability or reputation on a medium risk perspective. Internal structure data, budgets or future projects.
Public data: No-risk data. Information that is meant to be public such as websites or public information sources.
No damage if leaked.


## Cloud Data Lifecycle

1. Create: Initial phase. New or refreshed data. Data ownership and classification must be done here. 
Security aspects: Implementing TLS or SSL for secure communication. Encryption and secure connections.
2. Store: Phase where data is stores on a database normally, based on its form and classification. 
Security aspects: Encryption and Backup.
3. Use: Apps or services using the stored data. Decryption done here for usage.
Security aspects: Secure connection, secure platform and authentication, restrict permissions for non unauthorized manipulation, secure virtualisation without leaks between shared resources.
4. Share: After use, relocation of data inside or outside the cloud for further utilities. 
Security aspects: Jurisdiction and law compliance, data loss prevention.
5. Archive: Similar to storage but in long-term perspective. Save data for future, not inmediate, use.
Security aspects: Encryption, Physical security over storage devices, location of storage, backup procedure.
6. Destroy: After every phase data should be evaluated and, if there is no further use, it should be destroyed to avoid misuse. 


## Security Issues:

Data confidentiality. Hosting data in the cloud imply a confidentiality risk since the user has no physical acces to the data once it is outsourced. 
Virtualisation issues. Hosting data in shared resources implys risk of isolation issues and data exposure to other users using the same resources. 
Insecure interface or API: Adding another layer of services always creates new vulnerability points and risks. Software or APIs to manage data on the cloud are no exception to that.
Malicious insiders.
Account or service hijacking: Phising, vulnerability exploitation or password reuse can cause hijacking and access to cloud resources and data.
ACM: Acces control mechanicsm. Efficient and reliable access to resources and data is critical since data and users are in differnet domains.
