# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dashboards.models.dashboard_snapshots_page import DashboardSnapshotsPage

class TestDashboardSnapshotsPage(unittest.TestCase):
    """DashboardSnapshotsPage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DashboardSnapshotsPage:
        """Test DashboardSnapshotsPage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DashboardSnapshotsPage`
        """
        model = DashboardSnapshotsPage()
        if include_optional:
            return DashboardSnapshotsPage(
                pages = { },
                dashboard_snapshots = [
                    null
                    ]
            )
        else:
            return DashboardSnapshotsPage(
        )
        """

    def testDashboardSnapshotsPage(self):
        """Test DashboardSnapshotsPage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
