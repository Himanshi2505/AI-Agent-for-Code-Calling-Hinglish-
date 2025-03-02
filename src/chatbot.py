from transformers import pipeline
import json

class HinglishChatbot:
    def __init__(self, model_name="google/gemma-7b"):
        self.generator = pipeline("text-generation", model=model_name)
    
    def respond(self, prompt):
        response = self.generator(prompt, max_length=100, do_sample=True)
        return response[0]['generated_text']
