import os
import time
from flask import Flask, request, jsonify, render_template, send_file
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='../client/build', static_url_path='/')

# --- Mock Database ---
# This dictionary will store our fake video generation tasks
tasks = {}
PLACEHOLDER_VIDEO_URL = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"

# --- API Endpoints ---

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    """
    MOCK: This endpoint pretends to start a video generation task.
    """
    prompt = request.json.get('prompt')
    print(f"Received prompt: '{prompt}'. Starting MOCK generation.")
    
    # Create a fake task ID using the current time
    task_id = f"mock_{int(time.time())}"
    
    # Store the fake task's start time in our "database"
    tasks[task_id] = {"start_time": time.time()}
    
    return jsonify({"taskId": task_id})


@app.route('/api/status/<taskId>', methods=['GET'])
def status(taskId):
    """
    MOCK: This endpoint checks the status of our fake task.
    """
    task = tasks.get(taskId)

    if not task:
        return jsonify({"error": "Task not found"}), 404

    # SIMULATE a 5-second processing time
    processing_time = 5 
    current_time = time.time()
    
    if current_time - task["start_time"] < processing_time:
        # If it hasn't been 5 seconds yet, pretend we're still processing
        print(f"Task {taskId} is still processing...")
        return jsonify({"status": "processing"})
    else:
        # If 5 seconds have passed, return the placeholder video
        print(f"Task {taskId} is complete. Returning placeholder video.")
        return jsonify({
            "status": "completed",
            "videoUrl": PLACEHOLDER_VIDEO_URL
        })

if __name__ == '__main__':
    app.run(debug=True, port=5001)