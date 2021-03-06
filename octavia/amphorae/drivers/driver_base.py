# Copyright 2011-2014 OpenStack Foundation,author: Min Wang,German Eichberger
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
# License for the specific language governing permissions and limitations
# under the License.

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class AmphoraLoadBalancerDriver(object):
    @abc.abstractmethod
    def get_logger(self):
        """Return the logger to use.

        This is a way to inject a custom logger for testing,etc.
        :returns: the logger
        """
        pass

    @abc.abstractmethod
    def update(self, listener, vip):
        """Update the amphora with a new configuration

        :param listener: listener object,
        need to use its protocol_port property
        :type listener: object
        :param vip: vip object, need to use its ip_address property
        :type vip: object
        :returns: return a value list (listener, vip, status flag--update)

        At this moment, we just build the basic structure for testing, will
        add more function along with the development
        """
        pass

    @abc.abstractmethod
    def disable(self, listener, vip):
        """Suspend the running amphora --optional

        :param listener: listener object,
        need to use its protocol_port property
        :type listener: object
        :param vip: vip object, need to use its ip_address property
        :type vip: object
        :returns: return a value list (listener, vip, status flag--suspend)

        At this moment, we just build the basic structure for testing, will
        add more function along with the development
        """
        pass

    @abc.abstractmethod
    def enable(self, listener, vip):
        """Start/enable the listener

        :param listener: listener object,
        need to use its protocol_port property
        :type listener: object
        :param vip : vip object, need to use its ip_address property
        :type vip: object
        :returns: return a value list (listener, vip, status flag--enable)

        At this moment, we just build the basic structure for testing, will
        add more function along with the development
        """
        pass

    @abc.abstractmethod
    def delete(self, listener, vip):
        """Delete the listener from the amphora

        :param listener: listener object,
        need to use its protocol_port property
        :type listener: object
        :param vip: vip object, need to use its ip_address property
        :type vip: object
        :returns: return a value list (listener, vip, status flag--delete)

        At this moment, we just build the basic structure for testing, will
        add more function along with the development
        """
        pass

    @abc.abstractmethod
    def info(self, amphora):
        """Returns information about the amphora

        :param amphora: amphora object, need to use its id property
        :type amphora: object
        :returns: return a value list (amphora.id, status flag--'info')

        At this moment, we just build the basic structure for testing, will
        add more function along with the development, eventually, we want it
        to return information as:
        {"Rest Interface": "1.0", "Amphorae": "1.0",
        "packages":{"ha proxy":"1.5"}}
        some information might come from querying the amphora
        """
        pass

    @abc.abstractmethod
    def get_metrics(self, amphora):
        """Return ceilometer ready metrics

        Some amphora might choose to send them straight to ceilometer others
        might use the mixin support metrics to be compatible with Neutron LBaaS

        :param amphora: amphora object, need to use its id property
        :type amphora: object
        :returns: return a value list (amphora.id, status flag--'get_metrics')

        At this moment, we just build the basic structure for testing, will
        add more function along with the development, eventually, we want it
        to return information as:
        {"Rest Interface": "1.0", "Amphorae": "1.0",
        "packages":{"ha proxy":"1.5"}}
        some information might come from querying the amphora
        """
        pass

    @abc.abstractmethod
    def get_health(self, amphora):
        """Return ceilometer ready health

        :param amphora: amphora object, need to use its id property
        :type amphora: object
        :returns: return a value list (amphora.id, status flag--'get_health')

        At this moment, we just build the basic structure for testing, will
        add more function along with the development, eventually, we want it
        to return information as:
        returns map: {"amphora-status":HEALTHY,
        loadbalancers: {"loadbalancer-id": {"loadbalancer-status": HEALTHY,
        "listeners":{"listener-id":{"listener-status":HEALTHY,
        "nodes":{"node-id":HEALTHY, ...}}, ...}, ...}}
        """
        pass

    @abc.abstractmethod
    def get_diagnostics(self, amphora):
        """Return ceilometer ready health

        :param amphora: amphora object, need to use its id property
        :type amphora: object
        :returns: return a value list (amphora.id, status flag--'ge
        t_diagnostics')

        At this moment, we just build the basic structure for testing, will
        add more function along with the development, eventually, we want it
        run some expensive self tests to determine if the amphora and the lbs
        are healthy the idea is that those tests are triggered more infrequent
        than the health gathering
        """
        pass


@six.add_metaclass(abc.ABCMeta)
class HealthMixin(object):
    @abc.abstractmethod
    def update_health(self, health):
        """Return ceilometer ready health

        :param health: health information emitted from the amphora
        :type health: bool
        :returns: return health

        At this moment, we just build the basic structure for testing, will
        add more function along with the development, eventually, we want it
        return:
        map: {"amphora-status":HEALTHY, loadbalancers: {"loadbalancer-id":
        {"loadbalancer-status": HEALTHY,
        "listeners":{"listener-id":{"listener-status":HEALTHY,
        "nodes":{"node-id":HEALTHY, ...}}, ...}, ...}}
        only items whose health has changed need to be submitted
        awesome update code
        """
        pass


@six.add_metaclass(abc.ABCMeta)
class StatsMixin(object):
    @abc.abstractmethod
    def update_stats(self, stats):
        """Return ceilometer ready stats

        :param stats: statistic information emitted from the amphora
        :type stats: string
        :returns: return stats

        At this moment, we just build the basic structure for testing, will
        add more function along with the development, eventually, we want it
        return:
        uses map {"loadbalancer-id":{"listener-id":
        {"bytes-in": 123, "bytes_out":123, "active_connections":123,
        "total_connections", 123}, ...}
        elements are named to keep it extsnsible for future versions
        awesome update code and code to send to ceilometer
        """
        pass