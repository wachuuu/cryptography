from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SubmitField, TextAreaField


class EncryptForm(FlaskForm):
  filepath = StringField('Ścieżka do pliku')
  message = TextAreaField('Wiadomość', render_kw={"rows": 20})
  debug = BooleanField('Debug', default=False)
  usebbs = BooleanField('Wykorzystaj szyfr', default=False)
  submit = SubmitField('Zaszyfruj')

class DecryptForm(FlaskForm):
  filepath = StringField('Ścieżka do pliku')
  submit = SubmitField('Odszyfruj')
  usebbs = BooleanField('Wykorzystaj szyfr', default=False)
  pfield = StringField('Szyfr - p')
  qfield = StringField('Szyfr - q')
  seedfield = StringField('Szyfr - seed')

