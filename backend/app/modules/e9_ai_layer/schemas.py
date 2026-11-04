"""
E9 · AI layer — the shapes of data the API returns (Pydantic).

Suggestion is not stored in a table: the service builds it from other modules' data.
"""

from pydantic import BaseModel, Field


class Suggestion(BaseModel):
    document_id: int = Field(description="Document the suggestion is about", examples=[1])
    file_name: str = Field(description="File name", examples=["blood_report.pdf"])
    current_type: str = Field(description="Type stored in the vault now", examples=["Other"])
    suggested_type: str = Field(description="What the AI thinks it is", examples=["Lab report"])
    reason: str = Field(
        description="Why: every AI answer must show its source", examples=["File name contains 'blood'"]
    )
