import os
from google import genai

# 🔐 API Key yahan paste karo
client = genai.Client(api_key="AIzaSyAaaMTKwX2S_1XWr20-hNL7lHDq5gJ9HBk")

# ---- FAQ DATA ----
faq_list = {
    "What is your return policy?": "We offer a 7-day return policy for unused items.",
    "Do you offer cash on delivery?": "Yes, cash on delivery is available in selected areas.",
    "How long does delivery take?": "Delivery usually takes 3-5 business days.",
    "How can I track my order?": "You can track your order using the tracking link sent to your email."
}

faq_text = "\n".join([f"Q: {q}\nA: {a}" for q, a in faq_list.items()])

# System prompt to guide the assistant's behavior
system_prompt = f"""
  you are a professional customer support assistant for an e-commerce store
Rules:
1. Answer only from the provided FAQ list.
2. Maintain a polite and professional tone.
3. If the question is not in the FAQ list then respond exactly with "I am forwarding your query to our human support team"
4. Do not make up information.
5. Keep answers short and clear
This is the FAQ list , answer user quesries according to this list

{faq_text}

"""
# Greeting message
print("Bot: Hello! Welcome to our customer support. How can I assist you today?")

while True:
    user_input = input("You: ").strip()  # .strip() to remove extra spaces from user input

    if user_input.lower() == "exit" or user_input.lower() == "quit":   # Or if user_input.lower() in ["exit", "quit"]: 
        print("Bot: Thank you for chatting with us. Have a great day!")
        break

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= system_prompt + f"\nUser Query: {user_input}"
    )

    print("Bot:", response.text)
