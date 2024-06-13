#main.py 
from flask import Flask, render_template, send_file, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
from roboflow import Roboflow

from inference_sdk import InferenceHTTPClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

def tarama(file):

    
    rf = Roboflow(api_key="bas1rIpS23k1bWt2XR8q")
    project = rf.workspace().project("cicekler-mys3e")
    model = project.version(25).model
    model.predict(file, confidence=40, overlap=30).save("static/files/prediction.jpg")





class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file

        # Save the file to the upload folder
        uploaded_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
        file.save(uploaded_file_path)

        # Perform prediction using the uploaded file
        tarama(uploaded_file_path)

        return render_template('result.html', prediction_image='files/prediction.jpg')

    return render_template('index.html', form=form)

@app.route('/show_result')
def show_result():
    return send_file('static/files/prediction.jpg', mimetype='image/jpeg')


# ÇİÇEKLERİN SAYFALARI

@app.route('/gala-cicegi')
def galaCicegi():
    return render_template("gala-cicegi.html")

@app.route('/lale')
def Lale():
    return render_template("lale.html")

@app.route('/orkide')
def Orkide():
    return render_template("orkide.html")

@app.route('/papatya')
def Papatya():
    return render_template("papatya.html")

@app.route('/menekse')
def Menekse():
    return render_template("menekse.html")

@app.route('/levisya')
def Levisya():
    return render_template("levisya.html")

@app.route('/karanfil')
def Karanfil():
    return render_template("karanfil.html")

@app.route('/lavanta')
def Lavanta():
    return render_template("lavanta.html")

@app.route('/ortanca')
def Ortanca():
    return render_template("ortanca.html")

@app.route('/kokina')
def Kokina():
    return render_template("kokina.html")

@app.route('/zambak')
def Zambak():
    return render_template("zambak.html")

@app.route('/gul')
def Gul():
    return render_template("gul.html")

@app.route('/aycicegi')
def Aycicegi():
    return render_template("aycicegi.html")

@app.route('/iris-cicegi')
def irisCicegi():
    return render_template("iris-cicegi.html")

@app.route('/nergis')
def Nergis():
    return render_template("nergis.html")

@app.route('/nilufer')
def Nilufer():
    return render_template("nilufer.html")

@app.route('/anemon-cicegi')
def AnemonCicegi():
    return render_template("anemon-cicegi.html")

@app.route('/antoryum-cicegi')
def AntoryumCicegi():
    return render_template("antoryum-cicegi.html")

@app.route('/kadife-cicegi')
def KadifeCicegi():
    return render_template("kadife-cicegi.html")

@app.route('/kupeli-cicegi')
def KupeliCicegi():
    return render_template("kupeli-cicegi.html")

@app.route('/petunya')
def Petunya():
    return render_template("petunya.html")

@app.route('/sakayik')
def Sakayik():
    return render_template("sakayik.html")

@app.route('/yildiz-cicegi')
def YildizCicegi():
    return render_template("yildiz-cicegi.html")


if __name__ == '__main__':
    app.run(debug=True)
