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

from .resource_py3 import Resource


class ActionResponse(Resource):
    """Action for alert rule.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource Id
    :vartype id: str
    :ivar name: Azure resource name
    :vartype name: str
    :ivar type: Azure resource type
    :vartype type: str
    :param etag: Etag of the action.
    :type etag: str
    :param workflow_id: The name of the logic app's workflow.
    :type workflow_id: str
    :param logic_app_resource_id: The logic app's resource id.
    :type logic_app_resource_id: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
        'workflow_id': {'key': 'properties.workflowId', 'type': 'str'},
        'logic_app_resource_id': {'key': 'properties.logicAppResourceId', 'type': 'str'},
    }

    def __init__(self, *, etag: str=None, workflow_id: str=None, logic_app_resource_id: str=None, **kwargs) -> None:
        super(ActionResponse, self).__init__(**kwargs)
        self.etag = etag
        self.workflow_id = workflow_id
        self.logic_app_resource_id = logic_app_resource_id
