from flask import Flask, render_template, request
import subprocess


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    if request.method == 'POST':
        try:
            script_path='C:/Users/Administrator/Downloads/face_detection/face_detection/facedetect.py'
            result = subprocess.run(['python', script_path], capture_output=True, text=True)
            # result = subprocess.run(['/usr/bin/python3', 'facedetect.py'], capture_output=True, text=True, stderr=subprocess.PIPE)

            output = result.stdout
            return render_template('index.html', output=output)
        except Exception as e:
            return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)



