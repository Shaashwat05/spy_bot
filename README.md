[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg)](https://www.python.org/downloads/release/python-360/) 
# spy_bot
 It is a bot that uses **raspberry pi** and its **camera** to take secret images. To encrypt these images we use **RSA encryption** from the **crypto** library of python. We use it with **OAEP**(Optimal Assymetric Encryption Padding). After encryption with the public key, the private key and the encrypted image are stored in a **firebase** Realtime Database. These can be retrived and decrypted as per will.

### Prerequisites

What things you need to install the software and how to install them

```
cv2
numpy 
firebase
zlib
base64
time
crypto
```

## Getting Started

Download a python interpeter preferable a version beyond 3.0. Install the prerequisute libraries given above.Also, the above prerequisits may not be enough to run firebase, but they easily be identified from the errors and repectively pip install them. Replace the firebase url with proper credentials/requirements. Run the main_deploy.py file to capture an image , encrypt it, and deploy. Only after encrypting can the main_retrive.py be run, or else it will give error.

```
$ main_deploy.py

$ main_retrive.py

```

## Cloning
```bash
$ git clone https://github.com/Shaashwat05/spy_bot
```


## Built With

* [python](https://www.python.org/) - The software used

## Authors
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Profile-teal.svg)](https://www.linkedin.com/in/shaashwat-agrawal-1904a117a/)       [![Github-profile](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com/Shaashwat05)

* [**Shaashwat Agrawal**](https://github.com/Shaashwat05) 

## Acknowledgments

* Hat tip to anyone whose code was used




