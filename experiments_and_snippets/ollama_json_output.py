from ollama import chat
from pydantic import BaseModel
import json

class Pet(BaseModel):
  name: str
  animal: str
  age: int
  color: str | None
  favorite_toy: str | None

class PetList(BaseModel):
  pets: list[Pet]

# Generate JSON schema from the Pydantic model
json_schema = PetList.model_json_schema()
print(json_schema)
response = chat(
  messages=[
    {
      'role': 'user',
      'content': '''
        Return as JSON:\nI have two pets.
        A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
        I also have a 2 year old black cat named Loki who loves tennis balls.
      ''',
    }
  ],
  model='llama3.2:latest',
  format=PetList.model_json_schema(),
)
print(response)
pets = PetList.model_validate_json(response.message.content)
print(pets)
print(f"{pets.pets[0]=}")
print(f"{pets.pets[0].name=}")
