from typing import List, Optional

from pydantic import BaseModel, Field


class Test(BaseModel):
    name: Optional[str] = Field(None, description="Name of the test or biomarker")
    value: Optional[str] = Field(None, description="Measured result value")
    unit: Optional[str] = Field(None, description="Unit of measurement (e.g. mg/dL, g/dL)")
    reference_range: Optional[str] = Field(None, description="Normal reference range (e.g. 13.5 - 17.5)")
    is_abnormal: Optional[bool] = Field(None, description="True if result is flagged as abnormal or out of reference range")
    category: Optional[str] = Field(None, description="Category of test (e.g., Hematology, Chemistry, Lipids)")


class MedicalReport(BaseModel):
    patient_name: Optional[str] = Field(None, description="Patient full name")
    patient_id: Optional[str] = Field(None, description="Patient ID or MRN if available")
    date: Optional[str] = Field(None, description="Date of test or report")
    lab_name: Optional[str] = Field(None, description="Name of laboratory or clinic")
    doctor_name: Optional[str] = Field(None, description="Ordering physician name")
    clinical_summary: Optional[str] = Field(None, description="Brief summary of key findings and overall health status")
    tests: List[Test] = Field(default_factory=list, description="List of lab tests extracted from the report")
