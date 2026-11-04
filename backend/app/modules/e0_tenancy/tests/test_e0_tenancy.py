"""
Tests for E0 · Tenancy and onboarding.

Run from backend/:   pytest app/modules/e0_tenancy
"""


def test_sign_up_creates_a_company(client):
    r = client.post("/api/e0/companies", json={"name": "Sunrise Medical Travel", "plan": "Free"})
    assert r.status_code == 201
    assert r.json()["id"] == 1


def test_my_company(client):
    client.post("/api/e0/companies", json={"name": "Sunrise Medical Travel", "plan": "Free"})
    me = client.get("/api/e0/companies/me", headers={"X-Company-Id": "1"})
    assert me.json()["name"] == "Sunrise Medical Travel"


def test_a_company_only_sees_itself(client):
    client.post("/api/e0/companies", json={"name": "Company A", "plan": "Free"})
    client.post("/api/e0/companies", json={"name": "Company B", "plan": "Free"})
    seen = client.get("/api/e0/companies", headers={"X-Company-Id": "2"}).json()
    assert [c["name"] for c in seen] == ["Company B"]


def test_unknown_company_is_404(client):
    assert client.get("/api/e0/companies/me", headers={"X-Company-Id": "99"}).status_code == 404
