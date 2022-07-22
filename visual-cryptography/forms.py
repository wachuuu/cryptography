from flask_uploads import IMAGES, UploadSet
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import SubmitField

photos = UploadSet('photos', IMAGES)

class EncryptForm(FlaskForm):
  photo = FileField(validators=[FileAllowed(photos, 'Niepoprawny format'), FileRequired('Plik jest pusty')])
  submit = SubmitField('Rozbij')

class DecryptForm(FlaskForm):
  photo_1 = FileField(validators=[FileAllowed(photos, 'Niepoprawny format'), FileRequired('Plik jest pusty')])
  photo_2 = FileField(validators=[FileAllowed(photos, 'Niepoprawny format'), FileRequired('Plik jest pusty')])
  submit = SubmitField('Połącz')
