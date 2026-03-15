from flask import Flask,render_template, Flask, request, redirect, url_for

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/merge',methods=['POST'])
def upload_files():
    uploaded_files=request.files.getlist['file']
    if uploaded_files.filename !="":
        uploaded_files.save(uploaded_files.filename)


if __name__=="__main__":
    app.run(debug=True)