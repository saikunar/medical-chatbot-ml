from chatbot import chatbot_response

print("Medical Chatbot Assistant")
print("Type 'exit' to stop")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        break

    reply = chatbot_response(user_input)
    print(reply)
