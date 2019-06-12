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


class PasswordManagementSettings(Model):
    """The password management settings.

    :param enabled: Indicates if the password extension is enabled.
    :type enabled: bool
    :param extension_file_path: The file path of the password management
     extension.
    :type extension_file_path: str
    :param connect_to: Connection point of password management.
    :type connect_to: str
    :param connection_timeout: Connection timeout for password extension.
    :type connection_timeout: int
    :param user: User to execute password extension.
    :type user: str
    :param supported_password_operations: The supported password operations.
     Possible values include: 'Undefined', 'Set', 'Change'
    :type supported_password_operations: str or
     ~azure.mgmt.adhybridhealthservice.models.PasswordOperationTypes
    :param maximum_retry_count: The maximum number of retries.
    :type maximum_retry_count: int
    :param retry_interval_in_seconds: The time between retries.
    :type retry_interval_in_seconds: int
    :param requires_secure_connection: Indicates if a secure connection is
     required for password management.
    :type requires_secure_connection: bool
    :param unlock_account: Indicates if accounts should be unlocked when
     resetting password.
    :type unlock_account: bool
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'extension_file_path': {'key': 'extensionFilePath', 'type': 'str'},
        'connect_to': {'key': 'connectTo', 'type': 'str'},
        'connection_timeout': {'key': 'connectionTimeout', 'type': 'int'},
        'user': {'key': 'user', 'type': 'str'},
        'supported_password_operations': {'key': 'supportedPasswordOperations', 'type': 'str'},
        'maximum_retry_count': {'key': 'maximumRetryCount', 'type': 'int'},
        'retry_interval_in_seconds': {'key': 'retryIntervalInSeconds', 'type': 'int'},
        'requires_secure_connection': {'key': 'requiresSecureConnection', 'type': 'bool'},
        'unlock_account': {'key': 'unlockAccount', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(PasswordManagementSettings, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.extension_file_path = kwargs.get('extension_file_path', None)
        self.connect_to = kwargs.get('connect_to', None)
        self.connection_timeout = kwargs.get('connection_timeout', None)
        self.user = kwargs.get('user', None)
        self.supported_password_operations = kwargs.get('supported_password_operations', None)
        self.maximum_retry_count = kwargs.get('maximum_retry_count', None)
        self.retry_interval_in_seconds = kwargs.get('retry_interval_in_seconds', None)
        self.requires_secure_connection = kwargs.get('requires_secure_connection', None)
        self.unlock_account = kwargs.get('unlock_account', None)
