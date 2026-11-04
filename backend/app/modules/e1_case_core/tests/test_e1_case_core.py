"""
Tests for E1 · Case management core.

Run from backend/:   pytest app/modules/e1_case_core
Rule of thumb: every "Done when" in your sheet tab becomes at least one test here.
"""

SAMPLE = {
    "code": "IPJ-0001",
    "patient_name": "Ahmed Musa",
    "country": "Nigeria",
    "stage": "Enquiry",
    "owner_name": "Coordinator A",
}


def test_create_then_list(client):
    created = client.post("/api/e1/cases", json=SAMPLE)
    assert created.status_code == 201
    assert created.json()["id"] == 1

    listed = client.get("/api/e1/cases")
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_get_one_and_missing_one(client):
    client.post("/api/e1/cases", json=SAMPLE)
    assert client.get("/api/e1/cases/1").status_code == 200
    assert client.get("/api/e1/cases/999").status_code == 404


def test_other_company_cannot_see_it(client):
    client.post("/api/e1/cases", json=SAMPLE, headers={"X-Company-Id": "1"})
    other = client.get("/api/e1/cases", headers={"X-Company-Id": "2"})
    assert other.json() == []
    assert client.get("/api/e1/cases/1", headers={"X-Company-Id": "2"}).status_code == 404


def test_missing_fields_are_refused(client):
    assert client.post("/api/e1/cases", json={}).status_code == 422
