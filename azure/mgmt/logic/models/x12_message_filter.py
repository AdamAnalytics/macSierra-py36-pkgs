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


class X12MessageFilter(Model):
    """The X12 message filter for odata query.

    :param message_filter_type: The message filter type. Possible values
     include: 'NotSpecified', 'Include', 'Exclude'
    :type message_filter_type: str or :class:`MessageFilterType
     <azure.mgmt.logic.models.MessageFilterType>`
    """

    _validation = {
        'message_filter_type': {'required': True},
    }

    _attribute_map = {
        'message_filter_type': {'key': 'messageFilterType', 'type': 'MessageFilterType'},
    }

    def __init__(self, message_filter_type):
        self.message_filter_type = message_filter_type