from flask import Flask, request, jsonify

from html_to_css import main

app = Flask(__name__)


@app.route('/process_html', methods=['POST'])
def process_html():
    if 'text' not in request.form:
        return jsonify({'error': 'The request must contain a "text" field'}), 400

    html = request.form['text']

    print("200")
    # return jsonify({'success': main(html)}), 200
    return main(html), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
