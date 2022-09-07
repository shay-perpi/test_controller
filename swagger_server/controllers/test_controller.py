import connexion
import six

from swagger_server.models.test import Test  # noqa: E501
from swagger_server import util


def by_name(body, test_id, add_params=None):  # noqa: E501
    """Test ingestion_discrete

     # noqa: E501

    :param body: the new test add
    :type body: dict | bytes
    :param test_id: String ID of the Test to Post
    :type test_id: str
    :param add_params: description of this spesific test
    :type add_params: str

    :rtype: Test
    """
    if connexion.request.is_json:
        body = str.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
