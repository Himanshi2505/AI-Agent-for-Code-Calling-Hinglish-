# from chatbot import HinglishChatbot
# from speech import speech_to_text, text_to_speech
# from prompts import DEMO_SCHEDULING_PROMPT, CANDIDATE_INTERVIEW_PROMPT, PAYMENT_FOLLOWUP_PROMPT

# def main():
#     chatbot = HinglishChatbot()
#     print("AI Cold Calling Agent Initialized")
    
#     while True:
#         print("Press Enter to start speaking, or type 'exit' to quit.")
#         input()
#         user_input = speech_to_text()
#         print("User:", user_input)
        
#         response = chatbot.respond(user_input)
#         print("Bot:", response)
        
#         text_to_speech(response)

# if __name__ == "__main__":
#     main()

from chatbot import HinglishChatbot
from speech import speech_to_text, text_to_speech
# from prompts import DEMO_SCHEDULING_PROMPT, CANDIDATE_INTERVIEW_PROMPT, PAYMENT_FOLLOWUP_PROMPT #Not needed
def fallback_speech_to_text():
    return input("User (Text): ")

def fallback_text_to_speech(text):
    print(f"Bot: {text}")

def main():
    chatbot = HinglishChatbot()
    print("AI Cold Calling Agent Initialized")

    while True:
        print("\nSelect a scenario:")
        print("1. ERP Demo Scheduling")
        print("2. Candidate Interview")
        print("3. Payment Follow-up")
        print("Type 'exit' to quit.")

        choice = input("Enter scenario number (1-3) or 'exit': ")

        if choice.lower() == 'exit':
            break

        if choice == '1':
            chatbot.set_scenario("demo")
        elif choice == '2':
            chatbot.set_scenario("interview")
        elif choice == '3':
            chatbot.set_scenario("payment")
        else:
            print("Invalid scenario choice.")
            continue

        print(f"Scenario: {chatbot.current_scenario}")

        while True:
            print("\nEnter your message or type 'back' to change scenario:")
            user_input = fallback_speech_to_text()

            if user_input.lower() == 'back':
                break  # Back to scenario selection

            try:
                response = chatbot.respond(user_input)
                fallback_text_to_speech(response)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")