# coding: utf-8

"""
    Tags API

    The ThousandEyes Tags API provides a tagging system with key/value pairs. It allows you to tag assets within the ThousandEyes platform (such as agents, tests, or alert rules) with meaningful metadata. For example: `branch:sfo`, `branch:nyc`, and `team:netops`.  This feature provides:  * Support for automation. * Powerful and flexible reports/dashboards. * Support for third-party integrations.  Things to note with the ThousandEyes Tags API:  * Tags are backwards-compatible with existing labels. * Tags are separated by Tests (CEA), Agents (CEA), Endpoint Agents, Scheduled Endpoint Tests, and Reports. A single tag can only apply to one type of target object, so each tag must specify the target type of object via a `type` field. * Tags are defined in a single table so that they can be represented using a single model - `Tag`. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tags.models.validation_error import ValidationError

class TestValidationError(unittest.TestCase):
    """ValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationError:
        """Test ValidationError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationError`
        """
        model = ValidationError()
        if include_optional:
            return ValidationError(
                type = '',
                title = '',
                status = 56,
                detail = '',
                instance = '',
                errors = [
                    tags.models.validation_error_all_of_errors.ValidationError_allOf_errors(
                        code = '', 
                        field = 56, 
                        message = '', )
                    ]
            )
        else:
            return ValidationError(
        )
        """

    def testValidationError(self):
        """Test ValidationError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
