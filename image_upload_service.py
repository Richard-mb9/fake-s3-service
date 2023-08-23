"""Service"""

import os


class ImageUploadService:
    """class service"""
    def __init__(self):
        pass

    def __verify_dir(self, path: str):
        if not os.path.isdir(path):
            os.mkdir(path)

    def save(self, image, bucket_name: str):
        """create folder with name equal bucket_name and save image"""
        filename = image.filename
        relative_path = f'./upload/{bucket_name}'
        self.__verify_dir(relative_path)
        image.save(os.path.join(relative_path, filename))
        return f'http://localhost:5001/image/{bucket_name}/{filename}'
