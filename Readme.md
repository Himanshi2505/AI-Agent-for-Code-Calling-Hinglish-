# AI Agent for Cold Calling (Hinglish)

This project implements an AI-powered chatbot for cold calling in Hinglish, focusing on ERP demo scheduling, candidate interviewing, and payment follow-ups.

## Features

### Completed Features

-  Basic chatbot functionality using the Google/Gemma-2b-it model
-  Three scenario implementations: ERP Demo, Candidate Interview, Payment Follow-up
-  Text-based user input and chatbot responses
-  Basic Hinglish language mixing in responses
-  Conversation history tracking within each scenario
-  Simple error handling for invalid user inputs

### Partially Implemented Features

-  Speech-to-text functionality (implemented but may need refinement)
-  Text-to-speech functionality (implemented but may need improvements for Hinglish)
-  Hinglish language enforcement (basic implementation, needs improvement for more natural mixing)
-  Scenario-specific prompts and responses (basic implementation, needs refinement)

### Unfinished or Planned Features

-  Fine-tuning the language model on Hinglish datasets
-  Advanced natural language understanding for better context awareness
-  Integration with ERP systems for real-time demo scheduling
-  Integration with HR systems for candidate data management
-  Integration with payment gateways for real-time payment processing
-  User authentication and personalized conversation history
-  Detailed analytics and reporting on conversation outcomes
-  Multi-user support for simultaneous conversations

## Setup and Running the Project

Follow these steps to set up and run the AI Agent for Cold Calling (Hinglish) project:

1. Clone the repository

2. Create and activate a virtual environment (optional but recommended):

3. Install the required dependencies:
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt


4. Set up your environment variables:
- Create a `.env` file in the project root
- Add the following variables:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```

5. Run the main script:
python src/main.py


6. Follow the prompts to select a scenario and interact with the chatbot.

### Requirements

- Python 3.7+
- Working microphone (for speech input)
- Speakers or headphones (for audio output)

## Known Issues

- Speech recognition may cut off longer sentences
- Hinglish responses are not consistently natural

## Future Improvements

- Improve Hinglish language mixing for more natural conversations
- Enhance speech recognition accuracy and duration handling
- Implement more sophisticated conversation flow management

