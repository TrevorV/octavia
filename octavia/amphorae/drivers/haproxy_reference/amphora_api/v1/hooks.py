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

import uuid

from pecan import hooks


class SimpleContext(object):
    """Simple Context class

    Very simple helper class for storing some request context data
    that wouldn't end up in a standard OpenStack RequestContext, and
    skipping attributes we don't care about.
    """

    def generate_request_id():
        return b'req-' + str(uuid.uuid4()).encode('ascii')

    def __init__(self, controller_id=None, request_id=None):
        self.controller_id = controller_id
        if not request_id:
            request_id = self.generate_request_id
        self.request_id = request_id

    def to_dict(self):
        return {
            'controller_id': self.controller_id,
            'request_id': self.request_id}

    @classmethod
    def from_dict(cls, ctx):
        return cls(
            controller_id=ctx.get("controller_id"),
            request_id=ctx.get("request_id"))


class ContextHook(hooks.PecanHook):
    def on_route(self, state):

        controller_id = None

        # TODO(sbalukoff): We only care about the controller's ID, which
        # the webserver should extract from its TLS certificate
        # Beyond that we don't care about anything else in the
        # request context. This will look something like the following
        # (note that we may have to parse the Subject DN further to get
        # just a UUID out of it):
        # if state.request.environ.get('SSL_CLIENT_VERIFY') = 'SUCCESS'
        #    controller_id = state.request.environ.get('SSL_CLIENT_S_DN')

        # TODO(sbalukoff): Once we are doing TLS verification of
        # the controller's client cert, we should disallow / abort
        # the request if we don't verify or don't get a controller_id
        # if not controller_id:
        #     authentication_error

        state.request.context = SimpleContext(controller_id=controller_id)
