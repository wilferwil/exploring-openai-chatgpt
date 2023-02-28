import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to ask questions to ChatGPT
def ask_chat_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    answer = response.choices[0].text.strip()
    return answer

# Example usage
prompt = "What is the meaning of life?"
answer = ask_chat_gpt(prompt)
print(answer)

