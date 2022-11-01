from pydantic import BaseModel

class AdvertiseIn(BaseModel):
    description: str
    email: str
    state: str
    category: str

class Advertise(BaseModel):
    id: int
    description: str
    email: str
    state: str
    category: str
