from flask import send_file,Flask,render_template, Flask, request, redirect, url_for
import os
from pdf2docx import Converter

import pdf2docx

app= Flask(__name__)

app.config['UPLOAD_FOLDER']='uploads'

@app.route("/")
def home():
    return render_template("index.html")


@app.route('/merge',methods=['GET','POST'])
def upload_files():
    uploaded_files=request.files.getlist('file')
    
    merger = pydf.PdfMerger()


    for pdfs in uploaded_files:
        if pdfs.filename !="":
            path=os.path.join(app.config['UPLOAD_FOLDER'],pdfs.filename)
            pdfs.save(path)
            print("saved",path)
            print("file exists",os.path.exists(path))
            merger.append(path)

    print("writing merged pdf")
    output_path = "Merged.pdf"
    merger.write(output_path)
    print('done')
    merger.close() 

    return send_file(output_path, as_attachment=True)


@app.route('/convert_pdfs', methods= ['GET','POST'])
def convert_pdfs():
    print('inside the function')
    uploaded_file= request.files.get('file')

    if uploaded_file.filename!="":
        print("inside the if statement")
        path1 = os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
        uploaded_file.save(path1)

    outputh_path= os.path.join(app.config['UPLOAD_FOLDER'],uploaded_file.filename)
    print("after the if statement")
    cv = Converter(path1)
    cv.convert(outputh_path)

    cv.close()
    return send_file(outputh_path, as_attachment=True, download_name='converted.docx')


if __name__=="__main__":
    app.run(debug=True)