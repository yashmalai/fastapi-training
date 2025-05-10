from typing import Annotated
from pydantic import BaseModel, constr, StringConstraints

class Creature(BaseModel):
    name: Annotated[str, StringConstraints(max_length=30)]
    country: str
    area: str
    description: str
    aka: str

    # def to_dict(self):
    #     return {
    #         'name': self.name,
    #         'country': self.country,
    #         'area': self.area,
    #         'description': self.description,
    #         'aka': self.aka
    #     }

thing = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
    )

# print("Name is", thing.name)