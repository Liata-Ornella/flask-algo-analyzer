Flask Algo Analyzer

A simple Flask web application that takes a list of numbers from the user, analyzes them, and displays results such as sum, maximum, and minimum. This project is meant as a beginner-friendly way to practice Flask forms, templates, and basic Python logic.

Features

Accepts a comma-separated list of numbers from the user.

Calculates and displays:

Sum

Maximum

Minimum

Shows error messages if the input is invalid.

Built using Flask and simple HTML templates.

Project Structure
flask-algo-analyzer/
│
├─ app.py                # Main Flask application
├─ .venv/                # Python virtual environment
└─ templates/
    └─ index.html        # HTML template with form

Setup

Clone the repository

git clone https://github.com/Liata-Ornella/flask-algo-analyzer.git
cd flask-algo-analyzer


Create a virtual environment (if not already)

python -m venv .venv


Activate the virtual environment

Windows (PowerShell):

& .venv/Scripts/Activate.ps1


macOS/Linux:

source .venv/bin/activate


Install dependencies

pip install Flask

Usage

Run the Flask app:

python app.py


Open your browser and go to:

http://127.0.0.1:3000/


Enter a comma-separated list of numbers in the form, for example:

1, 5, 9, 12


Click Analyze to see the results:

Sum: 27
Max: 12
Min: 1


Notes

This app runs on the Flask development server.

Do not use it as-is in production. For production, consider using a WSGI server like Gunicorn or uWSGI.

Author

Liata Ornella Sifa
GitHub: https://github.com/Liata-Ornella
