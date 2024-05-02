# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.tcp_connect import TcpConnect

class TestTcpConnect(unittest.TestCase):
    """TcpConnect unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TcpConnect:
        """Test TcpConnect
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TcpConnect`
        """
        model = TcpConnect()
        if include_optional:
            return TcpConnect(
                rtt = 77.777,
                error_code = 'ERR_TIMED_OUT',
                error = 'An operation timed out.',
                info_flags = ["TE_INFO_ICMP_BLOCKED_BY_FIREWALL"]
            )
        else:
            return TcpConnect(
        )
        """

    def testTcpConnect(self):
        """Test TcpConnect"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
