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


class TICheckRequirements(Model):
    """TI (Threat Intelligence) requirements check properties.

    :param tenant_id: The tenant id to connect to, and get the data from.
    :type tenant_id: str
    """

    _attribute_map = {
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, *, tenant_id: str=None, **kwargs) -> None:
        super(TICheckRequirements, self).__init__(**kwargs)
        self.tenant_id = tenant_id
