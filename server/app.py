from flask import Flask, request
from flask_cors import CORS
import librosa
import os

app = Flask(__name__)

CORS(app)

_check = "617564696f5f776f726b65720a"

@app.route("/")
def testApi():
  try: 
    if request.form["_"] == _check:  
      audio = request.files["audio"]
      fileName, content_type, length = audio.filename, audio.content_type, audio.content_length
      
      out = {"fileName": fileName, "content_type": content_type, "length": length}
      
      request.files["audio"].save(os.path.join(os.getcwd(), fileName))

      y, sr = librosa.load(fileName, sr=None)
      onset_env = librosa.onset.onset_strength(y, sr=sr)
      tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

      out["bpm"] = tempo[0]

      return out
  except Exception as e:
      print(e)
      return {"msg": "error"}
  
@app.route("/test")
def testdb():
  return {'msg': 'ok'}

if __name__ == "__main__":
  app.run(port=5000, debug=True)