# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from financialChatbot import FinancialChatbot  # Import your FinancialChatbot class
import pandas as pd

# Create a Flask web application
app = Flask(__name__)

# Read the dataset of financial questions and answers
filepath = 'financial_questions_answers.csv'
chatbot = FinancialChatbot(filepath)  # Initialize the FinancialChatbot with the dataset

# Define a route for the home page
@app.route('/')
def index():
    # Render the index.html template
    return render_template('index.html')

# Define a route for handling user queries
@app.route('/ask', methods=['POST'])
def ask():
    # Retrieve the user's input from the request
    user_input = request.form['messageText']
    print("User Input:", user_input)

    # Get the chatbot's response based on the user's input
    response = chatbot.get_response(user_input)

    # Return the chatbot's response in JSON format
    return jsonify({'answer': response})

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
