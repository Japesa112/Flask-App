from flask import Flask, render_template
import whisper
app = Flask(__name__)

# Load the Whisper model
model = whisper.load_model("base")
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
