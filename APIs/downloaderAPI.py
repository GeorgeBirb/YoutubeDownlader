from flask import Flask, request, jsonify
from pytube import YouTube

app = Flask(__name__)

@app.route('/ytDownloader', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data.get('url')  # Use data.get() to avoid KeyError if 'url' is missing
    save_path = r'C:\Users\PX\Downloads'

    try:
        video = YouTube(video_url)
        stream = video.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        return jsonify({'message': 'Video downloaded successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
