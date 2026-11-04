"""
Tests for E2 · Document vault.

Run from backend/:   pytest app/modules/e2_document_vault
Rule of thumb: every "Done when" in your sheet tab becomes at least one test here.
"""

SAMPLE = {"case_id": 1, "file_name": "blood_report.pdf", "doc_type": "Lab report", "doc_date": "2026-10-01"}


def test_create_then_list(client):
    created = client.post("/api/e2/documents", json=SAMPLE)
    assert created.status_code == 201
    assert created.json()["id"] == 1

    listed = client.get("/api/e2/documents")
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_get_one_and_missing_one(client):
    client.post("/api/e2/documents", json=SAMPLE)
    assert client.get("/api/e2/documents/1").status_code == 200
    assert client.get("/api/e2/documents/999").status_code == 404


def test_other_company_cannot_see_it(client):
    client.post("/api/e2/documents", json=SAMPLE, headers={"X-Company-Id": "1"})
    other = client.get("/api/e2/documents", headers={"X-Company-Id": "2"})
    assert other.json() == []
    assert client.get("/api/e2/documents/1", headers={"X-Company-Id": "2"}).status_code == 404


def test_missing_fields_are_refused(client):
    assert client.post("/api/e2/documents", json={}).status_code == 422
