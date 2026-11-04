"""
Tests for E7 · Patient journey.

Run from backend/:   pytest app/modules/e7_patient_journey
Rule of thumb: every "Done when" in your sheet tab becomes at least one test here.
"""

SAMPLE = {"case_id": 1, "contact_name": "Fatima Musa", "phone": "+234 800 000 0000", "active": True}


def test_create_then_list(client):
    created = client.post("/api/e7/family-links", json=SAMPLE)
    assert created.status_code == 201
    assert created.json()["id"] == 1

    listed = client.get("/api/e7/family-links")
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_get_one_and_missing_one(client):
    client.post("/api/e7/family-links", json=SAMPLE)
    assert client.get("/api/e7/family-links/1").status_code == 200
    assert client.get("/api/e7/family-links/999").status_code == 404


def test_other_company_cannot_see_it(client):
    client.post("/api/e7/family-links", json=SAMPLE, headers={"X-Company-Id": "1"})
    other = client.get("/api/e7/family-links", headers={"X-Company-Id": "2"})
    assert other.json() == []
    assert client.get("/api/e7/family-links/1", headers={"X-Company-Id": "2"}).status_code == 404


def test_missing_fields_are_refused(client):
    assert client.post("/api/e7/family-links", json={}).status_code == 422


CASE = {
    "code": "IPJ-0001",
    "patient_name": "Ahmed Musa",
    "country": "Nigeria",
    "stage": "Enquiry",
    "owner_name": "Coordinator A",
}


def test_journey_uses_case_stage_and_consent(client):
    client.post("/api/e1/cases", json=CASE)
    view = client.get("/api/e7/journey/1").json()
    assert view["stage_plain"].startswith("We have your enquiry")
    assert view["sharing_allowed"] is False  # no consent yet

    client.post("/api/e8/consents", json={"case_id": 1, "scope": "Share with family", "granted": True})
    assert client.get("/api/e7/journey/1").json()["sharing_allowed"] is True
