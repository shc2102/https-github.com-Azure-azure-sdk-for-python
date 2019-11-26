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

from ._configuration import SubscriptionClientConfiguration
from .operations import SubscriptionsOperations
from . import models


class SubscriptionClient(SDKClient):
    """Subscription client provides an interface to create and manage Azure subscriptions programmatically.

    :ivar config: Configuration for client.
    :vartype config: SubscriptionClientConfiguration

    :ivar subscriptions: Subscriptions operations
    :vartype subscriptions: azure.mgmt.subscription.operations.SubscriptionsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = SubscriptionClientConfiguration(credentials, base_url)
        super(SubscriptionClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-10-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.subscriptions = SubscriptionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
