# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API.  This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from admin_api.models.account_group_roles import AccountGroupRoles

class TestAccountGroupRoles(unittest.TestCase):
    """AccountGroupRoles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccountGroupRoles:
        """Test AccountGroupRoles
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccountGroupRoles`
        """
        model = AccountGroupRoles()
        if include_optional:
            return AccountGroupRoles(
                account_group_roles = [
                    admin_api.models.account_group_roles_account_group_roles_inner.AccountGroupRoles_accountGroupRoles_inner(
                        account_group = admin_api.models.account_group_1.AccountGroup_1(), 
                        roles = [
                            admin_api.models.role.Role()
                            ], )
                    ]
            )
        else:
            return AccountGroupRoles(
        )
        """

    def testAccountGroupRoles(self):
        """Test AccountGroupRoles"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
