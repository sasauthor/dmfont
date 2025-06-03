from flask import Flask, render_template, request, send_from_directory, jsonify
import subprocess
import os
import uuid

def create_app():
    app = Flask(__name__, static_folder='static', template_folder='templates')

    # 초기화 스크립트 실행
    def run_startup_scripts():
        subprocess.run(["python", "program1.py"], check=True)
        subprocess.run(["python", "program2.py"], check=True)

    run_startup_scripts()

    @app.route('/')
    def index():
        return render_template('index.html', examples=[])

    @app.route('/generate', methods=['POST'])
    def generate():
        text = request.form.get('text')
        if not text:
            return jsonify({"error": "텍스트가 없습니다."}), 400

        run_id = str(uuid.uuid4())[:8]

        subprocess.run(["python", "program3.py", "--text", text], check=True)
        subprocess.run([
            "python", "inference.py",
            "--config", "configs/infer_colab.yaml",
            "--checkpoint", "checkpoints/korean-handwriting.pth",
            "--save_dir", f"static/outputs/{run_id}"
        ], check=True)

        output_dir = f"static/outputs/{run_id}"
        if not os.path.exists(output_dir):
            return jsonify({"error": "이미지 생성 실패"}), 500

        image_files = [
            f"/{output_dir}/{f}" for f in os.listdir(output_dir)
            if f.lower().endswith('.png')
        ]

        return jsonify({"images": image_files})

    @app.route('/download/<path:filename>')
    def download_file(filename):
        return send_from_directory('static/outputs', filename, as_attachment=True)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=3000, debug=True)
