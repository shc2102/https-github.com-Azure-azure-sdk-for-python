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


class Tenant(Model):
    """The details of the onboarded tenant.

    :param tenant_id: The Id of the tenant.
    :type tenant_id: str
    :param aad_license: The Azure Active Directory license of the tenant.
    :type aad_license: str
    :param aad_premium: Indicate if the tenant has Azure Active Directory
     Premium license or not.
    :type aad_premium: bool
    :param agent_auto_update: Indicates if the tenant is configured to
     automatically receive updates for Azure Active Directory Connect Health
     client side features.
    :type agent_auto_update: bool
    :param alert_suppression_time_in_mins: The time in minutes after which an
     alert will be auto-suppressed.
    :type alert_suppression_time_in_mins: int
    :param consented_to_microsoft_dev_ops: Indicates if the tenant data can be
     seen by Microsoft through Azure portal.
    :type consented_to_microsoft_dev_ops: bool
    :param country_letter_code: The country letter code of the tenant.
    :type country_letter_code: str
    :param created_date: The date, in UTC, when the tenant was onboarded to
     Azure Active Directory Connect Health.
    :type created_date: datetime
    :param dev_ops_ttl: The date and time, in UTC, till when the tenant data
     can be seen by Microsoft through Azure portal.
    :type dev_ops_ttl: datetime
    :param disabled: Indicates if the tenant is disabled in Azure Active
     Directory Connect Health.
    :type disabled: bool
    :param disabled_reason: The reason due to which the tenant was disabled in
     Azure Active Directory Connect Health.
    :type disabled_reason: int
    :param global_admins_email: The list of global administrators for the
     tenant.
    :type global_admins_email: list[str]
    :param initial_domain: The initial domain of the tenant.
    :type initial_domain: str
    :param last_disabled: The date and time, in UTC, when the tenant was last
     disabled in Azure Active Directory Connect Health.
    :type last_disabled: datetime
    :param last_verified: The date and time, in UTC, when the tenant
     onboarding status in Azure Active Directory Connect Health was last
     verified.
    :type last_verified: datetime
    :param onboarding_allowed: Indicates if the tenant is allowed to  onboard
     to Azure Active Directory Connect Health.
    :type onboarding_allowed: bool
    :param onboarded: Indicates if the tenant is already onboarded to Azure
     Active Directory Connect Health.
    :type onboarded: bool
    :param pks_certificate: The certificate associated with the tenant to
     onboard data to Azure Active Directory Connect Health.
    :type pks_certificate: object
    :param private_preview_tenant: Indicates if the tenant has signed up for
     private preview of Azure Active Directory Connect Health features.
    :type private_preview_tenant: bool
    :param tenant_in_quarantine: Indicates if data collection for this tenant
     is disabled or not.
    :type tenant_in_quarantine: bool
    :param tenant_name: The name of the tenant.
    :type tenant_name: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'aad_license': {'key': 'aadLicense', 'type': 'str'},
        'aad_premium': {'key': 'aadPremium', 'type': 'bool'},
        'agent_auto_update': {'key': 'agentAutoUpdate', 'type': 'bool'},
        'alert_suppression_time_in_mins': {'key': 'alertSuppressionTimeInMins', 'type': 'int'},
        'consented_to_microsoft_dev_ops': {'key': 'consentedToMicrosoftDevOps', 'type': 'bool'},
        'country_letter_code': {'key': 'countryLetterCode', 'type': 'str'},
        'created_date': {'key': 'createdDate', 'type': 'iso-8601'},
        'dev_ops_ttl': {'key': 'devOpsTtl', 'type': 'iso-8601'},
        'disabled': {'key': 'disabled', 'type': 'bool'},
        'disabled_reason': {'key': 'disabledReason', 'type': 'int'},
        'global_admins_email': {'key': 'globalAdminsEmail', 'type': '[str]'},
        'initial_domain': {'key': 'initialDomain', 'type': 'str'},
        'last_disabled': {'key': 'lastDisabled', 'type': 'iso-8601'},
        'last_verified': {'key': 'lastVerified', 'type': 'iso-8601'},
        'onboarding_allowed': {'key': 'onboardingAllowed', 'type': 'bool'},
        'onboarded': {'key': 'onboarded', 'type': 'bool'},
        'pks_certificate': {'key': 'pksCertificate', 'type': 'object'},
        'private_preview_tenant': {'key': 'privatePreviewTenant', 'type': 'bool'},
        'tenant_in_quarantine': {'key': 'tenantInQuarantine', 'type': 'bool'},
        'tenant_name': {'key': 'tenantName', 'type': 'str'},
    }

    def __init__(self, *, tenant_id: str=None, aad_license: str=None, aad_premium: bool=None, agent_auto_update: bool=None, alert_suppression_time_in_mins: int=None, consented_to_microsoft_dev_ops: bool=None, country_letter_code: str=None, created_date=None, dev_ops_ttl=None, disabled: bool=None, disabled_reason: int=None, global_admins_email=None, initial_domain: str=None, last_disabled=None, last_verified=None, onboarding_allowed: bool=None, onboarded: bool=None, pks_certificate=None, private_preview_tenant: bool=None, tenant_in_quarantine: bool=None, tenant_name: str=None, **kwargs) -> None:
        super(Tenant, self).__init__(**kwargs)
        self.tenant_id = tenant_id
        self.aad_license = aad_license
        self.aad_premium = aad_premium
        self.agent_auto_update = agent_auto_update
        self.alert_suppression_time_in_mins = alert_suppression_time_in_mins
        self.consented_to_microsoft_dev_ops = consented_to_microsoft_dev_ops
        self.country_letter_code = country_letter_code
        self.created_date = created_date
        self.dev_ops_ttl = dev_ops_ttl
        self.disabled = disabled
        self.disabled_reason = disabled_reason
        self.global_admins_email = global_admins_email
        self.initial_domain = initial_domain
        self.last_disabled = last_disabled
        self.last_verified = last_verified
        self.onboarding_allowed = onboarding_allowed
        self.onboarded = onboarded
        self.pks_certificate = pks_certificate
        self.private_preview_tenant = private_preview_tenant
        self.tenant_in_quarantine = tenant_in_quarantine
        self.tenant_name = tenant_name
