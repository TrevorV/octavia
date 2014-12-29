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

"""
This is an API handler which is meant to simulate successful amphora
control operations. It's meant to be used for testing the amphora API in
situations where we aren't actually running on an amphora and therefore can't
really do things like topology changes, network device discover, etc.
"""

from amphora_api.v1.handlers import abstract_handler

class SimulatedBackendHandler(abstract_handler.BaseHandler):
    """
    Handler that simulates actions that would be done on a
    real amphora if we were running on one.
    """
    #TODO(sbalukoff): Implement this. :)
    pass
