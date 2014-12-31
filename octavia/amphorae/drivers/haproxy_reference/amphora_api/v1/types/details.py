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

from amphora_api.v1.types import base
from wsme import types as wtypes


class DetailResponse(base.BaseType):
    """Defines which attributes should be shown in any response."""
    hostname = wtypes.wsattr(wtypes.text)
    uuid = wtypes.wsattr(wtypes.UuidType())
    version = wtypes.wsattr(wtypes.text)
    api_version = wtypes.wsattr(wtypes.text)
    network_tx = wtypes.wsattr(wtypes.IntegerType())
    network_rx = wtypes.wsattr(wtypes.IntegerType())
    active = wtypes.wsattr(bool)
    haproxy_count = wtypes.wsattr(wtypes.IntegerType())
    # TODO(sbalukoff): Fill out rest of detail response attributes
