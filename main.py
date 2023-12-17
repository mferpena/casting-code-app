from flask import Flask, request, jsonify

from html_to_css import main

app = Flask(__name__)


@app.route('/process_html', methods=['POST'])
def process_html():
    try:
        html = request.get_data(as_text=True)
        if not html:
            raise ValueError("The request must contain a \"text\" field")

        return main(html), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
