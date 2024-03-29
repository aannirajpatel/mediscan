"""Generated client library for cloudidentity version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.cloudidentity.v1alpha1 import cloudidentity_v1alpha1_messages as messages


class CloudidentityV1alpha1(base_api.BaseApiClient):
  """Generated client library for service cloudidentity version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://cloudidentity.googleapis.com/'

  _PACKAGE = u'cloudidentity'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-identity.groups', u'https://www.googleapis.com/auth/cloud-identity.groups.readonly', u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'CloudidentityV1alpha1'
  _URL_VERSION = u'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new cloudidentity handle."""
    url = url or self.BASE_URL
    super(CloudidentityV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.groups_memberships = self.GroupsMembershipsService(self)
    self.groups = self.GroupsService(self)

  class GroupsMembershipsService(base_api.BaseApiService):
    """Service class for the groups_memberships resource."""

    _NAME = u'groups_memberships'

    def __init__(self, client):
      super(CloudidentityV1alpha1.GroupsMembershipsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Membership.

      Args:
        request: (CloudidentityGroupsMembershipsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships',
        http_method=u'POST',
        method_id=u'cloudidentity.groups.memberships.create',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[],
        relative_path=u'v1alpha1/{+parent}/memberships',
        request_field=u'membership',
        request_type_name=u'CloudidentityGroupsMembershipsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Membership.

      Args:
        request: (CloudidentityGroupsMembershipsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships/{membershipsId}',
        http_method=u'DELETE',
        method_id=u'cloudidentity.groups.memberships.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'CloudidentityGroupsMembershipsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves a Membership.

      Args:
        request: (CloudidentityGroupsMembershipsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Membership) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships/{membershipsId}',
        http_method=u'GET',
        method_id=u'cloudidentity.groups.memberships.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'CloudidentityGroupsMembershipsGetRequest',
        response_type_name=u'Membership',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List Memberships within a Group.

      Args:
        request: (CloudidentityGroupsMembershipsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListMembershipsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships',
        http_method=u'GET',
        method_id=u'cloudidentity.groups.memberships.list',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'pageSize', u'pageToken', u'view'],
        relative_path=u'v1alpha1/{+parent}/memberships',
        request_field='',
        request_type_name=u'CloudidentityGroupsMembershipsListRequest',
        response_type_name=u'ListMembershipsResponse',
        supports_download=False,
    )

    def Lookup(self, request, global_params=None):
      r"""Looks up [resource.
name](https://cloud.google.com/apis/design/resource_names) of a Membership
within a Group by member's EntityKey.

      Args:
        request: (CloudidentityGroupsMembershipsLookupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LookupMembershipNameResponse) The response message.
      """
      config = self.GetMethodConfig('Lookup')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lookup.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships:lookup',
        http_method=u'GET',
        method_id=u'cloudidentity.groups.memberships.lookup',
        ordered_params=[u'parent'],
        path_params=[u'parent'],
        query_params=[u'memberKey_id', u'memberKey_namespace'],
        relative_path=u'v1alpha1/{+parent}/memberships:lookup',
        request_field='',
        request_type_name=u'CloudidentityGroupsMembershipsLookupRequest',
        response_type_name=u'LookupMembershipNameResponse',
        supports_download=False,
    )

    def ModifyMembershipRoles(self, request, global_params=None):
      r"""Modify membership roles.

      Args:
        request: (CloudidentityGroupsMembershipsModifyMembershipRolesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ModifyMembershipRolesResponse) The response message.
      """
      config = self.GetMethodConfig('ModifyMembershipRoles')
      return self._RunMethod(
          config, request, global_params=global_params)

    ModifyMembershipRoles.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships/{membershipsId}:modifyMembershipRoles',
        http_method=u'POST',
        method_id=u'cloudidentity.groups.memberships.modifyMembershipRoles',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}:modifyMembershipRoles',
        request_field=u'modifyMembershipRolesRequest',
        request_type_name=u'CloudidentityGroupsMembershipsModifyMembershipRolesRequest',
        response_type_name=u'ModifyMembershipRolesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Membership.

      Args:
        request: (CloudidentityGroupsMembershipsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}/memberships/{membershipsId}',
        http_method=u'PATCH',
        method_id=u'cloudidentity.groups.memberships.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'membership',
        request_type_name=u'CloudidentityGroupsMembershipsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class GroupsService(base_api.BaseApiService):
    """Service class for the groups resource."""

    _NAME = u'groups'

    def __init__(self, client):
      super(CloudidentityV1alpha1.GroupsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a Group.

      Args:
        request: (CloudidentityGroupsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'cloudidentity.groups.create',
        ordered_params=[],
        path_params=[],
        query_params=[u'initialGroupConfig'],
        relative_path=u'v1alpha1/groups',
        request_field=u'group',
        request_type_name=u'CloudidentityGroupsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a Group.

      Args:
        request: (CloudidentityGroupsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}',
        http_method=u'DELETE',
        method_id=u'cloudidentity.groups.delete',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'CloudidentityGroupsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Retrieves a Group.

      Args:
        request: (CloudidentityGroupsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Group) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}',
        http_method=u'GET',
        method_id=u'cloudidentity.groups.get',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[],
        relative_path=u'v1alpha1/{+name}',
        request_field='',
        request_type_name=u'CloudidentityGroupsGetRequest',
        response_type_name=u'Group',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List groups within a customer or a domain.

      Args:
        request: (CloudidentityGroupsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListGroupsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudidentity.groups.list',
        ordered_params=[],
        path_params=[],
        query_params=[u'pageSize', u'pageToken', u'parent', u'view'],
        relative_path=u'v1alpha1/groups',
        request_field='',
        request_type_name=u'CloudidentityGroupsListRequest',
        response_type_name=u'ListGroupsResponse',
        supports_download=False,
    )

    def Lookup(self, request, global_params=None):
      r"""Looks up [resource.
name](https://cloud.google.com/apis/design/resource_names) of a Group by
its EntityKey.

      Args:
        request: (CloudidentityGroupsLookupRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (LookupGroupNameResponse) The response message.
      """
      config = self.GetMethodConfig('Lookup')
      return self._RunMethod(
          config, request, global_params=global_params)

    Lookup.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudidentity.groups.lookup',
        ordered_params=[],
        path_params=[],
        query_params=[u'groupKey_id', u'groupKey_namespace'],
        relative_path=u'v1alpha1/groups:lookup',
        request_field='',
        request_type_name=u'CloudidentityGroupsLookupRequest',
        response_type_name=u'LookupGroupNameResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Group.

      Args:
        request: (CloudidentityGroupsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path=u'v1alpha1/groups/{groupsId}',
        http_method=u'PATCH',
        method_id=u'cloudidentity.groups.patch',
        ordered_params=[u'name'],
        path_params=[u'name'],
        query_params=[u'updateMask'],
        relative_path=u'v1alpha1/{+name}',
        request_field=u'group',
        request_type_name=u'CloudidentityGroupsPatchRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Search(self, request, global_params=None):
      r"""Searches for Groups.

      Args:
        request: (CloudidentityGroupsSearchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SearchGroupsResponse) The response message.
      """
      config = self.GetMethodConfig('Search')
      return self._RunMethod(
          config, request, global_params=global_params)

    Search.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'cloudidentity.groups.search',
        ordered_params=[],
        path_params=[],
        query_params=[u'pageSize', u'pageToken', u'query', u'view'],
        relative_path=u'v1alpha1/groups:search',
        request_field='',
        request_type_name=u'CloudidentityGroupsSearchRequest',
        response_type_name=u'SearchGroupsResponse',
        supports_download=False,
    )
