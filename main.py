from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
app = Flask(__name__)

def setup_files_folder():
      UPLOAD_FOLDER = os.path.join(os.getcwd(),'files')
      if(not os.path.isdir(UPLOAD_FOLDER)):
            os.mkdir(UPLOAD_FOLDER)
      app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['POST'])
def uploader():
      if request.method == 'POST':
            for f in request.files:
                  f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return 'file uploaded successfully'
                  
if __name__ == '__main__':
      setup_files_folder()
      app.run(debug = True)