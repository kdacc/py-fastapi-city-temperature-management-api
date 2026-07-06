from pydantic import BaseModel
from datetime import datetime


class City(BaseModel):
    id: int
    name: str
    additional_info: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


class CityCreate(City):
    name: str
    additional_info: str


class CityUpdate(City):
    name: str
    additional_info: str

class Temperature(BaseModel):
    id: int
    city_id: int
    date_time: datetime
    temperature: float

    class Config:
        orm_mode = True