
import os
from PIL import Image
from flask import  url_for, current_app


def add_profile_pic(upload, username):
  filename = upload.filename
  
  ext_type = filename.split('.')[-1]
  # "picture. "jpg"
  storage_filename = str(username)+'.'+ext_type
  # "username. "jpg"
  filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)

  output_size = (200, 200)

  pic = Image.open(upload)
  pic.thumbnail(output_size)
  pic.save(filepath)
  return storage_filename