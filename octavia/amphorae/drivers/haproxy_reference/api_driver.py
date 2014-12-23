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

import requests


class AmphoraAPIDriver(object):
    def get_topology(self):
        r = requests.get(url="http://test.octavia.com/topology")
        return r

    def set_topology(self, topology):
        r = requests.put(url="http://test.octavia.com/topology", data=topology)
        return r

    def get_info(self):
        r = requests.get(url="http://test.octavia.com/info")
        return r

    def get_details(self):
        r = requests.get(url="http://test.octavia.com/details")
        return r

    def get_all_listeners(self):
        r = requests.get(url="http://test.octavia.com/listeners")
        return r

    def get_listener_status(self, listener_id):
        url = "http://test.octavia.com/listeners/{listener_id}".format(
            listener_id=listener_id)
        r = requests.get(url=url)
        return r

    def start_listener(self, listener_id):
        url = "http://test.octavia.com/listeners/{listener_id}".format(
            listener_id=listener_id)
        r = requests.get(url=url)
        return r

    def stop_listener(self, listener_id):
        url = "http://test.octavia.com/listeners/{listener_id}".format(
            listener_id=listener_id)
        r = requests.get(url=url)
        return r

    def delete_listener(self, listener_id):
        url = "http://test.octavia.com/listeners/{listener_id}".format(
            listener_id=listener_id)
        r = requests.delete(url=url)
        return r

    def upload_cert_pem(self, listener_id, pem_filename):
        url = ("http://test.octavia.com/listeners/{listener_id}",
               "/certificates/{filename}".format(
                   listener_id=listener_id, filename=pem_filename))
        r = requests.put(url=url, data=pem_filename)
        return r

    def get_cert_5sum(self, listener_id, pem_filename):
        url = ("http://test.octavia.com/listeners/{listener_id}",
               "/certificates/{filename}".format(
                   listener_id=listener_id, filename=pem_filename))
        r = requests.get(url=url)
        return r

    def delete_cert_pem(self, listener_id, pem_filename):
        url = ("http://test.octavia.com/listeners/{listener_id}",
               "/certificates/{filename}".format(
                   listener_id=listener_id, filename=pem_filename))
        r = requests.delete(url=url)
        return r

    def upload_config(self, listener_id, config):
        url = "http://test.octavia.com/listeners/{listener_id}".format(
            listener_id=listener_id)
        r = requests.put(url=url, data=config)
        return r