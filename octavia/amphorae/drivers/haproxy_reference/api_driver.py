#    Copyright 2014 Rackspace
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class AmphoraAPIDriver(object):
    def get_topology(self):
        pass

    def set_topology(self):
        pass

    def get_info(self):
        pass

    def get_details(self):
        pass

    def get_all_listeners(self):
        pass

    def get_listener_status(self, listener_id):
        pass

    def start_listener(self, listener_id):
        pass

    def stop_listener(self, listener_id):
        pass

    def delete_listener(self, listener_id):
        pass

    def upload_cert_pem(self, listener_id, pem_filename):
        pass

    def get_cert_5sum(self, listener_id, pem_filename):
        pass

    def delete_cert_pem(self, listener_id, pem_filename):
        pass

    def upload_config(self, listener_id):
        pass