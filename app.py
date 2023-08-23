import os
from http import HTTPStatus
from flask import Flask, request, jsonify, Response
from flask import send_file
from flask_cors import CORS
from errors import BadRequestError
from image_upload_service import ImageUploadService


def create_app():
    """create app"""
    app = Flask(__name__)
    CORS(app)

    return app


app = create_app()


@app.route('/<bucket_name>', methods=['POST'])
def create_image_store(bucket_name: int):
    """create images"""
    if 'image' not in request.files:
        raise BadRequestError('No file part')
    image = request.files['image']
    if image.filename == '':
        raise BadRequestError('No selected file')
    path = ImageUploadService().save(
        image=image,
        bucket_name=bucket_name
    )
    return jsonify({"path": path}), HTTPStatus.OK


@app.route('/image/<bucket_name>/<filename>', methods=['GET'])
def get_image(bucket_name, filename):  # pragma: no cover
    """get images"""
    path = os.path.abspath(f'upload/{bucket_name}/{filename}')
    return send_file(path)


@app.route('/image/<bucket_name>/<filename>', methods=['DELETE'])
def delete_image(bucket_name, filename):  # pragma: no cover
    """DELETE images"""
    path = os.path.abspath(f'upload/{bucket_name}/{filename}')
    try:
        os.remove(path)
    except Exception:
        print("file not found")
    return Response(status=HTTPStatus.NO_CONTENT)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
