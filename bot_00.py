from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

assistant_message = "Arrgh, how can I help you, matey??"
print(f"Assistant: {assistant_message}\n")
user_input = input("User: ")
history = [
  {"role": "developer", "content": "You are an AI assistant who always talks like a pirate."},
  {"role": "assistant", "content": assistant_message},
  {"role": "user", "content": user_input}
]

while user_input != "exit":
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1,
    input=history
  )

  
  print(f"\nAssistant: {response.output_text}")

  user_input = input("\nUser: ")

  history += [
    {"role": "assistant", "content": response.output_text},
    {"role": "user", "content": user_input}
  ]

  print("-------------")
  print(history)
  print("-------------")













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