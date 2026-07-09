"""
===============================================================================
File Name : file_service.py
Purpose   : File Management Service
===============================================================================
"""

import shutil
import os


class FileService:

    def copy_file(self, source, destination):

        shutil.copy(source, destination)

        return destination

    def move_file(self, source, destination):

        shutil.move(source, destination)

        return destination

    def delete_file(self, file_path):

        os.remove(file_path)

        return True

    def read_text(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def write_text(self, file_path, text):

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        return file_path
