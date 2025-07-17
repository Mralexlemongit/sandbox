import os

from openai import OpenAI, RateLimitError

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = OpenAI(
    api_key = OPENAI_API_KEY
)

try:
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt="Say this is a test",
        max_tokens=7,
        temperature=0
    )
    print(response.choices[0].message.content)

except RateLimitError:
    print("❌ Cuota excedida. Revisa tu uso en https://platform.openai.com/account/usage")


pass