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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import EventGridClientConfiguration
from .operations import EventGridClientOperationsMixin
from msrest.exceptions import HttpOperationError
from . import models


class EventGridClient(EventGridClientOperationsMixin, SDKClient):
    """EventGrid Client

    :ivar config: Configuration for client.
    :vartype config: EventGridClientConfiguration

    :param credentials: Subscription credentials which uniquely identify
     client subscription.
    :type credentials: None
    """

    def __init__(
            self, credentials):

        self.config = EventGridClientConfiguration(credentials)
        super(EventGridClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-01-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
