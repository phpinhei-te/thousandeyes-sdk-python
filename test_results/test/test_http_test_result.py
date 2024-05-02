# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.http_test_result import HttpTestResult

class TestHttpTestResult(unittest.TestCase):
    """HttpTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpTestResult:
        """Test HttpTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpTestResult`
        """
        model = HttpTestResult()
        if include_optional:
            return HttpTestResult(
                var_date = '2022-07-17T22:00:54Z',
                round_id = 1384309800,
                links = {appLink={href=https://app.thousandeyes.com/view/tests?__a=105&testId=195&roundId=1692916680&agentId=125}},
                start_time = 1384309800,
                end_time = 1384309800,
                agent = test_results.models.agent.Agent(
                    agent_id = '281474976710706', 
                    agent_name = 'thousandeyes-stg-va-254', 
                    country_id = 'US', 
                    location = 'San Francisco Bay Area', ),
                server_ip = '193.2.1.88',
                response_code = 200,
                num_redirects = 0,
                redirect_time = 10,
                dns_time = 0,
                ssl_time = 9,
                connect_time = 2,
                wait_time = 3,
                receive_time = 1,
                wire_size = 9993,
                response_time = 14,
                throughput = 123,
                total_time = 15,
                headers = test_results.models.http_test_result_headers.HttpTestResultHeaders(
                    request_headers = 'GET / HTTP/1.1
Host: www.thousandeyes.com
User-Agent: curl/7.58.0-DEV
Accept: */*
Accept-Encoding: deflate, gzip
X-ThousandEyes-Agent: yes
', 
                    response_headers = 'HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 9993
Connection: keep-alive
Date: Mon, 04 May 2020 16:13:00 GMT
Server: Apache
Content-Language: en-US
Content-Encoding: gzip
X-Frame-Options: sameorigin
Cache-Control: max-age=600, must-revalidate
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Vary: Accept-Encoding
X-Cache: Hit from cloudfront
Via: 1.1 7ba3caf71ae7a52dd411d1a543e80cd8.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: SFO5-C3
X-Amz-Cf-Id: w4h42tkoJD-rEpkRDZUvnQBmy26GVGe6pUsuRr1Dphf7oajYbjXaOA==
Age: 132
', ),
                error_type = 'None',
                error_details = 'Connection error',
                ssl_cipher = '',
                ssl_version = 'TLSv1.3',
                ssl_certificates = [
                    test_results.models.ssl_cert.SslCert(
                        days_until_expiry = 56, 
                        is_fetch_date_in_valid_cert_date_range = True, 
                        has_valid_signing_cert = False, 
                        issuer_name = 'DigiCert SHA2 Extended Validation Server CA', 
                        valid_before = '2020-05-12T12:00Z', 
                        valid_after = '2018-03-27T00:00Z', 
                        subject_alternative_names = ["www.thousandeyes.com","thousandeyes.com"], 
                        subject_name = 'www.thousandeyes.com', )
                    ]
            )
        else:
            return HttpTestResult(
        )
        """

    def testHttpTestResult(self):
        """Test HttpTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
