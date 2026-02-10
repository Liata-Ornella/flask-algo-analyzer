from flask import Flask, request, jsonify
import time
import matplotlib
matplotlib.use("Agg")  # Makes plots work without a GUI
import matplotlib.pyplot as plt
import io
import base64

from algorithms import bubble_sort, linear_search, binary_search, nested_loops

app = Flask(__name__)

ALGORITHMS = {
    "bubble": (bubble_sort, "O(n²)"),
    "linear": (linear_search, "O(n)"),
    "binary": (binary_search, "O(log n)"),
    "nested": (nested_loops, "O(n²)")
}

@app.route("/analyze")
def analyze():
    # 1. Get query parameters
    algo_name = request.args.get("algo", "bubble")
    n = int(request.args.get("n", 500))
    steps = int(request.args.get("steps", 10))

    if algo_name not in ALGORITHMS:
        return jsonify({"error": "Invalid algorithm"}), 400

    algorithm, complexity = ALGORITHMS[algo_name]

    # 2. Run analysis
    start_time = time.perf_counter()
    algorithm(n)
    end_time = time.perf_counter()
    total_time_ms = (end_time - start_time) * 1000

    # 3. Generate a simple graph
    x = list(range(1, steps+1))
    y = [n * i for i in x]

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Steps")
    plt.ylabel("Operations")
    plt.title(f"{algo_name} complexity")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    plt.close()
    img.seek(0)
    graph_base64 = base64.b64encode(img.read()).decode()

    # 4. Return JSON
    return jsonify({
        "algo": algo_name,
        "items": n,
        "steps": steps,
        "start_time": start_time,
        "end_time": end_time,
        "total_time_ms": round(total_time_ms, 3),
        "time_complexity": complexity,
        "graph_base64": graph_base64
    })

if __name__ == "__main__":
    app.run(port=3000, debug=True)
