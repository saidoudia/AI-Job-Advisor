from flask import Flask, request, jsonify
from dotenv import load_dotenv
import openai
import os


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)


@app.route('/cv/analyze/', methods=['POST'])
def cv_analyze():
    cv_text = request.json.get('cv_text')
    if not cv_text:
        return jsonify({"error": "CV text is required"}), 400
    
    
    response = openai.Completion.create(
        engine="text-davinci-003",  
        prompt=f"Analyse ce CV et donne des recommandations sur les points forts et les faiblesses :\n{cv_text}",
        max_tokens=200
    )
    
    feedback = response.choices[0].text.strip()
    
    return jsonify({"feedback": feedback})


@app.route('/')
def home():
    return "Le serveur fonctionne!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

 
