# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from labels.models.get_labels200_response import GetLabels200Response

class TestGetLabels200Response(unittest.TestCase):
    """GetLabels200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLabels200Response:
        """Test GetLabels200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLabels200Response`
        """
        model = GetLabels200Response()
        if include_optional:
            return GetLabels200Response(
                labels = [
                    labels.models.label.Label(
                        label_id = '961123', 
                        is_built_in = True, 
                        name = 'Label XYZ', 
                        type = 'endpoint-test', )
                    ],
                links = labels.models.self_links__links.SelfLinks__links(
                    self = labels.models.link.Link(
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
            return GetLabels200Response(
        )
        """

    def testGetLabels200Response(self):
        """Test GetLabels200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
