from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

user_input = input("Assistant: How can I help you today?\n\nUser: ")

while user_input != "exit":
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1,
    input=user_input
  )

  print(f"\nAssitant: {response.output_text}")

  user_input = input("\nUser: ")

# user_input = input("Share anything with me and I'll translate it to French: \n")

# def translate_to_french(text):
#   llm = OpenAI()
#   response = llm.responses.create(
#     model="gpt-4.1-mini",
#     temperature=1,
#     input=f"Translate the following into French, and only include the translation itself with no introductory text: {text}"
#   )

#   return response.output_text


# print(translate_to_french(user_input))