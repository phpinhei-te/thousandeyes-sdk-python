# coding: utf-8

"""
    Credentials API

    Manage credentials for transaction tests using the Credentials API.  The following permissions are required to access Credentials API endpoints:  * `Settings Tests Read` for read operations. * `Settings Tests Update` for write operations. * `View sensitive data in web transaction scripts` to view the encrypted value property of credentials. * `Settings Tests Create Transaction (Tx) Tests` to create credentials.  For more information about credentials, see [Working With Secure Credentials](https://docs.thousandeyes.com/product-documentation/browser-synthetics/transaction-tests/getting-started/working-with-secure-credentials). 

    The version of the OpenAPI document: 7.0.9
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.credentials.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.credentials.api.credentials_api import CredentialsApi


class TestCredentialsApi(unittest.TestCase):
    """CredentialsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CredentialsApi()

    def tearDown(self) -> None:
        pass

    def test_create_credential_models_validation(self) -> None:
        """Test case for create_credential request and response models"""
        request_body_json = """
                {
                  "name" : "Example Credential 1",
                  "value" : "Example Credential 1 Password"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.credentials.models.CredentialRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
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
                  },
                  "name" : "Example Credential",
                  "id" : "3247"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.credentials.models.CredentialWithoutValue.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_delete_credential_models_validation(self) -> None:
        """Test case for delete_credential request and response models"""


    def test_get_credential_models_validation(self) -> None:
        """Test case for get_credential request and response models"""

        response_body_json = """
                {
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
                  },
                  "name" : "Example Credential",
                  "id" : "3247",
                  "value" : "rwhR12uDm1Im47p5IVXgzz4ORgC7m48ajzzeWVUt"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.credentials.models.Credential.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_credentials_models_validation(self) -> None:
        """Test case for get_credentials request and response models"""

        response_body_json = """
                {
                  "credentials" : [ {
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
                    },
                    "name" : "Example Credential",
                    "id" : "3247",
                    "value" : "rwhR12uDm1Im47p5IVXgzz4ORgC7m48ajzzeWVUt"
                  }, {
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
                    },
                    "name" : "Example Credential",
                    "id" : "3247",
                    "value" : "rwhR12uDm1Im47p5IVXgzz4ORgC7m48ajzzeWVUt"
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
        response_from_json = thousandeyes_sdk.credentials.models.Credentials.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_update_credential_models_validation(self) -> None:
        """Test case for update_credential request and response models"""
        request_body_json = """
                {
                  "name" : "Example Credential 1",
                  "value" : "Example Credential 1 Password"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.credentials.models.CredentialRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
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
                  },
                  "name" : "Example Credential",
                  "id" : "3247"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.credentials.models.CredentialWithoutValue.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
