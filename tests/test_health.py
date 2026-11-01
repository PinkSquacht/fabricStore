from fabric_store import create_app

def test_health():
    app = create_app()
    app.config["TESTING"] = True
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

    