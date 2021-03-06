from flask import Flask, request
from flask_cors import CORS
from PIL import Image
import librosa
import librosa.display
import os
import matplotlib.pyplot as plt

app = Flask(__name__)

CORS(app)

_check = "617564696f5f776f726b65720a"

@app.route("/")
def testApi():
  try: 
    if request.form["_"] == _check:  
      print("worker: Valid check")
      audio = request.files["audio"]
      fileName, content_type, length = audio.filename, audio.content_type, audio.content_length
      
      out = {"fileName": fileName, "content_type": content_type, "length": length}
      
      print("worker: Saving mp3 locally")
      request.files["audio"].save(os.path.join(os.getcwd(), fileName))

      print("worker: Loading for analysis")
      y, sr = librosa.load(fileName, sr=None)
      # onset_env = librosa.onset.onset_strength(y, sr=sr)
      # print("worker: Determining BPM")
      # out["bpm"] = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0]

      print("worker: Creating waveform")
      fig, ax = plt.subplots(nrows=1, figsize=(16,9), sharex=True, sharey=True)
      ax.set_xticks([])
      ax.set_yticks([])
      ax.set_yticklabels([])
      ax.set_xticklabels([])
      ax.tick_params(left = False, right = False, top = False, labeltop = False, labelright = False, labelleft = False, labelbottom = False, bottom = False)
      librosa.display.waveplot(y, sr=sr)
      
      print("worker: Saving waveform")
      fig.savefig(os.path.join(os.getcwd(), fileName) + "_waveform.png")

      # print("worker: Removing files")
      # os.remove(os.path.join(os.getcwd(), fileName) + "_waveform.png")
      # os.remove(os.path.join(os.getcwd(), fileName))

      print("worker: Finishing")
      return out
    else: 
      raise Exception("_ code is incorrect in request.")
  except Exception as e:
      print(e)
      return {"msg": "error"}
  
@app.route("/test")
def testdb():
  return {'msg': 'ok'}

if __name__ == "__main__":
  app.run(port=5000, debug=True)