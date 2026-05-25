from flask import Flask, render_template, request

import time

from utils.extractor import extract_emails



app = Flask(__name__)





@app.route("/", methods=["GET", "POST"])

def home():



    emails = []



    if request.method == "POST":



        uploaded_file = request.files.get("file")



        if uploaded_file:



            # Loading Delay

            time.sleep(2)



            # Extract Emails

            emails = extract_emails(uploaded_file)





    return render_template(

        "index.html",

        emails=emails

    )





if __name__ == "__main__":



    app.run()