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


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class Dimension(Model):
    """Specifications of the Dimension of metrics.

    :param name: The public facing name of the dimension.
    :type name: str
    :param display_name: Localized friendly display name of the dimension.
    :type display_name: str
    :param internal_name: Name of the dimension as it appears in MDM.
    :type internal_name: str
    :param to_be_exported_for_shoebox: A Boolean flag indicating whether this
     dimension should be included for the shoebox export scenario.
    :type to_be_exported_for_shoebox: bool
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'internal_name': {'key': 'internalName', 'type': 'str'},
        'to_be_exported_for_shoebox': {'key': 'toBeExportedForShoebox', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(Dimension, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.internal_name = kwargs.get('internal_name', None)
        self.to_be_exported_for_shoebox = kwargs.get('to_be_exported_for_shoebox', None)


class MetricSpecification(Model):
    """Specifications of the Metrics for Azure Monitoring.

    :param name: Name of the metric.
    :type name: str
    :param display_name: Localized friendly display name of the metric.
    :type display_name: str
    :param display_description: Localized friendly description of the metric.
    :type display_description: str
    :param unit: The unit that makes sense for the metric.
    :type unit: str
    :param aggregation_type: Only provide one value for this field. Valid
     values: Average, Minimum, Maximum, Total, Count.
    :type aggregation_type: str
    :param fill_gap_with_zero: Optional. If set to true, then zero will be
     returned for time duration where no metric is emitted/published.
     Ex. a metric that returns the number of times a particular error code was
     emitted. The error code may not appear
     often, instead of the RP publishing 0, Shoebox can auto fill in 0s for
     time periods where nothing was emitted.
    :type fill_gap_with_zero: str
    :param category: The name of the metric category that the metric belongs
     to. A metric can only belong to a single category.
    :type category: str
    :param dimensions: The dimensions of the metrics.
    :type dimensions: list[~azure.mgmt.signalr.models.Dimension]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'display_description': {'key': 'displayDescription', 'type': 'str'},
        'unit': {'key': 'unit', 'type': 'str'},
        'aggregation_type': {'key': 'aggregationType', 'type': 'str'},
        'fill_gap_with_zero': {'key': 'fillGapWithZero', 'type': 'str'},
        'category': {'key': 'category', 'type': 'str'},
        'dimensions': {'key': 'dimensions', 'type': '[Dimension]'},
    }

    def __init__(self, **kwargs):
        super(MetricSpecification, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display_name = kwargs.get('display_name', None)
        self.display_description = kwargs.get('display_description', None)
        self.unit = kwargs.get('unit', None)
        self.aggregation_type = kwargs.get('aggregation_type', None)
        self.fill_gap_with_zero = kwargs.get('fill_gap_with_zero', None)
        self.category = kwargs.get('category', None)
        self.dimensions = kwargs.get('dimensions', None)


class NameAvailability(Model):
    """Result of the request to check name availability. It contains a flag and
    possible reason of failure.

    :param name_available: Indicates whether the name is available or not.
    :type name_available: bool
    :param reason: The reason of the availability. Required if name is not
     available.
    :type reason: str
    :param message: The message of the operation.
    :type message: str
    """

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NameAvailability, self).__init__(**kwargs)
        self.name_available = kwargs.get('name_available', None)
        self.reason = kwargs.get('reason', None)
        self.message = kwargs.get('message', None)


class NameAvailabilityParameters(Model):
    """Data POST-ed to the nameAvailability action.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The resource type. Should be always
     "Microsoft.SignalRService/SignalR".
    :type type: str
    :param name: Required. The SignalR service name to validate.
     e.g."my-signalR-name-here"
    :type name: str
    """

    _validation = {
        'type': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(NameAvailabilityParameters, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.name = kwargs.get('name', None)


class Operation(Model):
    """REST API operation supported by SignalR resource provider.

    :param name: Name of the operation with format:
     {provider}/{resource}/{operation}
    :type name: str
    :param display: The object that describes the operation.
    :type display: ~azure.mgmt.signalr.models.OperationDisplay
    :param origin: Optional. The intended executor of the operation; governs
     the display of the operation in the RBAC UX and the audit logs UX.
    :type origin: str
    :param properties: Extra properties for the operation.
    :type properties: ~azure.mgmt.signalr.models.OperationProperties
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'origin': {'key': 'origin', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'OperationProperties'},
    }

    def __init__(self, **kwargs):
        super(Operation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.display = kwargs.get('display', None)
        self.origin = kwargs.get('origin', None)
        self.properties = kwargs.get('properties', None)


class OperationDisplay(Model):
    """The object that describes a operation.

    :param provider: Friendly name of the resource provider
    :type provider: str
    :param resource: Resource type on which the operation is performed.
    :type resource: str
    :param operation: The localized friendly name for the operation.
    :type operation: str
    :param description: The localized friendly description for the operation
    :type description: str
    """

    _attribute_map = {
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OperationDisplay, self).__init__(**kwargs)
        self.provider = kwargs.get('provider', None)
        self.resource = kwargs.get('resource', None)
        self.operation = kwargs.get('operation', None)
        self.description = kwargs.get('description', None)


class OperationProperties(Model):
    """Extra Operation properties.

    :param service_specification: The service specifications.
    :type service_specification:
     ~azure.mgmt.signalr.models.ServiceSpecification
    """

    _attribute_map = {
        'service_specification': {'key': 'serviceSpecification', 'type': 'ServiceSpecification'},
    }

    def __init__(self, **kwargs):
        super(OperationProperties, self).__init__(**kwargs)
        self.service_specification = kwargs.get('service_specification', None)


class RegenerateKeyParameters(Model):
    """Parameters describes the request to regenerate access keys.

    :param key_type: The keyType to regenerate. Must be either 'primary' or
     'secondary'(case-insensitive). Possible values include: 'Primary',
     'Secondary'
    :type key_type: str or ~azure.mgmt.signalr.models.KeyType
    """

    _attribute_map = {
        'key_type': {'key': 'keyType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RegenerateKeyParameters, self).__init__(**kwargs)
        self.key_type = kwargs.get('key_type', None)


class Resource(Model):
    """The core properties of ARM resources.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g.
     "Microsoft.SignalRService/SignalR"
    :vartype type: str
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
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None


class ResourceSku(Model):
    """The billing information of the SignalR resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the SKU. Required.
     Allowed values: Standard_S1, Free_F1
    :type name: str
    :param tier: Optional tier of this particular SKU. 'Standard' or 'Free'.
     `Basic` is deprecated, use `Standard` instead. Possible values include:
     'Free', 'Basic', 'Standard', 'Premium'
    :type tier: str or ~azure.mgmt.signalr.models.SignalRSkuTier
    :param size: Optional string. For future use.
    :type size: str
    :param family: Optional string. For future use.
    :type family: str
    :param capacity: Optional, integer. The unit count of SignalR resource. 1
     by default.
     If present, following values are allowed:
     Free: 1
     Standard: 1,2,5,10,20,50,100
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ResourceSku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
        self.size = kwargs.get('size', None)
        self.family = kwargs.get('family', None)
        self.capacity = kwargs.get('capacity', None)


class ServiceSpecification(Model):
    """An object that describes a specification.

    :param metric_specifications: Specifications of the Metrics for Azure
     Monitoring.
    :type metric_specifications:
     list[~azure.mgmt.signalr.models.MetricSpecification]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecification]'},
    }

    def __init__(self, **kwargs):
        super(ServiceSpecification, self).__init__(**kwargs)
        self.metric_specifications = kwargs.get('metric_specifications', None)


class SignalRCorsSettings(Model):
    """Cross-Origin Resource Sharing (CORS) settings.

    :param allowed_origins: Gets or sets the list of origins that should be
     allowed to make cross-origin calls (for example:
     http://example.com:12345). Use "*" to allow all. If omitted, allow all by
     default.
    :type allowed_origins: list[str]
    """

    _attribute_map = {
        'allowed_origins': {'key': 'allowedOrigins', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(SignalRCorsSettings, self).__init__(**kwargs)
        self.allowed_origins = kwargs.get('allowed_origins', None)


class SignalRCreateOrUpdateProperties(Model):
    """Settings used to provision or configure the resource.

    :param host_name_prefix: Prefix for the hostName of the SignalR service.
     Retained for future use.
     The hostname will be of format:
     &lt;hostNamePrefix&gt;.service.signalr.net.
    :type host_name_prefix: str
    :param features: List of SignalR featureFlags. e.g. ServiceMode.
     FeatureFlags that are not included in the parameters for the update
     operation will not be modified.
     And the response will only include featureFlags that are explicitly set.
     When a featureFlag is not explicitly set, SignalR service will use its
     globally default value.
     But keep in mind, the default value doesn't mean "false". It varies in
     terms of different FeatureFlags.
    :type features: list[~azure.mgmt.signalr.models.SignalRFeature]
    :param cors: Cross-Origin Resource Sharing (CORS) settings.
    :type cors: ~azure.mgmt.signalr.models.SignalRCorsSettings
    """

    _attribute_map = {
        'host_name_prefix': {'key': 'hostNamePrefix', 'type': 'str'},
        'features': {'key': 'features', 'type': '[SignalRFeature]'},
        'cors': {'key': 'cors', 'type': 'SignalRCorsSettings'},
    }

    def __init__(self, **kwargs):
        super(SignalRCreateOrUpdateProperties, self).__init__(**kwargs)
        self.host_name_prefix = kwargs.get('host_name_prefix', None)
        self.features = kwargs.get('features', None)
        self.cors = kwargs.get('cors', None)


class SignalRUpdateParameters(Model):
    """Parameters for SignalR service update operation.

    :param tags: A list of key value pairs that describe the resource.
    :type tags: dict[str, str]
    :param sku: The billing information of the resource.(e.g. basic vs.
     standard)
    :type sku: ~azure.mgmt.signalr.models.ResourceSku
    :param properties: Settings used to provision or configure the resource
    :type properties:
     ~azure.mgmt.signalr.models.SignalRCreateOrUpdateProperties
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'properties': {'key': 'properties', 'type': 'SignalRCreateOrUpdateProperties'},
    }

    def __init__(self, **kwargs):
        super(SignalRUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.sku = kwargs.get('sku', None)
        self.properties = kwargs.get('properties', None)


class SignalRCreateParameters(SignalRUpdateParameters):
    """Parameters for SignalR service create/update operation.
    Keep the same schema as AzSignalR.Models.SignalRResource.

    All required parameters must be populated in order to send to Azure.

    :param tags: A list of key value pairs that describe the resource.
    :type tags: dict[str, str]
    :param sku: The billing information of the resource.(e.g. basic vs.
     standard)
    :type sku: ~azure.mgmt.signalr.models.ResourceSku
    :param properties: Settings used to provision or configure the resource
    :type properties:
     ~azure.mgmt.signalr.models.SignalRCreateOrUpdateProperties
    :param location: Required. Azure GEO region: e.g. West US | East US |
     North Central US | South Central US | West Europe | North Europe | East
     Asia | Southeast Asia | etc.
     The geo region of a resource never changes after it is created.
    :type location: str
    """

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'properties': {'key': 'properties', 'type': 'SignalRCreateOrUpdateProperties'},
        'location': {'key': 'location', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SignalRCreateParameters, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)


class SignalRFeature(Model):
    """Feature of a SignalR resource, which controls the SignalR runtime behavior.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar flag: Required. Kind of feature. Required. Default value:
     "ServiceMode" .
    :vartype flag: str
    :param value: Required. Value of the feature flag. See Azure SignalR
     service document https://docs.microsoft.com/en-us/azure/azure-signalr/ for
     allowed values.
    :type value: str
    :param properties: Optional properties related to this feature.
    :type properties: dict[str, str]
    """

    _validation = {
        'flag': {'required': True, 'constant': True},
        'value': {'required': True, 'max_length': 128, 'min_length': 1},
    }

    _attribute_map = {
        'flag': {'key': 'flag', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'properties': {'key': 'properties', 'type': '{str}'},
    }

    flag = "ServiceMode"

    def __init__(self, **kwargs):
        super(SignalRFeature, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.properties = kwargs.get('properties', None)


class SignalRKeys(Model):
    """A class represents the access keys of SignalR service.

    :param primary_key: The primary access key.
    :type primary_key: str
    :param secondary_key: The secondary access key.
    :type secondary_key: str
    :param primary_connection_string: SignalR connection string constructed
     via the primaryKey
    :type primary_connection_string: str
    :param secondary_connection_string: SignalR connection string constructed
     via the secondaryKey
    :type secondary_connection_string: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SignalRKeys, self).__init__(**kwargs)
        self.primary_key = kwargs.get('primary_key', None)
        self.secondary_key = kwargs.get('secondary_key', None)
        self.primary_connection_string = kwargs.get('primary_connection_string', None)
        self.secondary_connection_string = kwargs.get('secondary_connection_string', None)


class TrackedResource(Resource):
    """The resource model definition for a ARM tracked top level resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g.
     "Microsoft.SignalRService/SignalR"
    :vartype type: str
    :param location: The GEO location of the SignalR service. e.g. West US |
     East US | North Central US | South Central US.
    :type location: str
    :param tags: Tags of the service which is a list of key value pairs that
     describe the resource.
    :type tags: dict[str, str]
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
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(TrackedResource, self).__init__(**kwargs)
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class SignalRResource(TrackedResource):
    """A class represent a SignalR service resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource Id for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the service - e.g.
     "Microsoft.SignalRService/SignalR"
    :vartype type: str
    :param location: The GEO location of the SignalR service. e.g. West US |
     East US | North Central US | South Central US.
    :type location: str
    :param tags: Tags of the service which is a list of key value pairs that
     describe the resource.
    :type tags: dict[str, str]
    :param sku: SKU of the service.
    :type sku: ~azure.mgmt.signalr.models.ResourceSku
    :param host_name_prefix: Prefix for the hostName of the SignalR service.
     Retained for future use.
     The hostname will be of format:
     &lt;hostNamePrefix&gt;.service.signalr.net.
    :type host_name_prefix: str
    :param features: List of SignalR featureFlags. e.g. ServiceMode.
     FeatureFlags that are not included in the parameters for the update
     operation will not be modified.
     And the response will only include featureFlags that are explicitly set.
     When a featureFlag is not explicitly set, SignalR service will use its
     globally default value.
     But keep in mind, the default value doesn't mean "false". It varies in
     terms of different FeatureFlags.
    :type features: list[~azure.mgmt.signalr.models.SignalRFeature]
    :param cors: Cross-Origin Resource Sharing (CORS) settings.
    :type cors: ~azure.mgmt.signalr.models.SignalRCorsSettings
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Unknown', 'Succeeded', 'Failed', 'Canceled', 'Running',
     'Creating', 'Updating', 'Deleting', 'Moving'
    :vartype provisioning_state: str or
     ~azure.mgmt.signalr.models.ProvisioningState
    :ivar external_ip: The publicly accessible IP of the SignalR service.
    :vartype external_ip: str
    :ivar host_name: FQDN of the SignalR service instance. Format:
     xxx.service.signalr.net
    :vartype host_name: str
    :ivar public_port: The publicly accessible port of the SignalR service
     which is designed for browser/client side usage.
    :vartype public_port: int
    :ivar server_port: The publicly accessible port of the SignalR service
     which is designed for customer server side usage.
    :vartype server_port: int
    :param version: Version of the SignalR resource. Probably you need the
     same or higher version of client SDKs.
    :type version: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'external_ip': {'readonly': True},
        'host_name': {'readonly': True},
        'public_port': {'readonly': True},
        'server_port': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'ResourceSku'},
        'host_name_prefix': {'key': 'properties.hostNamePrefix', 'type': 'str'},
        'features': {'key': 'properties.features', 'type': '[SignalRFeature]'},
        'cors': {'key': 'properties.cors', 'type': 'SignalRCorsSettings'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'external_ip': {'key': 'properties.externalIP', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'public_port': {'key': 'properties.publicPort', 'type': 'int'},
        'server_port': {'key': 'properties.serverPort', 'type': 'int'},
        'version': {'key': 'properties.version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SignalRResource, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.host_name_prefix = kwargs.get('host_name_prefix', None)
        self.features = kwargs.get('features', None)
        self.cors = kwargs.get('cors', None)
        self.provisioning_state = None
        self.external_ip = None
        self.host_name = None
        self.public_port = None
        self.server_port = None
        self.version = kwargs.get('version', None)


class SignalRUsage(Model):
    """Object that describes a specific usage of SignalR resources.

    :param id: Fully qualified ARM resource id
    :type id: str
    :param current_value: Current value for the usage quota.
    :type current_value: long
    :param limit: The maximum permitted value for the usage quota. If there is
     no limit, this value will be -1.
    :type limit: long
    :param name: Localizable String object containing the name and a localized
     value.
    :type name: ~azure.mgmt.signalr.models.SignalRUsageName
    :param unit: Representing the units of the usage quota. Possible values
     are: Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond.
    :type unit: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'current_value': {'key': 'currentValue', 'type': 'long'},
        'limit': {'key': 'limit', 'type': 'long'},
        'name': {'key': 'name', 'type': 'SignalRUsageName'},
        'unit': {'key': 'unit', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SignalRUsage, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.current_value = kwargs.get('current_value', None)
        self.limit = kwargs.get('limit', None)
        self.name = kwargs.get('name', None)
        self.unit = kwargs.get('unit', None)


class SignalRUsageName(Model):
    """Localizable String object containing the name and a localized value.

    :param value: The identifier of the usage.
    :type value: str
    :param localized_value: Localized name of the usage.
    :type localized_value: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'localized_value': {'key': 'localizedValue', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SignalRUsageName, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.localized_value = kwargs.get('localized_value', None)
