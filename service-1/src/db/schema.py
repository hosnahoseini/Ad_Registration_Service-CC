from pydantic import BaseModel

class AdvertiseIn(BaseModel):
    description: str
    email: str
    state: str
    category: str
    address: str

class Advertise(BaseModel):
    id: int
    description: str
    email: str
    state: str
    category: str
    address: str
