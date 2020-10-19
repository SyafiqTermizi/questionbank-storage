import os
from datetime import datetime

import pypandoc
from flask import Flask, request
from minio import Minio
from minio.error import ResponseError, BucketAlreadyOwnedByYou, BucketAlreadyExists


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
    minio_client = Minio(
        os.environ.get("QUESTION_STORAGE_HOST"),
        access_key=os.environ.get("MINIO_ACCESS_KEY"),
        secret_key=os.environ.get("MINIO_SECRET_KEY"),
        secure=False,
    )

    try:
        minio_client.make_bucket(bucket_name)
    except BucketAlreadyOwnedByYou as err:
        pass
    except BucketAlreadyExists as err:
        pass

    minio_client.fput_object(bucket_name, output_file_name, full_output_file_path)
    return {"file": minio_client.presigned_get_object(bucket_name, output_file_name)}
