def test_server_is_up(client):
    assert client.get("/api/health").json() == {"ok": True}
