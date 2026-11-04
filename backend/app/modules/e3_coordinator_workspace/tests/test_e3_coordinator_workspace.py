"""
Tests for E3 · Coordinator workspace.

Run from backend/:   pytest app/modules/e3_coordinator_workspace
"""

CASE = {
    "code": "IPJ-0001",
    "patient_name": "Ahmed Musa",
    "country": "Nigeria",
    "stage": "Enquiry",
    "owner_name": "Coordinator A",
}


def test_today_is_empty_without_cases(client):
    assert client.get("/api/e3/today").json() == []


def test_today_shows_each_case_with_next_action(client):
    client.post("/api/e1/cases", json=CASE)  # create the case through E1's API
    today = client.get("/api/e3/today").json()
    assert today[0]["code"] == "IPJ-0001"
    assert today[0]["next_action"] == "Collect medical reports"


def test_today_only_shows_own_company(client):
    client.post("/api/e1/cases", json=CASE, headers={"X-Company-Id": "1"})
    assert client.get("/api/e3/today", headers={"X-Company-Id": "2"}).json() == []
