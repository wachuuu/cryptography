from flask import Flask, flash, render_template

from cipher import TrithemiusCipher
from forms import DecryptingForm, EncryptingForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '661738ee921951187e5d2431e784248b'

@app.route('/', methods=['GET', 'POST'])
def main():
  enc_form = EncryptingForm()
  dec_form = DecryptingForm()
  cipher = TrithemiusCipher()

  if not (enc_form.is_submitted() or dec_form.is_submitted()):
    return render_template('mainpage.html', enc_form=enc_form, dec_form=dec_form)

  if dec_form.is_submitted():
    dec_output = cipher.decrypt(dec_form.dec_message.data, dec_form.step.data)

  if enc_form.is_submitted():
    enc_output = cipher.encrypt(enc_form.enc_message.data, enc_form.step.data)
    
  return render_template('mainpage.html', enc_form=enc_form, dec_form=dec_form, enc_output=enc_output, dec_output=dec_output)


@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(debug=True)
