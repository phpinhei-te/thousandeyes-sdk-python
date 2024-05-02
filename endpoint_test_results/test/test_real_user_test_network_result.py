# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.real_user_test_network_result import RealUserTestNetworkResult

class TestRealUserTestNetworkResult(unittest.TestCase):
    """RealUserTestNetworkResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RealUserTestNetworkResult:
        """Test RealUserTestNetworkResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RealUserTestNetworkResult`
        """
        model = RealUserTestNetworkResult()
        if include_optional:
            return RealUserTestNetworkResult(
                agent_id = '861b7557-cd57-4bbb-b648-00bddf88ef49',
                var_date = '2022-07-17T22:00:54Z',
                id = '07625:1490529480:aVDViw0i',
                round_id = 1384309800,
                destination = endpoint_test_results.models.network_metrics.NetworkMetrics(
                    jitter = 46, 
                    latency = 150, 
                    loss = 0.1, 
                    target = '54.208.6.220', ),
                vpn = endpoint_test_results.models.network_metrics.NetworkMetrics(
                    jitter = 46, 
                    latency = 150, 
                    loss = 0.1, 
                    target = '54.208.6.220', ),
                proxy = endpoint_test_results.models.network_metrics.NetworkMetrics(
                    jitter = 46, 
                    latency = 150, 
                    loss = 0.1, 
                    target = '54.208.6.220', ),
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
                    physical_memory_total_bytes = 1024, )
            )
        else:
            return RealUserTestNetworkResult(
        )
        """

    def testRealUserTestNetworkResult(self):
        """Test RealUserTestNetworkResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
