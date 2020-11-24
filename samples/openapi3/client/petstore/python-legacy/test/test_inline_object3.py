# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import petstore_api
from petstore_api.models.inline_object3 import InlineObject3  # noqa: E501
from petstore_api.rest import ApiException

class TestInlineObject3(unittest.TestCase):
    """InlineObject3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InlineObject3
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = petstore_api.models.inline_object3.InlineObject3()  # noqa: E501
        if include_optional :
            return InlineObject3(
                integer = 10, 
                int32 = 20, 
                int64 = 56, 
                number = 32.1, 
                float = 1.337, 
                double = 67.8, 
                string = 'a', 
                pattern_without_delimiter = 'AUR,rZ#UM/?R,Fp^l6$ARjbhJk C>', 
                byte = 'YQ==', 
                binary = bytes(b'blah'), 
                date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                password = '0123456789', 
                callback = ''
            )
        else :
            return InlineObject3(
                number = 32.1,
                double = 67.8,
                pattern_without_delimiter = 'AUR,rZ#UM/?R,Fp^l6$ARjbhJk C>',
                byte = 'YQ==',
        )

    def testInlineObject3(self):
        """Test InlineObject3"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()