# from dotenv import load_dotenv
# import google.generativeai as genai
# import os

# load_dotenv()
# api_key = os.environ.get("GEMINI_API_KEY")
# genai.configure(api_key=api_key)


# modle = genai.GenerativeModel("gemini-1.5-flash")
# responce = modle.generate_content(input("Type anything :"))
# print(responce.text)

from dotenv import load_dotenv
import google.generativeai as genai
import os

# Load environment variables
load_dotenv()

# Get the API key from environment variables
api_key = os.environ.get("GEMINI_API_KEY")

# Configure the Gemini API
try:
    genai.configure(api_key=api_key)
except Exception as e:
    print("Error configuring API key:", e)
    exit()

# Initialize the model
try:
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    print("Error initializing the model:", e)
    exit()

# Chatbot interaction loop
print("Welcome to the Gemini Chatbot! Type 'exit' or 'quit' to stop.")

# Conversation history
conversation_history = []

while True:
    try:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the chatbot. Goodbye!")
            break
        
        # Append user input to conversation history
        conversation_history.append({"role": "user", "parts": [user_input]})
        
        # Pass history to model
        response = model.generate_content(conversation_history)
        
        # Extract response text
        bot_response = response.text
        print("Bot:", bot_response)
        
        # Append bot response to conversation history
        conversation_history.append({"role": "model", "parts": [bot_response]})
    
    except KeyboardInterrupt:
        print("\nChatbot interrupted. Goodbye!")
        break

    except Exception as e:
        print("An error occurred:", e)
