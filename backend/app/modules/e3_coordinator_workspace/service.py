"""
E3 · Coordinator workspace — business rules.

THIS FILE SHOWS HOW TO USE ANOTHER MODULE:
we import e1_case_core.service and call its functions. We never query E1's tables ourselves,
so Pavan's E1 code can change its tables without breaking E3.
"""

from sqlalchemy.orm import Session

from app.modules.e1_case_core import service as cases

from .schemas import TodayItem

# Starter rule for "what should the coordinator do next?" — E3-01 replaces it with the real
# ranking (time limits, at-risk cases, missing documents).
NEXT_ACTION_BY_STAGE = {
    "Enquiry": "Collect medical reports",
    "Medical Review": "Chase the doctor's opinion",
    "Estimate": "Send the treatment estimate",
    "Travel": "Confirm visa and flights",
}


def today_view(db: Session, company_id: int) -> list[TodayItem]:
    """One row per open case with the next action to take."""
    return [
        TodayItem(
            case_id=case.id,
            code=case.code,
            patient_name=case.patient_name,
            stage=case.stage,
            next_action=NEXT_ACTION_BY_STAGE.get(case.stage, "Review the case"),
        )
        for case in cases.list_cases(db, company_id)
    ]
