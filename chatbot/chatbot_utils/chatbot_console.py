from openai import OpenAI
from constances import OPEN_AI_API_KEY
client = OpenAI(api_key=OPEN_AI_API_KEY)

response = client.responses.create(
    model="gpt-3.5-turbo",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)