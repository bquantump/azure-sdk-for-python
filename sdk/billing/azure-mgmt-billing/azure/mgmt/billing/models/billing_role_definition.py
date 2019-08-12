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

from .resource import Resource


class BillingRoleDefinition(Resource):
    """Result of get role definition for a role.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar description: The role description
    :vartype description: str
    :ivar value: The list of billingPermissions a caller has on a billing
     account.
    :vartype value:
     list[~azure.mgmt.billing.models.BillingPermissionsProperties]
    :ivar role_name: The name of the role
    :vartype role_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'description': {'readonly': True},
        'value': {'readonly': True},
        'role_name': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'value': {'key': 'properties.permissions.value', 'type': '[BillingPermissionsProperties]'},
        'role_name': {'key': 'properties.roleName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BillingRoleDefinition, self).__init__(**kwargs)
        self.description = None
        self.value = None
        self.role_name = None