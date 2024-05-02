# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from agents.models.simple_enterprise_agent import SimpleEnterpriseAgent

class TestSimpleEnterpriseAgent(unittest.TestCase):
    """SimpleEnterpriseAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SimpleEnterpriseAgent:
        """Test SimpleEnterpriseAgent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SimpleEnterpriseAgent`
        """
        model = SimpleEnterpriseAgent()
        if include_optional:
            return SimpleEnterpriseAgent(
                ip_addresses = [99.139.65.220, 9bbd:8a0a:a257:5876:288b:6cb2:3f36:64ce],
                public_ip_addresses = [192.168.1.78, f9b2:3a21:f25c:d300:03f4:586d:f8d6:4e1c],
                network = 'AT&T Services, Inc. (AS 7018)',
                agent_id = '281474976710706',
                agent_name = 'thousandeyes-stg-va-254',
                location = 'San Francisco Bay Area',
                country_id = 'US',
                enabled = True,
                prefix = '99.128.0.0/11',
                verify_ssl_certificates = True,
                cluster_members = [
                    null
                    ],
                utilization = 25,
                account_groups = [
                    agents.models.account_group.AccountGroup()
                    ],
                ipv6_policy = 'force-ipv4',
                error_details = [
                    agents.models.error_detail.ErrorDetail(
                        code = 'agent-version-outdated', 
                        description = 'Agent Version 0.1.1 (latest: 1.0.0)', )
                    ],
                hostname = 'thousandeyes.com',
                last_seen = '2022-07-17T22:00:54Z',
                agent_state = 'online',
                keep_browser_cache = True,
                created_date = '2022-07-17T22:00:54Z',
                target_for_tests = '1.1.1.1',
                local_resolution_prefixes = [
                    '10.2.3.3/24'
                    ],
                interface_ip_mappings = [
                    agents.models.interface_ip_mapping.InterfaceIpMapping(
                        interface_name = 'wlp4s0', 
                        ip_addresses = ["73.252.207.219","2601:646:300:3ae0::b977"], )
                    ]
            )
        else:
            return SimpleEnterpriseAgent(
        )
        """

    def testSimpleEnterpriseAgent(self):
        """Test SimpleEnterpriseAgent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
