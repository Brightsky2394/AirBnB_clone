#!/usr/bin/python3

"""
create a unique FileStorage instance
for the application
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
