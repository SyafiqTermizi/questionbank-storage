import os
from datetime import datetime

import pypandoc
from flask import Flask, request, send_file, url_for

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    text_to_convert = request.get_json()["text"]

    output_file_name = f"{int(datetime.now().timestamp())}.odt"
    full_output_file_path = f"temp/{output_file_name}"
    pypandoc.convert_text(
        text_to_convert, "odt", "html", outputfile=full_output_file_path
    )

    bucket_name = os.environ.get("QUESTION_BUCKET_NAME")

    return {"file": url_for("get_file", file_name=output_file_name, _external=True)}


@app.route("/files/<file_name>")
def get_file(file_name):
    path = f"temp/{file_name}"
    return send_file(path, "application/vnd.oasis.opendocument.text")
