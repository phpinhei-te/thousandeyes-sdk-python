# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.network_dynamic_test_result import NetworkDynamicTestResult

class TestNetworkDynamicTestResult(unittest.TestCase):
    """NetworkDynamicTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkDynamicTestResult:
        """Test NetworkDynamicTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkDynamicTestResult`
        """
        model = NetworkDynamicTestResult()
        if include_optional:
            return NetworkDynamicTestResult(
                aid = '1234',
                agent_id = '861b7557-cd57-4bbb-b648-00bddf88ef49',
                round_id = 1384309800,
                server_ip = '185.199.108.153',
                network_profile = None,
                system_metrics = endpoint_test_results.models.system_metrics.SystemMetrics(
                    start_time_ms = 1581508857327, 
                    end_time_ms = 1581508867333, 
                    cpu_utilization = endpoint_test_results.models.cpu_utilization.CpuUtilization(
                        min = 0.22, 
                        max = 0.75, 
                        mean = 0.55, 
                        median = 0.61, 
                        std_dev = 0.01, 
                        count = 150, ), 
                    physical_memory_used_bytes = endpoint_test_results.models.physical_memory_used_bytes.PhysicalMemoryUsedBytes(
                        min = 1.2, 
                        max = 2.5, 
                        mean = 1.77, 
                        median = 1.85, 
                        std_dev = 0.25, 
                        count = 155, ), 
                    physical_memory_total_bytes = 1024, ),
                vpn_profile = endpoint_test_results.models.vpn_profile.VpnProfile(
                    vpn_client_addresses = ["184.81.113.85","13.129.91.62"], 
                    vpn_client_network_range = [
                        '9.88.37.27'
                        ], 
                    vpn_gateway_address = '120.98.134.7', 
                    vpn_type = 'cisco-anyconnect', ),
                avg_latency = 167.04,
                error_details = 'Error',
                jitter = 0.076808,
                is_icmp_blocked = True,
                loss = 0.0,
                max_latency = 168.0,
                min_latency = 167.0,
                application = 'webex',
                webex = endpoint_test_results.models.dynamic_base_test_result_webex.DynamicBaseTestResult_webex(
                    conference_id = '225817074608419375', 
                    correlation_id = '22581707460321454', 
                    local_sip_session_id = '22581707460321454', 
                    remote_sip_session_id = '22581707460321454', )
            )
        else:
            return NetworkDynamicTestResult(
        )
        """

    def testNetworkDynamicTestResult(self):
        """Test NetworkDynamicTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
