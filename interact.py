from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send():
    user_message = request.json['message']
    # This is where you'd integrate with Gemini's API
    response = gemini_api_request(user_message)
    return jsonify({'message': response})

def gemini_api_request(text):
    # Assume Gemini's API endpoint and your API key are stored correctly
    endpoint = "https://api.gemini.example.com/respond"
    headers = {'Authorization': 'Bearer your_api_key'}
    data = {'prompt': text, 'max_tokens': 150}
    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()['choices'][0]['text']
    else:
        return "Sorry, I couldn't process that request."

if __name__ == '__main__':
    app.run(debug=True)