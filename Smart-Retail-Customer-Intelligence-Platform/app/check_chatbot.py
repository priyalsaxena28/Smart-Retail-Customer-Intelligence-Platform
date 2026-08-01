import joblib

chatbot = joblib.load("models/chatbot.pkl")

print("Type:", type(chatbot))

if isinstance(chatbot, dict):
    print("Keys:", chatbot.keys())
else:
    print("Methods:")
    print(dir(chatbot))