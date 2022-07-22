# Visual crytography
Visual cryptography is a cryptographic technique which allows visual information to be encrypted in such a way that the decrypted information appears as a visual image.

### Example
#### Original image
![Image](static/toencrypt_example.png?raw=true "Original image")
<br>

#### Image after encryption
Original image is split in two decrypted images (called shares). They seem to be just a random noise.

![Image](static/share1_example.png?raw=true "Share 1")
![Image](static/share2_example.png?raw=true "Share 2")
<br>

#### Image after decryption
After conjunction of the two shares, we can see something similar to original image.

![Image](static/decrypted_example.png?raw=true "Share 2")
<br>


### Requirements
To start this app you need `Flask` and `wt-forms` libraries
```
pip install flask
pip install flask-wtf
```

### Setup
1. Run file `main.py` using Pyhhon interpreter. For example from console, like this:
```
$> python main.py
```
2. Oen your web browser and go on page:
```
http://localhost:5000/
```