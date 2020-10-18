from datetime import datetime

import pypandoc
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    text_to_convert = request.get_json()["text"]

    output_file_name = f"{int(datetime.now().timestamp())}.odt"

    pypandoc.convert_text(text_to_convert, "odt", "html", outputfile=output_file_name)

    # TODO: upload output file to storage server
    return {"file": output_file_name}
