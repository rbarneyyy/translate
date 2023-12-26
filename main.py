from flask import Flask, request, jsonify
from libretranslate import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate():
    try:
        data = request.json
        text = data.get('text', '')
        target_lang = data.get('target_lang', 'en')  # Default to English if target language is not provided

        if not text:
            return jsonify({'error': 'Text to translate is missing'}), 400

        translation = translator.translate(text, target_lang)
        return jsonify({'translation': translation})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
