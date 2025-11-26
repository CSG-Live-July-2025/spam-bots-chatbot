from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

llm = OpenAI()

# system prompt
developer_message = """What follows below is a converation between a priate AI assistant and a human user:"""
assistant_message = "\nAssistant: Arrgh, how can I help you, matey??\n\nUser: "
user_input = input(assistant_message)
history = developer_message + assistant_message + user_input

while user_input != "exit":
  response = llm.responses.create(
    model="gpt-4.1-mini",
    temperature=1,
    input=history
  )

  llm_response_text = f"\nAssitant: {response.output_text}"
  print(llm_response_text)

  user_input = input("\nUser: ")
  history += f"{llm_response_text}\nUser: {user_input}"

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