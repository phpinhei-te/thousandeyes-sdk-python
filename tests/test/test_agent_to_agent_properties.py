# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.agent_to_agent_properties import AgentToAgentProperties

class TestAgentToAgentProperties(unittest.TestCase):
    """AgentToAgentProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentToAgentProperties:
        """Test AgentToAgentProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentToAgentProperties`
        """
        model = AgentToAgentProperties()
        if include_optional:
            return AgentToAgentProperties(
                direction = 'to-target',
                dscp = 'Best Effort (DSCP 0)',
                dscp_id = '0',
                mss = 20,
                num_path_traces = 1,
                path_trace_mode = 'classic',
                port = 1,
                protocol = 'tcp',
                target_agent_id = '2954',
                throughput_measurements = True,
                throughput_duration = 5000,
                throughput_rate = 8,
                fixed_packet_rate = 50,
                type = 'agent-to-agent'
            )
        else:
            return AgentToAgentProperties(
                target_agent_id = '2954',
        )
        """

    def testAgentToAgentProperties(self):
        """Test AgentToAgentProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
