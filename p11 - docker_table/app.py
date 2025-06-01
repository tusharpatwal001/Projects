from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiplication Table</title>
</head>
<body>
    <h1>Multiplication Table Generator</h1>
    <form method="POST">
        <label for="number">Enter a number:</label>
        <input type="text" id="number" name="number" required>
        <button type="submit">Generate Table</button>
    </form>

    {% if table %}
    <h2>Multiplication Table for {{ table[0][0] }}</h2>
    <table border="1">
        <tr>
            <th>Number</th>
            <th>Multiplier</th>
            <th>Result</th>
        </tr>
        {% for num, i, result in table %}
        <tr>
            <td>{{ num }}</td>
            <td>{{ i }}</td>
            <td>{{ result }}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    {% if error %}
    <p style="color: red;">{{ error }}</p>
    {% endif %}
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    table = []
    if request.method == 'POST':
        try:
            number = int(request.form['number'])
            table = [(number, i, number * i) for i in range(1, 11)]
        except ValueError:
            return render_template_string(HTML_TEMPLATE, error="Please enter a valid integer.", table=table)

    return render_template_string(HTML_TEMPLATE, table=table)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
