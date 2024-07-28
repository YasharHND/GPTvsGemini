from google import generativeai
from openai import OpenAI


class GPT:
    def __init__(self, api_key, model, system_instruction):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.messages = [{"role": "system", "content": system_instruction}]

    def chat(self, user_message):
        self.messages.append({"role": "user", "content": user_message})
        response = self.client.chat.completions.create(model=self.model, messages=self.messages)
        assistant_message = response.choices[0].message.content.strip()
        self.messages.append({"role": "assistant", "content": assistant_message})
        return assistant_message


class Gemini:
    def __init__(self, api_key, model, system_instruction):
        generativeai.configure(api_key=api_key)
        generative_model = generativeai.GenerativeModel(model_name=model, safety_settings=4, system_instruction=system_instruction)
        self.session = generative_model.start_chat(history=[])

    def chat(self, user_message):
        response = self.session.send_message(user_message)
        return response.text.strip()
