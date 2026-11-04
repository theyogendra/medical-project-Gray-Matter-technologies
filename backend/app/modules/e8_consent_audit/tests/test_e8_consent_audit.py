"""
Tests for E8 · Consent and audit.

Run from backend/:   pytest app/modules/e8_consent_audit
Rule of thumb: every "Done when" in your sheet tab becomes at least one test here.
"""

SAMPLE = {"case_id": 1, "scope": "Share reports with Dr. Rao", "granted": True}


def test_create_then_list(client):
    created = client.post("/api/e8/consents", json=SAMPLE)
    assert created.status_code == 201
    assert created.json()["id"] == 1

    listed = client.get("/api/e8/consents")
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_get_one_and_missing_one(client):
    client.post("/api/e8/consents", json=SAMPLE)
    assert client.get("/api/e8/consents/1").status_code == 200
    assert client.get("/api/e8/consents/999").status_code == 404


def test_other_company_cannot_see_it(client):
    client.post("/api/e8/consents", json=SAMPLE, headers={"X-Company-Id": "1"})
    other = client.get("/api/e8/consents", headers={"X-Company-Id": "2"})
    assert other.json() == []
    assert client.get("/api/e8/consents/1", headers={"X-Company-Id": "2"}).status_code == 404


def test_missing_fields_are_refused(client):
    assert client.post("/api/e8/consents", json={}).status_code == 422
