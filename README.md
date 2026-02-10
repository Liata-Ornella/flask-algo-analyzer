Flask Algorithm Analyzer

A Flask-based REST API that analyzes the time complexity of common algorithms, visualizes their performance, and returns execution metrics along with a Base64-encoded graph.

This project was built as part of a backend engineering assignment to demonstrate:

Flask API development

Algorithm time complexity analysis

Data visualization with Matplotlib

JSON-based API responses

Features

Analyze algorithm performance using configurable input sizes

Supported algorithms:

Bubble Sort

Linear Search

Binary Search

Nested Loops

Measure execution time dynamically

Generate and return a performance graph

Encode graph image as Base64 and include it in the API response

Technologies Used

Python 3

Flask

NumPy

Matplotlib

Project Structure
flask-algo-analyzer/
│
├── app.py              # Main Flask application
├── venv/               # Virtual environment (not committed)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (optional)

Installation & Setup
Clone the repository
[git clone ](https://github.com/Liata-Ornella/flask-algo-analyzer/)  
cd flask-algo-analyzer

Create and activate a virtual environment

Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install flask numpy matplotlib

Running the Application
python app.py


The server will start at:

http://127.0.0.1:3000

API Documentation
Analyze Algorithm

Endpoint

GET /analyze


Query Parameters

Parameter	Type	Description
algo	string	Algorithm to analyze (bubble, linear, binary, nested)
n	int	Maximum number of elements
steps	int	Step increment for input sizes

Example Request

http://127.0.0.1:3000/analyze?algo=bubble&n=1000&steps=10

Example Response
{
  "algo": "bubble",
  "items": 1000,
  "steps": 10,
  "start_time": 5812.1234,
  "end_time": 5819.4259,
  "total_time_ms": 7.30,
  "time_complexity": "O(n²)",
  "graph_base64": "iVBORw0KGgoAAAANSUhEUgAA..."
}

Graph Output

The graph shows input size vs execution time

It is generated using Matplotlib

Returned as a Base64-encoded PNG image

Can be decoded and saved as a .png file if needed

 Time Complexity Mapping
Algorithm	Time Complexity
Bubble Sort	O(n²)
Linear Search	O(n)
Binary Search	O(log n)
Nested Loops	O(n²)
Notes

This project uses Matplotlib’s Agg backend to allow graph generation without a GUI.

Designed for development and learning purposes, not production use.

👩🏽‍💻 Author

Liata Ornella Sifa
