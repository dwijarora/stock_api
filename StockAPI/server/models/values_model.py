from pydantic import BaseModel


class ValuesModel(BaseModel):
    scriptIds: str
