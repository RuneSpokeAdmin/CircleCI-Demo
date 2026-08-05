from app import create_app


def test_health():
    client = create_app().test_client()
    assert client.get("/health").status_code == 200


def test_widget_count():
    client = create_app().test_client()
    r = client.get("/widgets/count")
    assert r.status_code == 200
    assert r.get_json()["count"] == 3
