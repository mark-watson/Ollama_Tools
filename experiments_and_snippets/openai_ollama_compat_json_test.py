from openai import OpenAI
import openai
from pydantic import BaseModel

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

class Pet(BaseModel):
    name: str
    animal: str
    age: int
    color: str | None
    favorite_toy: str | None

class PetList(BaseModel):
    pets: list[Pet]

try:
    completion = client.beta.chat.completions.parse(
        temperature=0,
        model="llama3.2:latest",
        messages=[
            {"role": "user", "content": '''
                I have two pets.
                A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
                I also have a 2 year old black cat named Loki who loves tennis balls.
            '''}
        ],
        response_format=PetList.model_json_schema(),
    )

    pet_response = completion.choices[0].message
    print(pet_response)
    print(pet_response.content)
    print(dir(pet_response))
    if pet_response.parsed:
        print(pet_response.parsed)
    elif pet_response.refusal:
        print(pet_response.refusal)
except Exception as e:
    if type(e) == openai.LengthFinishReasonError:
        print("Too many tokens: ", e)
        pass
    else:
        print(e)
        pass

