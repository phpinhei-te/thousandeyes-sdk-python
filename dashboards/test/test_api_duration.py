# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.api_duration import ApiDuration

class TestApiDuration(unittest.TestCase):
    """ApiDuration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiDuration:
        """Test ApiDuration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiDuration`
        """
        model = ApiDuration()
        if include_optional:
            return ApiDuration(
                value = 10,
                unit = 'Days'
            )
        else:
            return ApiDuration(
        )
        """

    def testApiDuration(self):
        """Test ApiDuration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
