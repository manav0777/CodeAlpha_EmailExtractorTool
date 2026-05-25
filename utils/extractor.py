import re

import pandas as pd

from PyPDF2 import PdfReader





def extract_emails(uploaded_file):



    filename = uploaded_file.filename.lower()



    content = ""





    # TXT FILE

    if filename.endswith(".txt"):



        content = uploaded_file.read().decode(

            "utf-8",

            errors="ignore"

        )





    # CSV FILE

    elif filename.endswith(".csv"):



        content = uploaded_file.read().decode(

            "utf-8",

            errors="ignore"

        )





    # XLSX FILE

    elif filename.endswith(".xlsx"):



        df = pd.read_excel(uploaded_file)

        content = df.to_string()





    # PDF FILE

    elif filename.endswith(".pdf"):



        pdf = PdfReader(uploaded_file)



        for page in pdf.pages:



            text = page.extract_text()



            if text:

                content += text





    # EMAIL EXTRACTION

    found_emails = re.findall(

        r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",

        content

    )



    # REMOVE DUPLICATES

    return sorted(list(set(found_emails)))