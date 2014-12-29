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

from amphora_api.v1.types import base


class TopologyResponse(base.BaseType):
    """Defines which attributes should be shown in any response."""
    hostname = wtypes.wsattr(wtypes.text)
    uuid = wtypes.wsattr(wtypes.UuidType())
    topology = wtypes.wsattr(wtypes.text)
    role = wtypes.wsattr(wtypes.text)
    ip = wtypes.wsattr(base.IPAddressType())
    ha_ip = wtypes.wsattr(base.IPAddressType())


class TopologyPOST(base.BaseType):
    """Defines mandatory and optional attributes of a POST request."""
    topology = wtypes.wsattr(wtypes.text, mandatory=True)
    role = wtypes.wsattr(wtypes.text)
    ha_ip = wtypes.wsattr(base.IPAddressType())
    secret = wtypes.wsattr(wtypes.text)
