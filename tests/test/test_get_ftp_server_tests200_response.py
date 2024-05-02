# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.get_ftp_server_tests200_response import GetFtpServerTests200Response

class TestGetFtpServerTests200Response(unittest.TestCase):
    """GetFtpServerTests200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetFtpServerTests200Response:
        """Test GetFtpServerTests200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetFtpServerTests200Response`
        """
        model = GetFtpServerTests200Response()
        if include_optional:
            return GetFtpServerTests200Response(
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
            return GetFtpServerTests200Response(
        )
        """

    def testGetFtpServerTests200Response(self):
        """Test GetFtpServerTests200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
