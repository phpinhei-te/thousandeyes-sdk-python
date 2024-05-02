# coding: utf-8

"""
    ThousandEyes for OpenTelemetry API

    ThousandEyes for OpenTelemetry provides machine-to-machine integration between ThousandEyes and its customers. It allows you to export ThousandEyes telemetry data in OTel format, which is widely used in the industry. With ThousandEyes for OTel, you can leverage frameworks widely used in the observability domain - such as Splunk, Grafana, and Honeycomb - to capture and analyze ThousandEyes data. Any client that supports OTel can use ThousandEyes for OpenTelemetry.  ThousandEyes for OTel is made up of the following components:  * Data streaming APIs that you can use to configure and enable your ThousandEyes tests with OTel-compatible streams, in particular to configure how ThousandEyes telemetry data is exported to client integrations. * A set of streaming pipelines called _collectors_ that actively fetch ThousandEyes network test data, enrich the data with some additional detail, filter, and push the data to the customer-configured endpoints, depending on what you configure via the public APIs. * Third-party OTel collectors that receive, transform, filter, and export different metrics to client applications such as AppD, or any other OTel-capable client configuration.  For more information about ThousandEyes for OpenTelemetry, see the [documentation](https://docs.thousandeyes.com/product-documentation/api/opentelemetry). 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from streaming.models.stream_response_links import StreamResponseLinks

class TestStreamResponseLinks(unittest.TestCase):
    """StreamResponseLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StreamResponseLinks:
        """Test StreamResponseLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StreamResponseLinks`
        """
        model = StreamResponseLinks()
        if include_optional:
            return StreamResponseLinks(
                var_self = streaming.models.stream_response__links_self.StreamResponse__links_self(
                    href = 'https://api.thousandeyes.com/v7/streams/575766da-9664-4e85-94fe-facbe1154799', )
            )
        else:
            return StreamResponseLinks(
        )
        """

    def testStreamResponseLinks(self):
        """Test StreamResponseLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
