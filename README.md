Overview

This project is a Q&A chatbot powered by LangChain and Ollama, providing interactive responses to user queries. The chatbot leverages Streamlit for a simple and user-friendly interface.

Features

Uses LangChain for structured conversational AI.

Integrates Ollama as the language model backend.

Provides adjustable parameters like temperature and max tokens.

Interactive Streamlit UI for an enhanced user experience.

Installation

Prerequisites

Ensure you have the following installed:

Python (>=3.8)

pip

Virtual environment (optional but recommended)

Steps

1)Clone the repository:
git clone <repo-url>
cd <repo-folder>

2)Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3)Install the dependencies:
pip install -r requirements.txt

4)Set up environment variables:
Create a .env file in the root directory and add:
LANGCHAIN_API_KEY=<your_api_key>

Usage

Run the Streamlit app using:
streamlit run apps.py
