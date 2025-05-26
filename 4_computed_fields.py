from pydantic import BaseModel, EmailStr, AnyHttpUrl, Field, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name:Annotated[str, Field(max_length=20, title="Name of the patient", description="Give the name of the patient in less than 20 chars", examples=["Nitin", "Amit"])]
    email: EmailStr
    linkedin_url: AnyHttpUrl
    age: int = Field(gt=0, le=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    height: Annotated[float, Field(gt=0, strict=True, description="Provide the height of patient in meters")]
    married: Annotated[bool, Field(default=False, description="Is the patient married or not")]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(Self) -> float:
        bmi = round(Self.weight / (Self.height ** 2), 2)
        return bmi
    

def insert_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data inserted successfully")
    
# insert_patient_data("John Doe", 25)

patient_info = {
    "name": "Vikash Kumar",
    "email": "vikash@hdfc.com",
    "linkedin_url": "http://linkedin.com/153",
    "age": 30,
    "weight": 70.5,
    "height": 1.56,
    "married": True,
    # "allergies": ["penicillin", "dust"],
    "contact_details": {"phone": "1234567890"}
}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)