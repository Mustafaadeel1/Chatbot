from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import google.generativeai as genai
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please check your .env file.")

# Configure Gemini API
genai.configure(api_key=api_key)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Flask app
app = Flask(__name__)

# Route for the chatbot frontend (HTML)
@app.route("/")
def index():
    return render_template("index.html")  # Serves the HTML file

# Route to handle user input and return chatbot response
@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user's input
        user_input = request.json.get("message")
        logging.debug(f"User input received: {user_input}")
        if not user_input:
            return jsonify({"response": "Please provide a valid input."})
        
        # Generate response from Gemini API
        gemini_response = model.generate_content(user_input)
        logging.debug(f"Gemini API response: {gemini_response}")
        
        # Safely get response text
        bot_response = gemini_response.text if hasattr(gemini_response, "text") else "No response generated."

        return jsonify({"response": bot_response})
    except Exception as e:
        # Log the error
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({"response": f"An error occurred: {str(e)}"})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)