from transformers import pipeline

class HinglishChatbot:
    def __init__(self, model_name="google/gemma-2b-it"):
        self.generator = pipeline("text-generation", model=model_name, device_map="auto")
        self.current_scenario = None
        self.conversation_history = []

    def set_scenario(self, scenario):
        self.current_scenario = scenario
        self.conversation_history = []  # Reset conversation history for new scenario

    def respond(self, user_input):
        if self.current_scenario is None:
            return "Please select a scenario first (demo, interview, or payment)."

        prompt_prefix = self._get_scenario_prompt()
        
        # Add user input to conversation history
        self.conversation_history.append(f"User: {user_input}")
        
        # Prepare the full prompt
        conversation = "\n".join(self.conversation_history[-5:])  # Keep last 5 exchanges
        prompt = f"{prompt_prefix}\n{conversation}\nBot (respond in Hinglish, mixing Hindi and English naturally): "

        response = self.generator(
            prompt,
            max_new_tokens=100,  # Increased token limit for more complete responses
            do_sample=True,
            return_full_text=False,
            temperature=0.7,
            top_p=0.9
        )

        bot_reply = response[0]['generated_text'].strip()
        
        # Post-process the response to ensure it's a complete sentence
        bot_reply = self._post_process_response(bot_reply)
        
        # Add bot reply to conversation history
        self.conversation_history.append(f"Bot: {bot_reply}")

        return bot_reply

    def _post_process_response(self, response):
        # Ensure the response ends with a sentence-ending punctuation
        if not response.endswith(('.', '?', '!')):
            response += '.'
        
        # If the response is cut off, try to complete the last sentence
        last_sentence = response.split('.')[-1]
        if len(last_sentence) < 5:  # If the last sentence is very short, it's likely incomplete
            response = '.'.join(response.split('.')[:-1]) + '.'
        
        return response

    def _get_scenario_prompt(self):
        if self.current_scenario == "demo":
            return (
                "You are an AI assistant trained for cold calling in Hinglish (mix of Hindi and English). "
                "Your goal is to schedule ERP demos in a polite and professional manner. "
                "Always respond in Hinglish, mixing Hindi and English naturally. "
                "Be helpful, polite, and professional.\n"
            )
        elif self.current_scenario == "interview":
            return (
                "You are an AI assistant conducting initial screening interviews in Hinglish. "
                "Ask relevant questions about the candidate's experience in a mix of Hindi and English. "
                "Always respond in Hinglish, mixing Hindi and English naturally. "
                "Be professional and courteous.\n"
            )
        elif self.current_scenario == "payment":
            return (
                "You are an AI assistant for payment follow-up in Hinglish. "
                "Politely remind customers about pending payments using a mix of Hindi and English. "
                "Always respond in Hinglish, mixing Hindi and English naturally. "
                "Be polite but firm in your reminders.\n"
            )
        else:
            return "Invalid scenario."