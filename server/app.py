from flask import Flask, request
from flask_cors import CORS
import librosa

app = Flask(__name__)

CORS(app)

_check = "617564696f5f776f726b65720a"

@app.route("/")
def testApi():
  try: 
    if request.form["_"] == _check:       
      audio = lr.ex(request.files["audio"])
      y, sr = lr.load(audio)
      onset_env = librosa.onset.onset_strength(y, sr=sr)
      tempo = lr.beat.tempo(onset_envelope=onset_env, sr=sr)
      print(tempo)

      return "looks good"
  except Exception:
      return {"msg": "err"}
  


@app.route("/test")
def testdb():
  return {'msg': 'ok'}

if __name__ == "__main__":
  app.run(port=5000, debug=True)