# Copyright 2014 Rackspace
# All Rights Reserved.
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

from webob import exc


def check_exception(status_code):
    if status_code is 401:
        return Unauthorized()
    if status_code is 403:
        return InvalidRequest()
    if status_code is 404:
        return NotFound()
    if status_code is 409:
        return Conflict()
    if status_code is 500:
        return InternalServerError()
    if status_code is 503:
        return ServiceUnavailable()
    return status_code


class APIException(exc.HTTPClientError):
    msg = "Something unknown went wrong"
    code = 500

    def __init__(self, **kwargs):
        self.msg = self.msg % kwargs
        super(APIException, self).__init__(detail=self.msg)


class Unauthorized(APIException):
    msg = "Unauthorized"
    code = 401


class InvalidRequest(APIException):
    msg = "Invalid request"
    code = 403


class NotFound(APIException):
    msg = "Not Found"
    code = 404


class Conflict(APIException):
    msg = "Conflict"
    code = 409


class InternalServerError(APIException):
    msg = "Internal Server Error"
    code = 500


class ServiceUnavailable(APIException):
    msg = "Service Unavailable"
    code = 503