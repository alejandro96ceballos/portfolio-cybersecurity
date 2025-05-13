## Security Goals and Control

# Non-repudiation

Enoforcing the inavility of a subject to deny that they participated in a digital operation

## AAA

# Character mode vs Packet mode

* Character mode

Sends keystrokes or commands to a network admission device

* Packet mode

Network admission serves as proxy for authentication on behalf of services as DNS, FTP...

Authentication and authorization should happen before a connection is establshed. TCP makes the 3-way handshake before authentication and authotization as a sub-optimal way of AAA and violates zero trust principles


## Authentication

* People

- Username and password
- Smart card token or fob
- Digital certificates
- Biometric attributes
- QR codes on private devices

* Systems (NPE)

- Endpoint authentication 

# Models

* DAC

- Grants access control decisions to owners and custodians
- Each resource has an owner who dictates permissions or shares
- Owners grant and revoke access rights at will
- Flexible but inconsistent controls
- Prone to privilege creep

* RBAC

- Access is asigned within predetermined roles
- Users are asigned roles not permissions directly
- Agile and escalable


Both are combinable

* MAC

- Mathematical model with strict predefined labels and rules
- Classification levels(top secret, secret, confidential...)
- Resources are labeled with those classifications
- Rules comapare permissions and labels to determine authorization
- No owner, comite based

* ABAC

- Authorization based on attributes given to each user
- Combination of discretional and non-discretional methods
- Attributes can be environmental, user based, resource based...

* ABDAC

- Combination of ABAC and DAC
- Considers dynamic factors as risk assessment, user attributes, resource attributes and contextual information
- Decisions are made in-real time over decision trees
- Fine-grained and context-aware access control. Zero-trust.
- Can include ML

* Rule-based access control

- Rules define condictions to be met to be authorized such as user attributes, time of acces, IP adress, meta-data...

# Control

## Categories

* Technical controls

- Confidentiality, integrity, authenticity and availability protocols runned by the system
- Defense against unauthorized access or misuse
- Facilitates detections of security violations 

Device hardening, IAM, cryptographic key management, cloud-based threat modeling tools, SIEM and SOAR

* Managerial controls

- Policies, procedures, guidelines. Set of rules for people to follow on an organization systems use.

* Operational controls

- Ongoing maintenance
- Monitoring controls
- Incident response

* Physical controls

- Barriers
- Security employees
- Locking mechanisms
- Mantraps and faraday cages
- Enviromental controls
- Surveillance equipment
- Sensors and alarms
- Safes, cabinets, security areas
- Fire detection and suppression

* Control types

- Preventive

Stops threats before they happend. 
- Deterrent

Discourages an attacker from continuing

- Detective

Identifies an attach and the steps of the kill chain
- Corrective

Restores the state of a system before an attack happened
- Compensating

Temporary solution

- Directive

Policies and regulations to mantain compliance and consistency
