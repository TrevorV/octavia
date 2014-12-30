# Copyright 2014 Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock

from octavia.amphorae.drivers.haproxy_reference import api_driver as driver
from octavia.amphorae.drivers.haproxy_reference import data_models as models
from octavia.openstack.common import log as logging
from octavia.openstack.common import uuidutils
from octavia.common import constants
from octavia.tests.unit import base as base

LOG = logging.getLogger(__name__)


class AmphoraAPIDriverTest(base.TestCase):
    FAKE_UUID_1 = uuidutils.generate_uuid()
    FAKE_PEM_FILENAME = "/some/file/location/name"

    def setUp(self):
        super(AmphoraAPIDriverTest, self).setUp()
        self.driver = driver.AmphoraAPIDriver(LOG)


    def create_topology(self):
        topology = models.Topology()
        topology.hostname = "some_hostname"
        topology.ip = "10.0.0.1"
        topology.ha_ip = "10.0.0.2"
        topology.topology = "SINGLE"
        topology.role = "ACTIVE"
        topology.uuid = self.FAKE_UUID_1
        return topology

    def test_get_logger(self):
        self.assertEqual(LOG, self.driver.log)

    def test_get_topology(self):
        topology = self.driver.get_topology()
        self.assertIsInstance(topology, models.Topology)

    def test_set_topology(self):
        topology = models.Topology()
        topology.hostname = "some_hostname"
        topology.ip = "10.0.0.1"
        topology.ha_ip = "10.0.0.2"
        topology.topology = "SINGLE"
        topology.role = "ACTIVE"
        topology.uuid = self.FAKE_UUID_1
        self.driver.set_topology(topology)


    def test_get_info(self):
        info = self.driver.get_info()
        self.assertIsInstance(info, models.Info)

    def test_get_details(self):
        details = self.driver.get_details()
        self.assertIsInstance(details, models.Details)

    def test_get_all_listeners(self):
        listeners = self.driver.get_all_listeners()
        self.assertIsInstance(listeners, list)
        [self.assertIsInstance(l, models.ListenerStatus) for l in listeners]

    def test_get_listener_status(self):
        status = self.driver.get_listener_status(self.FAKE_UUID_1)
        self.assertIsInstance(status, models.ListenerStatus)

    def test_start_listener(self):
        self.driver.start_listener(self.FAKE_UUID_1)
        status = self.driver.get_listener_status(self.FAKE_UUID_1)
        self.assertEqual(status.provisioning_status, constants.ACTIVE)

    def test_stop_listener(self):
        self.driver.stop_listener(self.FAKE_UUID_1)
        status = self.driver.get_listener_status(self.FAKE_UUID_1)
        self.assertEqual(status.provisioning_status, constants.OFFLINE)

    def test_delete_listener(self):
        self.driver.delete_listener(self.FAKE_UUID_1)
        listener = self.driver.get_listener_status(self.FAKE_UUID_1)
        self.assertIsNone(listener)

    def test_upload_cert_pem(self):
        self.driver.upload_cert_pem(self.FAKE_UUID_1, self.FAKE_PEM_FILENAME)

    def test_get_cert_5sum(self):
        md5sum = self.driver.get_cert_5sum(self.FAKE_UUID_1,
                                           self.FAKE_PEM_FILENAME)
        self.assertNotNone(md5sum)

    def test_delete_cert_pem(self):
        self.driver.delete_cert_pem(self.FAKE_UUID_1, self.FAKE_PEM_FILENAME)
        md5sum = self.driver.get_cert_5sum(self.FAKE_UUID_1,
                                           self.FAKE_PEM_FILENAME)
        self.assertIsNone(md5sum)

    def test_upload_config(self):
        config = {'name': 'fake_config'}
        self.driver.upload_config(self.FAKE_UUID_1, config)