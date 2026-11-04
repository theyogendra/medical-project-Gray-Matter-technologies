"""
Tests for E4 · Clinical review.

Run from backend/:   pytest app/modules/e4_clinical_review
Rule of thumb: every "Done when" in your sheet tab becomes at least one test here.
"""

SAMPLE = {"case_id": 1, "doctor_name": "Dr. Rao", "status": "Sent", "expires_at": "2026-11-10"}


def test_create_then_list(client):
    created = client.post("/api/e4/review-requests", json=SAMPLE)
    assert created.status_code == 201
    assert created.json()["id"] == 1

    listed = client.get("/api/e4/review-requests")
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_get_one_and_missing_one(client):
    client.post("/api/e4/review-requests", json=SAMPLE)
    assert client.get("/api/e4/review-requests/1").status_code == 200
    assert client.get("/api/e4/review-requests/999").status_code == 404


def test_other_company_cannot_see_it(client):
    client.post("/api/e4/review-requests", json=SAMPLE, headers={"X-Company-Id": "1"})
    other = client.get("/api/e4/review-requests", headers={"X-Company-Id": "2"})
    assert other.json() == []
    assert client.get("/api/e4/review-requests/1", headers={"X-Company-Id": "2"}).status_code == 404


def test_missing_fields_are_refused(client):
    assert client.post("/api/e4/review-requests", json={}).status_code == 422
