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

from amphora_api.v1.controllers import base
from amphora_api.v1.types import topology as topology_types
from wsme import types as wtypes
from wsmeext import pecan as wsme_pecan


class TopologyController(base.BaseController):

    def __init__(self):
        super(TopologyController, self).__init__()
        self.handler = self.handler.topology

    @wsme_pecan.wsexpose(topology_types.TopologyResponse, wtypes.text)
    def get(self):
        """Gets the amphora's topology configuration."""
        # TODO(sbalukoff): Implement this. :)
        return "GET topology"

    @wsme_pecan.wsexpose(topology_types.TopologyResponse,
                         body=topology_types.TopologyPOST,
                         status_code=202)
    def post(self, req):
        """Sets the amphora's topology configuration."""
        # TODO(sbalukoff): Implement this. :)
        return "POST topology"
