#    Copyright 2014 Blue Box Group, Inc.
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

from wsme import types as wtypes
from wsmeext import pecan as wsme_pecan

from amphora_api.v1.controllers import base
from amphora_api.v1.controllers import topology

class V1Controller(base.BaseController):

    topology = topology.TopologyController()

    @wsme_pecan.wsexpose(wtypes.text)
    def get(self):
        # TODO(sbalukoff): Return specific API version information
        return "V1"

