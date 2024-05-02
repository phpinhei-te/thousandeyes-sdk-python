# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from snapshots.models.snapshot_links import SnapshotLinks

class TestSnapshotLinks(unittest.TestCase):
    """SnapshotLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnapshotLinks:
        """Test SnapshotLinks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnapshotLinks`
        """
        model = SnapshotLinks()
        if include_optional:
            return SnapshotLinks(
                links = {"self":{"href":"http://api.thousandeyes.com/v7/tests/227103/snapshot"},"appLink":{"href":"https://app.stg.thousandeyes.com/view/tests/?testId=227103&__a=105"}}
            )
        else:
            return SnapshotLinks(
        )
        """

    def testSnapshotLinks(self):
        """Test SnapshotLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
