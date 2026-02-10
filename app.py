from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # get input from the form
        numbers = request.form.get("numbers")
        if numbers:
            try:
                # convert input string to a list of integers
                numbers_list = [int(x.strip()) for x in numbers.split(",")]
                result = {
                    "sum": sum(numbers_list),
                    "max": max(numbers_list),
                    "min": min(numbers_list)
                }
            except ValueError:
                result = "Please enter valid numbers separated by commas."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, port=3000)
