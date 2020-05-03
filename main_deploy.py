from image import get_image
from generate import gen
from encrypt import encrypt_blob
from cloud_deploy import dep
import cv2

# get the secret image and save it
images = get_image()
cv2.imwrite("gallery/c_im.jpg", images[0])

# generate the private and public key
gen()

# loading public key
fd = open("public_key.pem", "rb")
public_key = fd.read()
fd.close()

#loading image
fd = open("gallery/c_im.jpg", "rb")
unencrypted_blob = fd.read()
fd.close()

# encryption
encrypted_blob = encrypt_blob(unencrypted_blob, public_key)

#storing encrypted data
fd = open("gallery/encrypted_img.jpg", "wb")
fd.write(encrypted_blob)
fd.close()

#loading the private key
fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()

#deploying in firebase
result = dep(private_key, encrypted_blob)
