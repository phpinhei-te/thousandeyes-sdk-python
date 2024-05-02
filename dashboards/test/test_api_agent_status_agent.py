# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.api_agent_status_agent import ApiAgentStatusAgent

class TestApiAgentStatusAgent(unittest.TestCase):
    """ApiAgentStatusAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAgentStatusAgent:
        """Test ApiAgentStatusAgent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAgentStatusAgent`
        """
        model = ApiAgentStatusAgent()
        if include_optional:
            return ApiAgentStatusAgent(
                agent_id = '6522',
                status = 'online',
                ip_info = dashboards.models.api_agent_status_ip_info.ApiAgentStatusIpInfo(
                    public_ip = '172.58.92.31', 
                    private_ip = '172.58.92.31', 
                    ipv6 = '', 
                    operative_system_version = '', ),
                agent_name = '0c3898000117',
                location = dashboards.models.api_agent_location.ApiAgentLocation(
                    latitude = 37.77493, 
                    longitude = -122.41942, 
                    location_name = 'San Francisco, California, US', )
            )
        else:
            return ApiAgentStatusAgent(
        )
        """

    def testApiAgentStatusAgent(self):
        """Test ApiAgentStatusAgent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
