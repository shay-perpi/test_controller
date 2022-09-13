# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from test_controller.swagger_server.models.test import Test  # noqa: E501
from test_controller.swagger_server.test import BaseTestCase


class TestTestController(BaseTestCase):
    """TestController integration test stubs"""

    def test_by_name(self):
        """Test case for by_name

        Test ingestion_discrete
        """
        body = 'body_example'
        query_string = [('test_id', 'test_id_example'),
                        ('add_params', 'add_params_example')]
        response = self.client.open(
            '/tests/',
            method='POST',
            data=json.dumps(body),
            content_type='Apliction/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

        print(response)


if __name__ == '__main__':
    import unittest
    unittest.main()
