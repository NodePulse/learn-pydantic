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

# temp = patient.model_dump()
# temp = patient.model_dump_json()
# temp = patient.model_dump(include={"name", "age"})
# temp = patient.model_dump(exclude={"address"})
temp = patient.model_dump(exclude={"address": {"state"}})

print(temp)
print(type(temp))