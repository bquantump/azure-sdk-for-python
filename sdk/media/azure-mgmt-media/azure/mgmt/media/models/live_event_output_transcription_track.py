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


class LiveEventOutputTranscriptionTrack(Model):
    """Describes a transcription track in the output of a Live Event, generated
    using speech-to-text transcription.

    All required parameters must be populated in order to send to Azure.

    :param track_name: Required. The output track name.
    :type track_name: str
    """

    _validation = {
        'track_name': {'required': True},
    }

    _attribute_map = {
        'track_name': {'key': 'trackName', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(LiveEventOutputTranscriptionTrack, self).__init__(**kwargs)
        self.track_name = kwargs.get('track_name', None)
