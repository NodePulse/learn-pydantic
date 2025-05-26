from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: int

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

patient_address = {"city": "Delhi", "state": "Delhi", "pin": 110001}
address = Address(**patient_address)

patient_info = {"name": "Vikash Kumar", "gender": "Male", "age": 30, "address": address}
patient = Patient(**patient_info)

print(patient)