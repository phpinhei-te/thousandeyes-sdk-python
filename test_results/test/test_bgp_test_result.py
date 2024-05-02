# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.bgp_test_result import BgpTestResult

class TestBgpTestResult(unittest.TestCase):
    """BgpTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BgpTestResult:
        """Test BgpTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BgpTestResult`
        """
        model = BgpTestResult()
        if include_optional:
            return BgpTestResult(
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800,
                links = {appLink={href=https://app.thousandeyes.com/view/tests?__a=105&testId=195&roundId=1692916680&agentId=125}},
                monitor = test_results.models.monitor.Monitor(
                    monitor_id = '281474976710706', 
                    monitor_name = 'Vancouver, Canada - Bell Canada (AS 6539)', 
                    country_id = 'US', ),
                prefix_id = '215',
                prefix = '99.128.0.0/11',
                start_time = 1384309800,
                end_time = 1384309800,
                updates = 0.0,
                path_changes = 0.0,
                reachability = 0.0
            )
        else:
            return BgpTestResult(
        )
        """

    def testBgpTestResult(self):
        """Test BgpTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
