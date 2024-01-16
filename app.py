from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
generator = pipeline('text-generation', model = 'gpt2') 

@app.route('/gpt-action', methods=['POST'])
def gpt_action():
	data = request.json  # Extract JSON data from the request
	prompt = data.get("message","")    
	gpt_response = generator(prompt, max_length = 50, num_return_sequences=1)  # Pass the data to the function
	return jsonify({"message": "GPT Model Response", "response": gpt_response[0]["generated_text"]})

if __name__ == '__main__':
    app.run(debug=True)
