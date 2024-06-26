# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Describe command for the Label Manager - Label Keys CLI."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.labelmanager import service as labelmanager
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.labelmanager import arguments


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class List(base.ListCommand):
  r"""Lists label keys under the specified parent resource.

  ## EXAMPLES

  To list all the label keys under an organization run:

        $ gcloud alpha labelmanager keys list 'organizations/123'
  """

  @staticmethod
  def Args(parser):
    arguments.AddLabelParentArgToParser(parser)
    parser.display_info.AddFormat('table(name:sort=1, displayName)')

  def Run(self, args):
    labelkeys_service = labelmanager.LabelKeysService()
    labelmanager_messages = labelmanager.LabelManagerMessages()

    label_parent = args.label_parent

    list_request = labelmanager_messages.LabelmanagerLabelKeysListRequest(
        parent=label_parent)
    response = labelkeys_service.List(list_request)
    return response.keys
