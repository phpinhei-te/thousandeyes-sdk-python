# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.8
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.test_results.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.test_results.api.web_page_load_test_metrics_api import WebPageLoadTestMetricsApi


class TestWebPageLoadTestMetricsApi(unittest.TestCase):
    """WebPageLoadTestMetricsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebPageLoadTestMetricsApi()

    def tearDown(self) -> None:
        pass

    def test_get_test_page_load_agent_round_results_models_validation(self) -> None:
        """Test case for get_test_page_load_agent_round_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "numErrors" : 0,
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "responseTime" : 34.35,
                    "pageLoadTime" : 352,
                    "numObjects" : 17,
                    "totalSize" : 403301,
                    "domLoadTime" : 352,
                    "har" : {
                      "log" : {
                        "creator" : {
                          "name" : "ThousandEyes DB Exporter"
                        },
                        "entries" : [ {
                          "pageref" : "page_0",
                          "request" : {
                            "headers" : [ {
                              "name" : ":authority",
                              "value" : "google.com"
                            }, {
                              "name" : ":method",
                              "value" : "GET"
                            }, {
                              "name" : ":path",
                              "value" : "/"
                            }, {
                              "name" : ":scheme",
                              "value" : "https"
                            }, {
                              "name" : "accept",
                              "value" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                            }, {
                              "name" : "accept-encoding",
                              "value" : "gzip, deflate, br"
                            }, {
                              "name" : "accept-language",
                              "value" : "en-US,en;q=0.9"
                            }, {
                              "name" : "upgrade-insecure-requests",
                              "value" : "1"
                            }, {
                              "name" : "user-agent",
                              "value" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.83 Safari/537.36"
                            }, {
                              "name" : "x-thousandeyes-agent",
                              "value" : "yes"
                            } ],
                            "method" : "GET",
                            "url" : "https://google.com/"
                          },
                          "response" : {
                            "bodySize" : 220,
                            "content" : {
                              "mimeType" : "text/html",
                              "size" : 220
                            },
                            "headers" : [ {
                              "name" : "alt-svc",
                              "value" : "quic=\\":443\\"; ma=2592000; v=\\"46,43\\",h3-Q050=\\":443\\"; ma=2592000,h3-Q049=\\":443\\"; ma=2592000,h3-Q048=\\":443\\"; ma=2592000,h3-Q046=\\":443\\"; ma=2592000,h3-Q043=\\":443\\"; ma=2592000"
                            }, {
                              "name" : "cache-control",
                              "value" : "public, max-age=2592000"
                            }, {
                              "name" : "content-length",
                              "value" : "220"
                            }, {
                              "name" : "content-type",
                              "value" : "text/html; charset=UTF-8"
                            }, {
                              "name" : "date",
                              "value" : "Fri, 15 Nov 2019 16:41:54 GMT"
                            }, {
                              "name" : "expires",
                              "value" : "Sun, 15 Dec 2019 16:41:54 GMT"
                            }, {
                              "name" : "location",
                              "value" : "https://www.google.com/"
                            }, {
                              "name" : "server",
                              "value" : "gws"
                            }, {
                              "name" : "status",
                              "value" : "301"
                            }, {
                              "name" : "x-frame-options",
                              "value" : "SAMEORIGIN"
                            }, {
                              "name" : "x-xss-protection",
                              "value" : "0"
                            } ],
                            "headersSize" : 471,
                            "redirectURL" : "",
                            "status" : 301,
                            "statusText" : "MOVED_PERMANENTLY"
                          },
                          "serverIPAddress" : "172.217.6.110",
                          "startedDateTime" : "2019-11-15T16:41:54.798Z",
                          "time" : 71,
                          "timings" : {
                            "blocked" : 2,
                            "connect" : 16,
                            "dns" : 1,
                            "receive" : 1,
                            "send" : 0,
                            "ssl" : 14,
                            "wait" : 50
                          }
                        }, {
                          "pageref" : "page_0",
                          "request" : {
                            "headers" : [ {
                              "name" : ":authority",
                              "value" : "www.google.com"
                            }, {
                              "name" : ":method",
                              "value" : "GET"
                            }, {
                              "name" : ":path",
                              "value" : "/"
                            }, {
                              "name" : ":scheme",
                              "value" : "https"
                            }, {
                              "name" : "accept",
                              "value" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                            }, {
                              "name" : "accept-encoding",
                              "value" : "gzip, deflate, br"
                            }, {
                              "name" : "accept-language",
                              "value" : "en-US,en;q=0.9"
                            }, {
                              "name" : "upgrade-insecure-requests",
                              "value" : "1"
                            }, {
                              "name" : "user-agent",
                              "value" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.83 Safari/537.36"
                            }, {
                              "name" : "x-thousandeyes-agent",
                              "value" : "yes"
                            } ],
                            "method" : "GET",
                            "url" : "https://www.google.com/"
                          },
                          "response" : {
                            "bodySize" : 65214,
                            "content" : {
                              "mimeType" : "text/html",
                              "size" : 225039
                            },
                            "headers" : [ {
                              "name" : "alt-svc",
                              "value" : "quic=\\":443\\"; ma=2592000; v=\\"46,43\\",h3-Q050=\\":443\\"; ma=2592000,h3-Q049=\\":443\\"; ma=2592000,h3-Q048=\\":443\\"; ma=2592000,h3-Q046=\\":443\\"; ma=2592000,h3-Q043=\\":443\\"; ma=2592000"
                            }, {
                              "name" : "cache-control",
                              "value" : "private, max-age=0"
                            }, {
                              "name" : "content-encoding",
                              "value" : "br"
                            }, {
                              "name" : "content-length",
                              "value" : "65214"
                            }, {
                              "name" : "content-type",
                              "value" : "text/html; charset=UTF-8"
                            }, {
                              "name" : "date",
                              "value" : "Fri, 15 Nov 2019 16:41:54 GMT"
                            }, {
                              "name" : "expires",
                              "value" : "-1"
                            }, {
                              "name" : "p3p",
                              "value" : "CP=\\"This is not a P3P policy! See g.co/p3phelp for more info.\\""
                            }, {
                              "name" : "server",
                              "value" : "gws"
                            }, {
                              "name" : "set-cookie",
                              "value" : "(removed)"
                            }, {
                              "name" : "status",
                              "value" : "200"
                            }, {
                              "name" : "strict-transport-security",
                              "value" : "max-age=31536000"
                            }, {
                              "name" : "x-frame-options",
                              "value" : "SAMEORIGIN"
                            }, {
                              "name" : "x-xss-protection",
                              "value" : "0"
                            } ],
                            "headersSize" : 915,
                            "redirectURL" : "",
                            "status" : 200,
                            "statusText" : "OK"
                          },
                          "serverIPAddress" : "172.217.4.196",
                          "startedDateTime" : "2019-11-15T16:41:54.870Z",
                          "time" : 182,
                          "timings" : {
                            "blocked" : 2,
                            "connect" : 4,
                            "dns" : 0,
                            "receive" : 58,
                            "send" : 0,
                            "ssl" : 2,
                            "wait" : 118
                          }
                        } ],
                        "pages" : [ {
                          "id" : "page_0",
                          "pageTimings" : {
                            "onContentLoad" : 367,
                            "onLoad" : 737
                          },
                          "responseCode" : 0,
                          "startedDateTime" : "2019-11-15T16:41:54.796Z",
                          "title" : "Google"
                        } ],
                        "version" : "1.2"
                      }
                    },
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "numErrors" : 0,
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "responseTime" : 34.35,
                    "pageLoadTime" : 352,
                    "numObjects" : 17,
                    "totalSize" : 403301,
                    "domLoadTime" : 352,
                    "har" : {
                      "log" : {
                        "creator" : {
                          "name" : "ThousandEyes DB Exporter"
                        },
                        "entries" : [ {
                          "pageref" : "page_0",
                          "request" : {
                            "headers" : [ {
                              "name" : ":authority",
                              "value" : "google.com"
                            }, {
                              "name" : ":method",
                              "value" : "GET"
                            }, {
                              "name" : ":path",
                              "value" : "/"
                            }, {
                              "name" : ":scheme",
                              "value" : "https"
                            }, {
                              "name" : "accept",
                              "value" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                            }, {
                              "name" : "accept-encoding",
                              "value" : "gzip, deflate, br"
                            }, {
                              "name" : "accept-language",
                              "value" : "en-US,en;q=0.9"
                            }, {
                              "name" : "upgrade-insecure-requests",
                              "value" : "1"
                            }, {
                              "name" : "user-agent",
                              "value" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.83 Safari/537.36"
                            }, {
                              "name" : "x-thousandeyes-agent",
                              "value" : "yes"
                            } ],
                            "method" : "GET",
                            "url" : "https://google.com/"
                          },
                          "response" : {
                            "bodySize" : 220,
                            "content" : {
                              "mimeType" : "text/html",
                              "size" : 220
                            },
                            "headers" : [ {
                              "name" : "alt-svc",
                              "value" : "quic=\\":443\\"; ma=2592000; v=\\"46,43\\",h3-Q050=\\":443\\"; ma=2592000,h3-Q049=\\":443\\"; ma=2592000,h3-Q048=\\":443\\"; ma=2592000,h3-Q046=\\":443\\"; ma=2592000,h3-Q043=\\":443\\"; ma=2592000"
                            }, {
                              "name" : "cache-control",
                              "value" : "public, max-age=2592000"
                            }, {
                              "name" : "content-length",
                              "value" : "220"
                            }, {
                              "name" : "content-type",
                              "value" : "text/html; charset=UTF-8"
                            }, {
                              "name" : "date",
                              "value" : "Fri, 15 Nov 2019 16:41:54 GMT"
                            }, {
                              "name" : "expires",
                              "value" : "Sun, 15 Dec 2019 16:41:54 GMT"
                            }, {
                              "name" : "location",
                              "value" : "https://www.google.com/"
                            }, {
                              "name" : "server",
                              "value" : "gws"
                            }, {
                              "name" : "status",
                              "value" : "301"
                            }, {
                              "name" : "x-frame-options",
                              "value" : "SAMEORIGIN"
                            }, {
                              "name" : "x-xss-protection",
                              "value" : "0"
                            } ],
                            "headersSize" : 471,
                            "redirectURL" : "",
                            "status" : 301,
                            "statusText" : "MOVED_PERMANENTLY"
                          },
                          "serverIPAddress" : "172.217.6.110",
                          "startedDateTime" : "2019-11-15T16:41:54.798Z",
                          "time" : 71,
                          "timings" : {
                            "blocked" : 2,
                            "connect" : 16,
                            "dns" : 1,
                            "receive" : 1,
                            "send" : 0,
                            "ssl" : 14,
                            "wait" : 50
                          }
                        }, {
                          "pageref" : "page_0",
                          "request" : {
                            "headers" : [ {
                              "name" : ":authority",
                              "value" : "www.google.com"
                            }, {
                              "name" : ":method",
                              "value" : "GET"
                            }, {
                              "name" : ":path",
                              "value" : "/"
                            }, {
                              "name" : ":scheme",
                              "value" : "https"
                            }, {
                              "name" : "accept",
                              "value" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
                            }, {
                              "name" : "accept-encoding",
                              "value" : "gzip, deflate, br"
                            }, {
                              "name" : "accept-language",
                              "value" : "en-US,en;q=0.9"
                            }, {
                              "name" : "upgrade-insecure-requests",
                              "value" : "1"
                            }, {
                              "name" : "user-agent",
                              "value" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.83 Safari/537.36"
                            }, {
                              "name" : "x-thousandeyes-agent",
                              "value" : "yes"
                            } ],
                            "method" : "GET",
                            "url" : "https://www.google.com/"
                          },
                          "response" : {
                            "bodySize" : 65214,
                            "content" : {
                              "mimeType" : "text/html",
                              "size" : 225039
                            },
                            "headers" : [ {
                              "name" : "alt-svc",
                              "value" : "quic=\\":443\\"; ma=2592000; v=\\"46,43\\",h3-Q050=\\":443\\"; ma=2592000,h3-Q049=\\":443\\"; ma=2592000,h3-Q048=\\":443\\"; ma=2592000,h3-Q046=\\":443\\"; ma=2592000,h3-Q043=\\":443\\"; ma=2592000"
                            }, {
                              "name" : "cache-control",
                              "value" : "private, max-age=0"
                            }, {
                              "name" : "content-encoding",
                              "value" : "br"
                            }, {
                              "name" : "content-length",
                              "value" : "65214"
                            }, {
                              "name" : "content-type",
                              "value" : "text/html; charset=UTF-8"
                            }, {
                              "name" : "date",
                              "value" : "Fri, 15 Nov 2019 16:41:54 GMT"
                            }, {
                              "name" : "expires",
                              "value" : "-1"
                            }, {
                              "name" : "p3p",
                              "value" : "CP=\\"This is not a P3P policy! See g.co/p3phelp for more info.\\""
                            }, {
                              "name" : "server",
                              "value" : "gws"
                            }, {
                              "name" : "set-cookie",
                              "value" : "(removed)"
                            }, {
                              "name" : "status",
                              "value" : "200"
                            }, {
                              "name" : "strict-transport-security",
                              "value" : "max-age=31536000"
                            }, {
                              "name" : "x-frame-options",
                              "value" : "SAMEORIGIN"
                            }, {
                              "name" : "x-xss-protection",
                              "value" : "0"
                            } ],
                            "headersSize" : 915,
                            "redirectURL" : "",
                            "status" : 200,
                            "statusText" : "OK"
                          },
                          "serverIPAddress" : "172.217.4.196",
                          "startedDateTime" : "2019-11-15T16:41:54.870Z",
                          "time" : 182,
                          "timings" : {
                            "blocked" : 2,
                            "connect" : 4,
                            "dns" : 0,
                            "receive" : 58,
                            "send" : 0,
                            "ssl" : 2,
                            "wait" : 118
                          }
                        } ],
                        "pages" : [ {
                          "id" : "page_0",
                          "pageTimings" : {
                            "onContentLoad" : 367,
                            "onLoad" : 737
                          },
                          "responseCode" : 0,
                          "startedDateTime" : "2019-11-15T16:41:54.796Z",
                          "title" : "Google"
                        } ],
                        "version" : "1.2"
                      }
                    },
                    "startTime" : 1384309800,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.PageLoadDetailTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_test_page_load_results_models_validation(self) -> None:
        """Test case for get_test_page_load_results request and response models"""

        response_body_json = """
                {
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "endDate" : "2022-07-18T22:00:54Z",
                  "_links" : {
                    "next" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "previous" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "results" : [ {
                    "date" : "2022-07-17T22:00:54Z",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "totalSize" : 403301,
                    "numErrors" : 0,
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "responseTime" : 34.35,
                    "domLoadTime" : 352,
                    "startTime" : 1384309800,
                    "pageLoadTime" : 352,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "numObjects" : 17
                  }, {
                    "date" : "2022-07-17T22:00:54Z",
                    "agent" : {
                      "agentId" : "281474976710706",
                      "agentName" : "thousandeyes-stg-va-254",
                      "location" : "San Francisco Bay Area",
                      "countryId" : "US"
                    },
                    "totalSize" : 403301,
                    "numErrors" : 0,
                    "_links" : {
                      "appLink" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "responseTime" : 34.35,
                    "domLoadTime" : 352,
                    "startTime" : 1384309800,
                    "pageLoadTime" : 352,
                    "endTime" : 1384309800,
                    "roundId" : 1384309800,
                    "numObjects" : 17
                  } ],
                  "startDate" : "2022-07-17T22:00:54Z"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.test_results.models.PageLoadTestResults.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
