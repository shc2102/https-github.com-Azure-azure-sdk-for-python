# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .entity import Entity


class HostEntity(Entity):
    """Represents a host entity.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar type: Azure resource type
    :vartype type: str
    :ivar name: Azure resource name
    :vartype name: str
    :param kind: Required. Constant filled by server.
    :type kind: str
    :ivar dns_domain: The DNS domain that this host belongs to. Should contain
     the compete DNS suffix for the domain
    :vartype dns_domain: str
    :ivar nt_domain: The NT domain that this host belongs to.
    :vartype nt_domain: str
    :ivar host_name: The hostname without the domain suffix.
    :vartype host_name: str
    :ivar net_bios_name: The host name (pre-windows2000).
    :vartype net_bios_name: str
    :ivar azure_id: The azure resource id of the VM.
    :vartype azure_id: str
    :ivar oms_agent_id: The OMS agent id, if the host has OMS agent installed.
    :vartype oms_agent_id: str
    :param os_family: The operating system type. Possible values include:
     'Linux', 'Windows', 'Android', 'IOS'
    :type os_family: str or ~azure.mgmt.securityinsight.models.OSFamily
    :ivar os_version: A free text representation of the operating system. This
     field is meant to hold specific versions the are more fine grained than
     OSFamily or future values not supported by OSFamily enumeration
    :vartype os_version: str
    :ivar is_domain_joined: Determines whether this host belongs to a domain.
    :vartype is_domain_joined: bool
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'kind': {'required': True},
        'dns_domain': {'readonly': True},
        'nt_domain': {'readonly': True},
        'host_name': {'readonly': True},
        'net_bios_name': {'readonly': True},
        'azure_id': {'readonly': True},
        'oms_agent_id': {'readonly': True},
        'os_version': {'readonly': True},
        'is_domain_joined': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'dns_domain': {'key': 'properties.dnsDomain', 'type': 'str'},
        'nt_domain': {'key': 'properties.ntDomain', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'net_bios_name': {'key': 'properties.netBiosName', 'type': 'str'},
        'azure_id': {'key': 'properties.azureID', 'type': 'str'},
        'oms_agent_id': {'key': 'properties.omsAgentID', 'type': 'str'},
        'os_family': {'key': 'properties.osFamily', 'type': 'OSFamily'},
        'os_version': {'key': 'properties.osVersion', 'type': 'str'},
        'is_domain_joined': {'key': 'properties.isDomainJoined', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(HostEntity, self).__init__(**kwargs)
        self.dns_domain = None
        self.nt_domain = None
        self.host_name = None
        self.net_bios_name = None
        self.azure_id = None
        self.oms_agent_id = None
        self.os_family = kwargs.get('os_family', None)
        self.os_version = None
        self.is_domain_joined = None
        self.kind = 'Host'
