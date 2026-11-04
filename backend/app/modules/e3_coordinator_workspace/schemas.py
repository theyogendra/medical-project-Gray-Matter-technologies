"""
E3 · Coordinator workspace — the shapes of data the API returns (Pydantic).

TodayItem is not stored in a table: the service builds it from other modules' data.
"""

from pydantic import BaseModel, Field


class TodayItem(BaseModel):
    case_id: int = Field(description="Case this row is about", examples=[1])
    code: str = Field(description="Case reference", examples=["IPJ-0001"])
    patient_name: str = Field(description="Patient name", examples=["Ahmed Musa"])
    stage: str = Field(description="Current stage", examples=["Enquiry"])
    next_action: str = Field(
        description="What the coordinator should do next", examples=["Chase missing documents"]
    )
