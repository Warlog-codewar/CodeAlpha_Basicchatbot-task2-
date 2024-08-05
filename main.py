#CodeAlpha_BasicChatbot(task2)
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm good what about you?",
    "bye": "Goodbye! Have a nice day!",
    "what is your name": "I'm chiggu a simple chatbot created by kartik singh",
    "how is it going": "I'm doing fantastic thanks for asking",
    "sing a song":"husan mera tauba tauba tauba tauba.. tururururu husn mera tauba tauba tauba tauba.... marjaniii paudi bhangraaa chiggu di beat pe...tu tututu tututututu..",
    "tell me a joke":"hey girl you look beautiful",
    "this is not a joke":"it is u ain't beautiful",
    "what is your age":"i am two minutes twenty point five seconds old",
" na manne tu":"badmoshii ni bhagat",
"how to make abs":"every morrow just move your ass from bed",
    "default": "I'm sorry, I did'nt get you. Can you please rephrase?"
}

def get_response(user_input):
    # Convert user input to lowercase to handle case insensitivity
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

def main():
    print("Welcome sir/ma'am  Chiggu this side a simple chatbot! Type 'bye' to exit.")

    while True:
        # Get user input
        user_input = input("You: ")

        # Check if user wants to exit
        if user_input.lower() == "bye":
            print("Chatbot: " + responses["bye sir/ma'am"])
            break

        # Get response from the chatbot
        response = get_response(user_input)
        print("Chatbot: " + response)

if __name__ == "__main__":
    main()