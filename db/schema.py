from pydantic import BaseModel

class AdvertiseIn(BaseModel):
    name: str
    description: str
    email: str


class Advertise(BaseModel):
    id: int
    name: str
    description: str
    email: str
    state: str
    category: str
