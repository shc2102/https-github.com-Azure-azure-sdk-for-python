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

from .rule_condition_py3 import RuleCondition


class LocationThresholdRuleCondition(RuleCondition):
    """A rule condition based on a certain number of locations failing.

    All required parameters must be populated in order to send to Azure.

    :param data_source: the resource from which the rule collects its data.
     For this type dataSource will always be of type RuleMetricDataSource.
    :type data_source: ~azure.mgmt.monitor.models.RuleDataSource
    :param odatatype: Required. Constant filled by server.
    :type odatatype: str
    :param window_size: the period of time (in ISO 8601 duration format) that
     is used to monitor alert activity based on the threshold. If specified
     then it must be between 5 minutes and 1 day.
    :type window_size: timedelta
    :param failed_location_count: Required. the number of locations that must
     fail to activate the alert.
    :type failed_location_count: int
    """

    _validation = {
        'odatatype': {'required': True},
        'failed_location_count': {'required': True, 'minimum': 0},
    }

    _attribute_map = {
        'data_source': {'key': 'dataSource', 'type': 'RuleDataSource'},
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'window_size': {'key': 'windowSize', 'type': 'duration'},
        'failed_location_count': {'key': 'failedLocationCount', 'type': 'int'},
    }

    def __init__(self, *, failed_location_count: int, data_source=None, window_size=None, **kwargs) -> None:
        super(LocationThresholdRuleCondition, self).__init__(data_source=data_source, **kwargs)
        self.window_size = window_size
        self.failed_location_count = failed_location_count
        self.odatatype = 'Microsoft.Azure.Management.Insights.Models.LocationThresholdRuleCondition'