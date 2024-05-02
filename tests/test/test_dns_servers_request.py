# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.dns_servers_request import DnsServersRequest

class TestDnsServersRequest(unittest.TestCase):
    """DnsServersRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsServersRequest:
        """Test DnsServersRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsServersRequest`
        """
        model = DnsServersRequest()
        if include_optional:
            return DnsServersRequest(
                dns_servers = ["dns-example.net","8.8.8.8"]
            )
        else:
            return DnsServersRequest(
        )
        """

    def testDnsServersRequest(self):
        """Test DnsServersRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
