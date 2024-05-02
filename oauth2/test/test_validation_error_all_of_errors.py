# coding: utf-8

"""
    OAuth2 API

    This endpoint allows clients to trade their client credentials for an Access Token that can be used on subsequent calls to our API. Example of usage:    `   curl -X POST -H \"Content-Type: application/x-www-form-urlencoded\" -d 'client_id=someId&scope=someScope&client_secret=someSecret&grant_type=client_credentials' 'https://api.thousandeyes.com/v7/oauth2/token'   `

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from oauth2.models.validation_error_all_of_errors import ValidationErrorAllOfErrors

class TestValidationErrorAllOfErrors(unittest.TestCase):
    """ValidationErrorAllOfErrors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationErrorAllOfErrors:
        """Test ValidationErrorAllOfErrors
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationErrorAllOfErrors`
        """
        model = ValidationErrorAllOfErrors()
        if include_optional:
            return ValidationErrorAllOfErrors(
                code = '',
                var_field = 56,
                message = ''
            )
        else:
            return ValidationErrorAllOfErrors(
        )
        """

    def testValidationErrorAllOfErrors(self):
        """Test ValidationErrorAllOfErrors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
