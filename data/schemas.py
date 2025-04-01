from pydantic import BaseModel
from datetime import date

# This file contains the data models for the application,
# it uses Pydantic for data validation and serialization.

class MarkSchema(BaseModel):
    subjectName: str
    markValue: float
    markDate: date
    comment: str