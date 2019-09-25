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

from .data_connectors_check_requirements_py3 import DataConnectorsCheckRequirements


class ASCCheckRequirements(DataConnectorsCheckRequirements):
    """ASC (Azure Security Center) requirements check properties.

    :param kind: The kind of the data connector. Possible values include:
     'AzureActiveDirectory', 'AzureSecurityCenter',
     'MicrosoftCloudAppSecurity', 'ThreatIntelligence', 'Office365',
     'AmazonWebServicesCloudTrail', 'AzureAdvancedThreatProtection',
     'MicrosoftDefenderAdvancedThreatProtection'
    :type kind: str or ~azure.mgmt.securityinsight.models.DataConnectorKind
    :param subscription_id: The subscription id to connect to, and get the
     data from.
    :type subscription_id: str
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
    }

    def __init__(self, *, kind=None, subscription_id: str=None, **kwargs) -> None:
        super(ASCCheckRequirements, self).__init__(kind=kind, **kwargs)
        self.subscription_id = subscription_id
