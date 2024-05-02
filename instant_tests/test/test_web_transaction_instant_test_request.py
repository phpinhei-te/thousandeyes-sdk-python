# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instant_tests.models.web_transaction_instant_test_request import WebTransactionInstantTestRequest

class TestWebTransactionInstantTestRequest(unittest.TestCase):
    """WebTransactionInstantTestRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebTransactionInstantTestRequest:
        """Test WebTransactionInstantTestRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebTransactionInstantTestRequest`
        """
        model = WebTransactionInstantTestRequest()
        if include_optional:
            return WebTransactionInstantTestRequest(
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'web-transactions',
                links = instant_tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [9842, 1283],
                shared_with_accounts = [1234, 12345],
                auth_type = 'none',
                bandwidth_measurements = True,
                client_certificate = '-----BEGIN PRIVATE KEY-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
-----END CERTIFICATE-----
',
                content_regex = '(regex)+',
                custom_headers = {"root":{"header1":"value1"},"domains":{"domain1.com":{"header2":"value2"}},"all":{"header3":"value3"}},
                desired_status_code = '200',
                follow_redirects = True,
                http_target_time = 100,
                http_time_limit = 5,
                http_version = 1,
                include_headers = True,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                password = 'password',
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                protocol = 'tcp',
                ssl_version = 'Auto',
                ssl_version_id = '0',
                target_time = 1,
                time_limit = 5,
                transaction_script = 'if (true) { return true; }',
                url = 'www.thousandeyes.com',
                use_ntlm = False,
                user_agent = 'curl',
                username = 'username',
                verify_certificate = True,
                allow_unsafe_legacy_renegotiation = True,
                block_domains = 'domain.com/',
                disable_screenshot = True,
                allow_mic_and_camera = True,
                allow_geolocation = True,
                browser_language = 'en-US',
                page_loading_strategy = 'normal',
                fixed_packet_rate = 50,
                agents = [
                    {"agentId":"125","sourceIpAddress":"1.1.1.1"}
                    ],
                credentials = ["3247","1051"]
            )
        else:
            return WebTransactionInstantTestRequest(
                transaction_script = 'if (true) { return true; }',
                url = 'www.thousandeyes.com',
                agents = [
                    {"agentId":"125","sourceIpAddress":"1.1.1.1"}
                    ],
        )
        """

    def testWebTransactionInstantTestRequest(self):
        """Test WebTransactionInstantTestRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
