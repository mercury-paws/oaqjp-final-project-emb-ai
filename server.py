from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector



app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotionDetector():
    data = request.get_json()
    text_to_analyze = data.get("text", "")

    result = emotion_detector(text_to_analyze)
    
    # Check if the dominant_emotion is None (for blank entries)
    if result.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"}), 400
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
