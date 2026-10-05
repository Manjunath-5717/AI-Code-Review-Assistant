# AI Code Review Assistant

An AI-powered code review application that analyzes source code for bugs, security issues, code quality, and possible improvements using the Google Gemini API.

## Features

- Select a programming language
- Submit source code for AI review
- Identify bugs and potential errors
- Analyze security issues
- Review code quality and best practices
- Get practical improvement suggestions
- Generate improved code using AI
- Preserve the selected programming language
- Handle API failures gracefully

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- python-dotenv

## How It Works

User
↓
Select Programming Language
↓
Paste Source Code
↓
Streamlit Application
↓
Prompt + Source Code
↓
Google Gemini API
↓
AI Code Analysis
↓
Review Results
↓
Generate Improved Code

## Review Categories

### Summary
Provides a short overview of the submitted code.

### Bugs and Errors
Identifies potential syntax, runtime, and logical errors.

### Security Issues
Identifies possible security vulnerabilities and unsafe coding practices.

### Code Quality
Analyzes readability, naming, structure, maintainability, and best practices.

### Improvements
Provides practical suggestions to improve the code.

### Suggested Fix
Generates an improved version of the code while preserving the selected programming language.

## Installation

### 1. Clone the Repository

git clone https://github.com/Manjunath-5717/AI-Code-Review-Assistant.git

### 2. Open the Project

cd AI-Code-Review-Assistant

### 3. Create a Virtual Environment

python -m venv venv

### 4. Activate the Virtual Environment

For Windows PowerShell:

.\venv\Scripts\Activate.ps1

### 5. Install Required Packages

pip install streamlit google-genai python-dotenv

## API Key Configuration

This project uses the Google Gemini API.

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

Never share or upload your API key to GitHub.

The .env file is excluded from Git using .gitignore.

## Run the Application

After activating the virtual environment, run:

streamlit run app.py

The application will be available at:

http://localhost:8501

## Project Structure

AI-Code-Review-Assistant/
│
├── app.py
├── .gitignore
├── README.md
└── venv/

## Limitations

- AI-generated suggestions may not always be completely correct.
- The application reviews the code provided by the user.
- It does not perform complete project-wide static analysis.
- Generated code should be reviewed and tested before production use.

## Future Improvements

- Support for multi-file projects
- Static code analysis integration
- Automated test generation
- Review history
- User authentication
- Public cloud deployment

## Author

Manjunath A R

Java Full Stack Developer | AI Application Development
