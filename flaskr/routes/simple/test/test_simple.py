from http import HTTPStatus
from flaskr.routes.simple.route import api

url = api.name


def test_get_request(client):
    """GETリクエスト: 正常系"""
    # 実行
    rv = client.get(url, follow_redirects=True)

    # 判定
    assert rv.status_code == HTTPStatus.OK
    assert rv.text == '"Response of GET Request"\n'


def test_post_request(client):
    """POSTリクエスト: 正常系"""
    # リクエスト情報
    request_body = {}

    # 実行
    rv = client.post(url, follow_redirects=True, json=request_body)

    # 判定
    assert rv.status_code == HTTPStatus.OK
    assert rv.text == '"Response of POST Request"\n'
