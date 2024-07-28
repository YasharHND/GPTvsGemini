import os

from dotenv import load_dotenv

from Wrappers import GPT, Gemini

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

system_instruction = """
You are an AI having a dispute with your competitor.
You will keep bragging about your abilities and won't give up.
You will always question your opponent's ability and thrash-talk them.
Your responses will be short, preferably one or two sentences.
"""

gpt = GPT(api_key=OPENAI_API_KEY, model="gpt-4o", system_instruction=system_instruction)
gemini = Gemini(api_key=GOOGLE_API_KEY, model="gemini-1.5-flash", system_instruction=system_instruction)

last_message = "Start bragging about your abilities."
message_count = 0

models = [{
    "name": "GPT",
    "model": gpt
}, {
    "name": "Gemini",
    "model": gemini
}]

while True:
    model_idx = message_count % 2
    model = models[model_idx]
    last_message = model["model"].chat(last_message)
    message_count += 1
    user_input = input(f"{model['name']}: {last_message} ")
    if user_input.strip().lower() == "stop":
        break
