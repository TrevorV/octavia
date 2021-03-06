..
 This work is licensed under a Creative Commons Attribution 3.0 Unported
 License.

 http://creativecommons.org/licenses/by/3.0/legalcode

==========================================
Octavia Controller
==========================================

Launchpad blueprint:

https://blueprints.launchpad.net/octavia/+spec/controller

Octavia is an operator-grade reference implementation for Load Balancing as a
Service (LBaaS) for OpenStack.  The component of Octavia that does the load
balancing is known as Amphora.

The component of Octavia that provides command and control of the Amphora is
the Octavia controller.

Problem description
===================

Octavia requires a controller component that provides the following
capabilities:

* Processing Amphora configuration updates and making them available to the
  Amphora driver
* Providing certificate information to the Amphora driver
* Deploying Amphora instances
* Managing the Amphora spares pool
* Cleaning up Amphora instances that are no longer needed
* Monitoring the health of Amphora instances
* Processing alerts and messages from the Amphora (example "member down")
* Respecting colocation / apolocation / flavor requirements of the Amphora
* Processing statistical data from the Amphora including communicating with
  metering services, such as Ceilometer
  (https://blueprints.launchpad.net/ceilometer/+spec/ceilometer-meter-lbaas)
* Responding to API requests sent by the API processes
* Proxy Amphora data to other OpenStack services such as Swift for log file
  archival

Proposed change
===============

The Octavia controller will consist of the following components:

* Amphora Driver
* API Manager
* Certificate Library
* Compute Driver
* Deploy Worker
* Health Manager
* Housekeeping Manager
* Network Driver
* Services Proxy

 .. graphviz:: controller.dot

The manager and proxy components should be implemented as independent
processes to provide a level of autonomy to these controller functions.

The highly available database will provide the persistent "brain" for the
Octavia controller.  Octavia controller processes will share state and
information about the Amphora, load balancers, and listeners via the database.
It is expected that the Octavia controller and Amphora driver will directly
interact with the database but the Amphorae will never directly access the
database.

By using a highly available database, Octavia controllers themselves do not
directly keep any stateful information on Amphorae. Because of this, Amphorae
are not assigned to any specific controller. Any controller is able to service
monitoring, heartbeat, API, and other requests coming to or from Amphorae.

**Amphora Driver**

The Amphora driver abstracts the backend implementation of an Amphora.  The
controller will interact with Amphora via the Amphora driver.  This interface
is defined in the amphora-driver-interface specification.

**API Manager**

The API Manager is event driven and tasked with servicing requests from the
API components via an Oslo messaging queue.  It is also the primary lifecycle
management component for Amphora.  Many API requests can be serviced by
querying the database for the current state of load balancers and listeners.

Requests for a new load balancer or listener will cause the API Manager to
spawn a Deploy Worker process.  Spawning a seperate process makes sure that
the API Manager can continue to service API requests while the longer running
deployment process is progressing.

API requests may also cause the API Manager to push updated configurations to
the Octavia database and notify the driver to push an updated configuration
to the listener.  A worker will be dispatched to supervise the process of
pushing out the new configuration.

Delete requests for load balancers or listeners will call the Amphora driver
wrap up method to gracefully shutdown the processes, ship logs, ship
statistics, un-plug network resources, and mark pending delete status in the
database for the Housekeeping Manager to cleanup the Amphora should it no
longer be needed.

**Compute Driver**

The Compute Driver abstracts the implementation of instantiating the virtual
machine, container, appliance, or device that the Amphora will run in.

**Deploy Worker**

The Deploy Worker is spawned from the API Manager or the Health
Manager.  It interfaces with the compute driver (in some deployment scenarios),
network driver, and Amphora driver to activate Amphora instances,
load balancers, and listeners.

When a request for a new instance or failover is received the Deploy Worker
will have responsibility for connecting the appropriate networking ports to the
Amphora via the network driver and triggering a configuration push via the
Amphora driver.  This will include validating that the targeted Amphora
has the required networks plumbed to the Amphora.

The Amphora configured by the Deploy Worker may be an existing Amphora
instance, a new Amphora from the spares pool, or a newly created Amphora.
This determination will be made based on the apolocation requirements of
the load balancer, the load balancer count on the existing Amphora, and
the availability of ready spare Amphora in the spares pool.

The Deploy Worker will be resposible for passing in the required metadata
via config drive when deploying an Amphora.  This metadata will include:
a list of controller IP addresses, controller certificate authority
certificate, and the Amphora certificate and key file.

The main flow of the Deploy Worker is described in the
amphora-lifecycle-management specification as the Activate Amphora sequence.

**Certificate Library**

The Certificate Library provides an abstration for workers to access security
data stored in OpenStack Barbican from the Amphora Driver.  It will provide a
short term (1 minute) cache of the security contents to facilitate the
efficient startup of a large number of listeners sharing security content.

**Health Manager**

The Health Manager is tasked with checking for missing or unhealthy Amphora
stored in the highly available database.  The amphora-lifecycle-management
specification details the health monitoring sequence.

The health monitor will have a separate thread that checks these timestamps on
a configurable interval to see if the Amphora has not provided a heartbeat in
the required amount of time which is another configurable setting.  Should a
Amphora fail to report a heartbeat in the configured interval the
Health Manager will initiate a failover of the Amphora by spawning a deploy
worker and will update the status of the listener in the database.

The Health Manager will have to be aware of the load balancer associated with
the failed listener to decide if it needs to fail over additional listeners to
migrate the failed listener to a new Amphora.

**Housekeeping Manager**

The Housekeeping Manager will manage the spare Amphora pool and the teardown
of Amphora that are no longer needed.  On a configurable interval the
Housekeeping Manager will check the Octavia database to identify the required
cleanup and maintenance actions.  The amphora-lifecycle-management
specification details the Create, Spare, and Delete Amphora sequences the
Housekeeping Manager will follow.

The operator can specify a number of Amphora instances to be held in a spares
pool.  Building Amphora instances can take a long time so the Housekeeping
Manager will spawn threads to manage the number of Amphorae in the spares pool.

The Housekeeping Manager will interface with the compute driver,
network driver, and the Certificate Manager to accomplish the create
and delete actions.

**Network Driver**

The Network Driver abstracts the implementation of connecting an Amphora to
the required networks.

**Services Proxy**

The Services Proxy enables Amphora to reach other cloud services directly over
the Load Balancer Network where the controller may need to provide
authentication tokens on behalf of the Amphora, such as when archiving load
balancer traffic logs into customer swift containers.


Alternatives
------------


Data model impact
-----------------


REST API impact
---------------


Security impact
---------------


Notifications impact
--------------------


Other end user impact
---------------------


Performance Impact
------------------


Other deployer impact
---------------------


Developer impact
----------------


Implementation
==============

Assignee(s)
-----------
Michael Johnson <johnsom>

Work Items
----------


Dependencies
============


Testing
=======


Documentation Impact
====================


References
==========

| Amphora lifecycle management: https://review.openstack.org/#/c/130424/
| LBaaS metering:
|    https://blueprints.launchpad.net/ceilometer/+spec/ceilometer-meter-lbaas
