# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.unexpanded_voice_test import UnexpandedVoiceTest

class TestUnexpandedVoiceTest(unittest.TestCase):
    """UnexpandedVoiceTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnexpandedVoiceTest:
        """Test UnexpandedVoiceTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnexpandedVoiceTest`
        """
        model = UnexpandedVoiceTest()
        if include_optional:
            return UnexpandedVoiceTest(
                interval = 120,
                alerts_enabled = True,
                enabled = True,
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'voice',
                links = tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                codec = 'G.711 @ 64 Kbps',
                codec_id = '0',
                dscp = 'Best Effort (DSCP 0)',
                dscp_id = '0',
                duration = 5,
                jitter_buffer = 0,
                num_path_traces = 1,
                port = 1024,
                target_agent_id = '281474976710706',
                bgp_measurements = True,
                use_public_bgp = True
            )
        else:
            return UnexpandedVoiceTest(
                interval = 120,
                target_agent_id = '281474976710706',
        )
        """

    def testUnexpandedVoiceTest(self):
        """Test UnexpandedVoiceTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
