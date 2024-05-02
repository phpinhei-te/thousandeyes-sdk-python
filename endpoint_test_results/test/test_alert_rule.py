# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.alert_rule import AlertRule

class TestAlertRule(unittest.TestCase):
    """AlertRule unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AlertRule:
        """Test AlertRule
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AlertRule`
        """
        model = AlertRule()
        if include_optional:
            return AlertRule(
                rule_id = '127094',
                rule_name = 'The End of the Internet',
                expression = '((hops((hopDelay >= 100 ms))))',
                direction = 'to-target',
                is_default = True,
                alert_type = 'http-server',
                minimum_sources = 10,
                minimum_sources_pct = 99,
                rounds_violating_mode = 'exact',
                rounds_violating_out_of = 5,
                rounds_violating_required = 2,
                severity = 'major'
            )
        else:
            return AlertRule(
        )
        """

    def testAlertRule(self):
        """Test AlertRule"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
