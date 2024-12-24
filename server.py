"""
This module implements a Flask application that provides an API endpoint 
for emotion detection. It accepts a POST request with a text string, processes 
the text to determine its dominant emotion using the emotion_detector function, 
and returns a JSON response with the emotion scores and the dominant emotion.
"""

from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api() -> 'Response':
    """
    Handles POST requests sent to /emotionDetector, processes the input text, 
    and returns the detected emotion scores along with the dominant emotion.
    
    Returns:
        Response: JSON response with emotion scores and the dominant emotion.
    """
    data = request.get_json()


    if not data or 'text' not in data:
        return jsonify({
            "response": "Invalid text! Please try again!"
        }), 400

    text_to_analyze = data['text']

    if not text_to_analyze:
        return jsonify({
            "response": "Invalid text! Please try again!"
        }), 400

    emotion_data = emotion_detector(text_to_analyze)
    
    return jsonify({
        "anger": emotion_data['anger'],
        "disgust": emotion_data['disgust'],
        "fear": emotion_data['fear'],
        "joy": emotion_data['joy'],
        "sadness": emotion_data['sadness'],
        "dominant_emotion": emotion_data['dominant_emotion']
    })


if __name__ == '__main__':
    """
    Starts the Flask application and runs the server on localhost:5000.
    """
    app.run(debug=True)
