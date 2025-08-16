# import time
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # --- Mock Database ---
# tasks = {}
# PLACEHOLDER_VIDEO_URL = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"

# # --- API Endpoints ---

# @app.route('/api/generate', methods=['POST'])
# def generate():
#     task_id = f"mock_{int(time.time())}"
#     tasks[task_id] = {"start_time": time.time()}
#     return jsonify({"taskId": task_id})

# @app.route('/api/status/<taskId>', methods=['GET'])
# def status(taskId):
#     task = tasks.get(taskId)
#     if not task:
#         return jsonify({"error": "Task not found"}), 404
    
#     if time.time() - task["start_time"] < 5:
#         return jsonify({"status": "processing"})
#     else:
#         return jsonify({
#             "status": "completed",
#             "videoUrl": PLACEHOLDER_VIDEO_URL
#         })
    
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Mock Database ---
tasks = {}
PLACEHOLDER_VIDEO_URL = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"

# --- API Endpoints ---

@app.route('/api/generate', methods=['POST'])
def generate():
    task_id = f"mock_{int(time.time())}"
    tasks[task_id] = {"start_time": time.time()}
    return jsonify({"taskId": task_id})

@app.route('/api/status/<taskId>', methods=['GET'])
def status(taskId):
    task = tasks.get(taskId)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    if time.time() - task["start_time"] < 5:
        return jsonify({"status": "processing"})
    else:
        return jsonify({
            "status": "completed",
            "videoUrl": PLACEHOLDER_VIDEO_URL
        })

# --- Add this block to run the server locally ---
if __name__ == '__main__':
    app.run(debug=True, port=5001)