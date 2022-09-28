from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config["UPLOAD_PATH"] = "C:/"


@app.route("/upload_file", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file_name'):
            f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
        return render_template("upload-file.html", msg="file has been uploaded successfully")
    return render_template("upload-file.html", msg="please chose a file")


if __name__ == '__main__':
    app.run(debug=True)
