# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.get_voice_tests200_response import GetVoiceTests200Response

class TestGetVoiceTests200Response(unittest.TestCase):
    """GetVoiceTests200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetVoiceTests200Response:
        """Test GetVoiceTests200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetVoiceTests200Response`
        """
        model = GetVoiceTests200Response()
        if include_optional:
            return GetVoiceTests200Response(
                tests = [
                    null
                    ],
                links = tests.models.self_links__links.SelfLinks__links(
                    self = tests.models.link.Link(
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
            return GetVoiceTests200Response(
        )
        """

    def testGetVoiceTests200Response(self):
        """Test GetVoiceTests200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
