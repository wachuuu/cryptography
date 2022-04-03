from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField


class EncryptingForm(FlaskForm):
  enc_message = StringField('Wiadomość')
  step = IntegerField('Klucz')
  submit = SubmitField('Zaszyfruj')

class DecryptingForm(FlaskForm):
  dec_message = StringField('Wiadomość')
  step = IntegerField('Klucz')
  submit = SubmitField('Odszyfruj')
