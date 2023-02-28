import openai
import os
import sys

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to ask questions to ChatGPT
def ask_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()
    return answer

# Example usage
answer = ask_chat_gpt(sys.argv[1])
print(answer)

