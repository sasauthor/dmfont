from flask import Flask, render_template, request, send_from_directory, jsonify
import subprocess
import os
import uuid

app = Flask(__name__, static_folder='static', template_folder='templates')

# 포트 3000에 Flask 실행
@app.before_first_request
def run_startup_scripts():
    subprocess.run(["python", "program1.py"])
    subprocess.run(["python", "program2.py"])

@app.route('/')
def index():
    return render_template('index.html', examples=[])

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "텍스트가 없습니다."}), 400

    # 고유 ID 생성
    run_id = str(uuid.uuid4())[:8]

    # program3.py 실행
    subprocess.run(["python", "program3.py", text])

    # inference.py 실행
    subprocess.run([
        "python", "inference.py",
        "--config", "configs/infer_colab.yaml",
        "--checkpoint", "checkpoints/korean-handwriting.pth",
        "--save_dir", f"static/outputs/{run_id}"
    ])

    # 결과 이미지 경로 추출
    image_files = os.listdir(f"static/outputs/{run_id}")
    image_files = [f"/static/outputs/{run_id}/{f}" for f in image_files if f.endswith('.png')]

    return jsonify({"images": image_files})

@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory('static/outputs', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(port=3000, debug=True)
