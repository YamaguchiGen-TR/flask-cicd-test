import pytest

""" このコードは全test_***.py で使用されます"""


@pytest.fixture(scope='session')
def app():
    from flaskr import create_app
    app = create_app()
    app.config['TESTING'] = True
    return app


@pytest.fixture(scope='session')
def client(app):
    """
    リクエストを送るテスト用クライアントを作成する。
    @pytest.fixtureにより、作成したクライアントは各テストの引数に渡される
    """
    return app.test_client()
