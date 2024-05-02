# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.get_endpoint_local_networks_topologies200_response import GetEndpointLocalNetworksTopologies200Response

class TestGetEndpointLocalNetworksTopologies200Response(unittest.TestCase):
    """GetEndpointLocalNetworksTopologies200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEndpointLocalNetworksTopologies200Response:
        """Test GetEndpointLocalNetworksTopologies200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEndpointLocalNetworksTopologies200Response`
        """
        model = GetEndpointLocalNetworksTopologies200Response()
        if include_optional:
            return GetEndpointLocalNetworksTopologies200Response(
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                results = [
                    endpoint_test_results.models.local_network_topology_result_base.LocalNetworkTopologyResultBase(
                        agent_id = '861b7557-cd57-4bbb-b648-00bddf88ef49', 
                        date = '2022-07-17T22:00:54Z', 
                        network_topology_id = '00160:54c3a4b180c6:1490536500:c7a58c49', 
                        round_id = 1384309800, 
                        target = '10.0.2.2', 
                        target_port = 80, 
                        type = 'vpn', 
                        icmp_ping = endpoint_test_results.models.network_ping.NetworkPing(
                            avg_rtt = 7, 
                            max_rtt = 66, 
                            mean_dev_rtt = 11, 
                            min_rtt = 1, 
                            pkts_received = 10, 
                            pkts_sent = 10, 
                            error = 'An operation timed out.', 
                            info_flags = ["TE_INFO_ICMP_BLOCKED_BY_FIREWALL"], ), 
                        is_icmp_blocked = True, 
                        tcp_connect = endpoint_test_results.models.tcp_connect.TcpConnect(
                            rtt = 77.777, 
                            error_code = 'ERR_TIMED_OUT', 
                            error = 'An operation timed out.', 
                            info_flags = ["TE_INFO_ICMP_BLOCKED_BY_FIREWALL"], ), 
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
                            physical_memory_total_bytes = 1024, ), )
                    ],
                links = endpoint_test_results.models.pagination_next_link__links.PaginationNextLink__links(
                    next = endpoint_test_results.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return GetEndpointLocalNetworksTopologies200Response(
        )
        """

    def testGetEndpointLocalNetworksTopologies200Response(self):
        """Test GetEndpointLocalNetworksTopologies200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
