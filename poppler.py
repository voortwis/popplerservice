import logging
import os
import subprocess
import glob
from werkzeug import secure_filename
from flask import Flask, render_template, request, send_file

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

@app.route("/")
def index():
  return render_template("poppler.html")

@app.route('/thumbnail', methods = ['GET', 'POST'])
def create_thumbnail():
   if request.method == 'POST':
      f = request.files['file']

      # create a secure filename
      filename = secure_filename(f.filename)

      # save file to /static/uploads
      filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
      f.save(filepath)
      
      logging.info(filepath)

      subprocess.call("pdftoppm -f 1 -l 1 -scale-to 200 -png "+filepath+" "+filepath+".png", shell=True)
      thumbnail = glob.glob(filepath+'.png-*')

      print "Thumbnails: ",thumbnail

      try:
         return send_file(thumbnail[0])
      finally:
         os.remove(filepath)
         os.remove(thumbnail[0])

@app.route('/pdfinfo', methods = ['GET', 'POST'])
def get_pdfinfo():
   if request.method == 'POST':
      f = request.files['file']

      # create a secure filename
      filename = secure_filename(f.filename)

      # save file to TEMP FOLDER
      filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
      f.save(filepath)
      
      logging.info(filepath)

      try:
         output = subprocess.check_output("pdfinfo "+filepath, shell=True)
         return output
      finally:
         os.remove(filepath)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)
