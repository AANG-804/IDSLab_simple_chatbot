import os
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
# from dotenv import load_dotenv

# # github을 이용하는 방법
# load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client

client = OpenAI()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400

        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        response = client.chat.completions.create(model="gpt-4o-mini",
                                                  messages=[{
                                                      "role":
                                                      "user",
                                                      "content":
                                                      user_message
                                                  }],
                                                  temperature=0.7)

        bot_response = response.choices[0].message.content
        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'error': f'Failed to get response: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8543, debug=False)
