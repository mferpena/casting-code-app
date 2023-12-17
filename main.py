import json
from flask import Flask, request, jsonify

from html_to_css import main
from json_to_java import generate_java_class
from json_to_yml import convert_json_to_yaml

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


@app.route('/json_to_java', methods=['POST'])
def process_json_to_java():
    try:
        json_data = request.get_data(as_text=True)
        if not json_data:
            raise ValueError("The request must contain a \"text\" field")

        json_input = json.loads(json_data)

        java_class_generated = generate_java_class(json_input)
        return java_class_generated, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/json_to_yaml', methods=['POST'])
def process_json_to_yaml():
    try:
        json_data = request.get_data(as_text=True)
        if not json_data:
            raise ValueError("The request must contain a \"text\" field")

        yaml_output = convert_json_to_yaml(json_data)
        return yaml_output, 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
