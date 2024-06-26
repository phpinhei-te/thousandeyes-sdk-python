# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.usage.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.usage.api.quotas_api import QuotasApi


class TestQuotasApi(unittest.TestCase):
    """QuotasApi unit test stubs"""

    def setUp(self) -> None:
        self.api = QuotasApi()

    def tearDown(self) -> None:
        pass

    def test_assign_organizations_account_groups_quotas_models_validation(self) -> None:
        """Test case for assign_organizations_account_groups_quotas request and response models"""
        request_body_json = """
                {
                  "organizations" : [ {
                    "orgId" : "1234",
                    "accountGroups" : [ {
                      "value" : 12000,
                      "aid" : "1234"
                    }, {
                      "value" : 12000,
                      "aid" : "1234"
                    } ]
                  }, {
                    "orgId" : "1234",
                    "accountGroups" : [ {
                      "value" : 12000,
                      "aid" : "1234"
                    }, {
                      "value" : 12000,
                      "aid" : "1234"
                    } ]
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.usage.models.OrganizationsQuotasAssign.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "organizations" : [ {
                    "orgId" : "1234",
                    "accountGroups" : [ {
                      "value" : 12000,
                      "aid" : "1234"
                    }, {
                      "value" : 12000,
                      "aid" : "1234"
                    } ]
                  }, {
                    "orgId" : "1234",
                    "accountGroups" : [ {
                      "value" : 12000,
                      "aid" : "1234"
                    }, {
                      "value" : 12000,
                      "aid" : "1234"
                    } ]
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.usage.models.OrganizationsQuotasAssign.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_assign_organizations_quotas_models_validation(self) -> None:
        """Test case for assign_organizations_quotas request and response models"""
        request_body_json = """
                {
                  "organizations" : [ {
                    "value" : 12000
                  }, {
                    "orgId" : "1234",
                    "value" : 10000
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.usage.models.QuotasAssignRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "organizations" : [ {
                    "orgId" : "1234",
                    "value" : 12000
                  }, {
                    "orgId" : "12345",
                    "value" : 10000
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.usage.models.QuotasAssignResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_quotas_models_validation(self) -> None:
        """Test case for get_quotas request and response models"""

        response_body_json = """
                {
                  "quotas" : [ {
                    "accountGroupQuotas" : [ {
                      "value" : 12000,
                      "aid" : "1234"
                    }, {
                      "value" : 10000,
                      "aid" : "12345"
                    } ],
                    "organizationQuota" : {
                      "value" : 22500,
                      "orgId" : "10"
                    }
                  }, {
                    "accountGroupQuotas" : [ {
                      "value" : 12000,
                      "aid" : "1234"
                    }, {
                      "value" : 10000,
                      "aid" : "12345"
                    } ],
                    "organizationQuota" : {
                      "value" : 22500,
                      "orgId" : "10"
                    }
                  } ],
                  "_links" : {
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  }
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.usage.models.Quotas.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_unassign_organizations_account_groups_quotas_models_validation(self) -> None:
        """Test case for unassign_organizations_account_groups_quotas request and response models"""
        request_body_json = """
                {
                  "organizations" : [ {
                    "orgId" : "1234",
                    "accountGroups" : [ "1234", "12345" ]
                  }, {
                    "orgId" : "1234",
                    "accountGroups" : [ "1234", "12345" ]
                  } ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.usage.models.OrganizationsQuotasUnassign.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)


    def test_unassign_organizations_quotas_models_validation(self) -> None:
        """Test case for unassign_organizations_quotas request and response models"""
        request_body_json = """
                {
                  "organizations" : [ "1234", "12345" ]
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.usage.models.QuotasUnassign.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)



if __name__ == '__main__':
    unittest.main()
