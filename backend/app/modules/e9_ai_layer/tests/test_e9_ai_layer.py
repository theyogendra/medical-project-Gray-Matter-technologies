"""
Tests for E9 · AI layer.

Run from backend/:   pytest app/modules/e9_ai_layer
"""

from app.modules.e9_ai_layer.service import suggest_type


def test_keyword_rule_gives_type_and_reason():
    assert suggest_type("Blood_Report_Oct.pdf") == ("Lab report", "File name contains 'blood'")
    assert suggest_type("holiday.jpg") is None


def test_suggestion_for_wrongly_typed_document(client):
    client.post(
        "/api/e2/documents",
        json={"case_id": 1, "file_name": "blood_report.pdf", "doc_type": "Other", "doc_date": "2026-10-01"},
    )
    suggestions = client.get("/api/e9/suggestions").json()
    assert suggestions[0]["suggested_type"] == "Lab report"
    assert suggestions[0]["reason"]  # every AI answer must show its source


def test_no_suggestion_when_type_already_right(client):
    client.post(
        "/api/e2/documents",
        json={
            "case_id": 1,
            "file_name": "blood_report.pdf",
            "doc_type": "Lab report",
            "doc_date": "2026-10-01",
        },
    )
    assert client.get("/api/e9/suggestions").json() == []
