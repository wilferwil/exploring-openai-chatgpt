import openai
import os
import sys

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to ask questions to ChatGPT
def ask_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    answer = response.choices[0].text.strip()
    return answer

if len(sys.argv) > 1:
    prompt = sys.argv[1]
else:
    prompt = input("Ask me anything: ")

answer = ask_chat_gpt(prompt)

print(answer)

