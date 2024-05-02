# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.update_sip_server_test1 import UpdateSipServerTest1

class TestUpdateSipServerTest1(unittest.TestCase):
    """UpdateSipServerTest1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSipServerTest1:
        """Test UpdateSipServerTest1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSipServerTest1`
        """
        model = UpdateSipServerTest1()
        if include_optional:
            return UpdateSipServerTest1(
                interval = 120,
                alerts_enabled = True,
                enabled = True,
                alert_rules = [
                    tests.models.alert_rule.AlertRule(
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
                        severity = 'major', )
                    ],
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'sip-server',
                links = tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltin":false}
                    ],
                shared_with_accounts = [
                    tests.models.shared_with_account.SharedWithAccount(
                        aid = '1234', 
                        name = 'Account name', )
                    ],
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                options_regex = '["a-z"]',
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                register_enabled = True,
                sip_target_time = 100,
                sip_time_limit = 5,
                fixed_packet_rate = 50,
                ipv6_policy = 'use-agent-policy',
                agents = [
                    null
                    ],
                target_sip_credentials = tests.models.test_sip_credentials.TestSipCredentials(
                    auth_user = 'username', 
                    password = 'password', 
                    port = 1, 
                    protocol = 'tcp', 
                    sip_registrar = 'voice.thousandeyes.com', 
                    user = 'username', ),
                bgp_measurements = True,
                use_public_bgp = True,
                monitors = [
                    tests.models.monitor.Monitor(
                        country_id = 'GB', 
                        monitor_id = '1234', 
                        ip_address = '4.69.184.193', 
                        network = 'Level 3 Communications, Inc. (AS 3356)', 
                        monitor_type = 'public', 
                        monitor_name = 'Seattle, WA', )
                    ]
            )
        else:
            return UpdateSipServerTest1(
                interval = 120,
                target_sip_credentials = tests.models.test_sip_credentials.TestSipCredentials(
                    auth_user = 'username', 
                    password = 'password', 
                    port = 1, 
                    protocol = 'tcp', 
                    sip_registrar = 'voice.thousandeyes.com', 
                    user = 'username', ),
        )
        """

    def testUpdateSipServerTest1(self):
        """Test UpdateSipServerTest1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
