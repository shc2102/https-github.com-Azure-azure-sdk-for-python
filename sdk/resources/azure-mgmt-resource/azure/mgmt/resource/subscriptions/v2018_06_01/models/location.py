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

from msrest.serialization import Model


class Location(Model):
    """Location information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The fully qualified ID of the location. For example,
     /subscriptions/00000000-0000-0000-0000-000000000000/locations/westus.
    :vartype id: str
    :ivar subscription_id: The subscription ID.
    :vartype subscription_id: str
    :ivar name: The location name.
    :vartype name: str
    :ivar display_name: The display name of the location.
    :vartype display_name: str
    :ivar latitude: The latitude of the location.
    :vartype latitude: str
    :ivar longitude: The longitude of the location.
    :vartype longitude: str
    """

    _validation = {
        'id': {'readonly': True},
        'subscription_id': {'readonly': True},
        'name': {'readonly': True},
        'display_name': {'readonly': True},
        'latitude': {'readonly': True},
        'longitude': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'str'},
        'longitude': {'key': 'longitude', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Location, self).__init__(**kwargs)
        self.id = None
        self.subscription_id = None
        self.name = None
        self.display_name = None
        self.latitude = None
        self.longitude = None