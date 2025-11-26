from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


# Point to your local LM Studio server
llm = OpenAI(
    base_url="http://localhost:1234/v1",  # LM Studio default endpoint
    api_key="lm-studio"  # Can be any string for local models
)


# Use chat completions format
response = llm.chat.completions.create(
    model="phi-4-mini-reasoning",
    temperature=0,
    messages=[
        {"role": "user", "content": "Who was the first US president?"}
    ]
)


print(response.choices[0].message.content)
