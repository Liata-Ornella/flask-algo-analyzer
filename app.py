from flask import Flask, render_template

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return render_template('index.html')  # Renders the HTML file in templates/

if __name__ == '__main__':
    app.run(debug=True, port=3000)  # Run on http://127.0.0.1:3000
