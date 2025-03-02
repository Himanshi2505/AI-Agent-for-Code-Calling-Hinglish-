from chatbot import HinglishChatbot
from speech import speech_to_text, text_to_speech
from prompts import DEMO_SCHEDULING_PROMPT, CANDIDATE_INTERVIEW_PROMPT, PAYMENT_FOLLOWUP_PROMPT

def main():
    chatbot = HinglishChatbot()
    print("AI Cold Calling Agent Initialized")
    
    while True:
        print("Press Enter to start speaking, or type 'exit' to quit.")
        input()
        user_input = speech_to_text()
        print("User:", user_input)
        
        response = chatbot.respond(user_input)
        print("Bot:", response)
        
        text_to_speech(response)

if __name__ == "__main__":
    main()

