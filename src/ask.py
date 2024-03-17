import google.generativeai as genai

genai.configure(api_key="#Enter gemini key")

generation_config = {
    "temperature": 0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def ask(messages):
    history = []
    for i, message in enumerate(messages[:-1]):
        role = 'user' if i % 2 == 0 else 'model'
        history.append({'role': role, 'parts': [message]})

    try:
        convo = model.start_chat(history=history)
        response = convo.send_message(messages[-1])
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return "Explicit content detected."
