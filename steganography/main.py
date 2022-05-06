from distutils.log import error

from flask import Flask, render_template

from cipher import SteganographyCipher, StreamCipher
from forms import DecryptForm, EncryptForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '661738ee921951187e5d2431e784248b'

@app.route('/')
def main():
  return render_template('mainpage.html')

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
  form = EncryptForm()
  if form.is_submitted():
    cipher = SteganographyCipher()
    try:
      if form.usebbs.data:
        bbs = StreamCipher()
        message_cipher = bbs.encrypt(form.message.data, inputformat='str')
        (p, q, seed) = bbs.get_cipher_properties()
        output = cipher.encrypt(message_cipher, form.filepath.data, debug=form.debug.data, inputformat='bits')
        return render_template('encrypt.html', form=form, output=output, settings=f'p: {p}, q: {q}, seed: {seed}')  
      else:
        output = cipher.encrypt(form.message.data, form.filepath.data, debug=form.debug.data, inputformat='str')
        return render_template('encrypt.html', form=form, output=output)  
    except ValueError as e:
      error = str(e)
      return render_template('encrypt.html', form=form, error=error)
  return render_template('encrypt.html', form=form)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
  form = DecryptForm()
  if form.is_submitted():
    cipher = SteganographyCipher()
    try:
      if form.usebbs.data:
        bbs = StreamCipher(int(form.pfield.data), int(form.qfield.data), int(form.seedfield.data))
        ciphertext = cipher.decrypt(form.filepath.data)
        output = bbs.decrypt(ciphertext, outputformat='str')
        return render_template('decrypt.html', form=form, output=output)  
      else:
        output = cipher.decrypt(form.filepath.data)
        return render_template('decrypt.html', form=form, output=output)  
    except ValueError as e:
      error = str(e)
      return render_template('decrypt.html', form=form, error=error)
  return render_template('decrypt.html', form=form)

if __name__ == '__main__':
  app.run(debug=True)
