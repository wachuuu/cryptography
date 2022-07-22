import os

from flask import Flask, render_template
from flask_uploads import configure_uploads

from cipher import VisualCipher
from forms import DecryptForm, EncryptForm, photos

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '661738ee921951187e5d2431e784248b'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static')
configure_uploads(app, photos)

def clear_directory():
  extensions = ['.jpg', '.png', '.bmp']
  filenames = ['toencrypt', 'share1', 'share2', 'decrypted']
  for ext in extensions:
    for name in filenames:
      if os.path.exists(f'static/{name}{ext}'):
        os.remove(f'static/{name}{ext}')

@app.route('/')
def main():
  clear_directory()
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
  share1, share2 = None, None
  form = EncryptForm()
  if form.validate_on_submit():
    clear_directory()
    filename = photos.save(form.photo.data, name='toencrypt.')
    cipher = VisualCipher()
    (share1, share2) = cipher.encrypt(f'static/{filename}')
  return render_template('encrypt.html', form=form, file1=share1, file2=share2)

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
  output = None
  form = DecryptForm()
  if form.validate_on_submit():
    clear_directory()
    share1 = photos.save(form.photo_1.data, name='share1.')
    share2 = photos.save(form.photo_2.data, name='share2.')
    cipher = VisualCipher()
    output = cipher.decrypt(f'static/{share1}', f'static/{share2}')
  return render_template('decrypt.html', form=form, file=output)


if __name__ == '__main__':
  app.run(debug=True)
