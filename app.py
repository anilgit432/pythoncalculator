from flask import Flask, request, render_template_string
from waitress import serve

app = Flask(__name__)

# Simple HTML form embedded directly
HTML_FORM = """
<!doctype html>
<html>
  <head><title>Calculator</title></head>
  <body>
    <h2>Simple Calculator</h2>
    <form method="post">
      <input type="number" name="a" placeholder="First number" required>
      <input type="number" name="b" placeholder="Second number" required>
      <select name="op">
        <option value="add">+</option>
        <option value="sub">-</option>
        <option value="mul">*</option>
        <option value="div">/</option>
      </select>
      <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
      <p><strong>Result: {{ result }}</strong></p>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        op = request.form["op"]
        if op == "add":
            result = a + b
        elif op == "sub":
            result = a - b
        elif op == "mul":
            result = a * b
        elif op == "div":
            result = a / b if b != 0 else "Division by zero!"
    return render_template_string(HTML_FORM, result=result)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5002)
