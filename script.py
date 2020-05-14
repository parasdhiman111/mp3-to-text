from flask import *
import speech_recognition as sr
import urllib.request
from os import path
import subprocess
import os

app = Flask(__name__)


@app.route('/')
def customer():
   return render_template('index.html')



@app.route('/speech',methods = ['POST'])
def speech():
      url=request.form['url']
      r = sr.Recognizer()
      print('Downloading file......')
      urllib.request.urlretrieve(url, 'sample.mp3')
      subprocess.call(['ffmpeg', '-i', 'sample.mp3','test.wav'])
      os.remove("sample.mp3")
      audio='test.wav'
      with sr.AudioFile(audio) as source:
          audio=r.record(source)
          print('done!')

      try:
          text = r.recognize_google(audio, language ='en-IN')
          print(text)
          os.remove('test.wav')
          return render_template('result.html',text=text)

      except Exception as e:
          print(e)



if __name__ == '__main__':
   app.run(debug = True)
