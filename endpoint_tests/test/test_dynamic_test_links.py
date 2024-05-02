# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_tests.models.dynamic_test_links import DynamicTestLinks

class TestDynamicTestLinks(unittest.TestCase):
    """DynamicTestLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DynamicTestLinks:
        """Test DynamicTestLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DynamicTestLinks`
        """
        model = DynamicTestLinks()
        if include_optional:
            return DynamicTestLinks(
                var_self = None,
                test_results = [{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/network/filter"},{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/dynamic-tests/281474976710706/pathvis"}]
            )
        else:
            return DynamicTestLinks(
        )
        """

    def testDynamicTestLinks(self):
        """Test DynamicTestLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
