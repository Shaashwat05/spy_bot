from cloud_retrive import retrive
from decrypt import decrypt_blob
import cv2

#retreiving data from cloud
private_key, encrypted_image = retrive()

 #decryption
 decrypted = decrypt_blob(encrypted_image, private_key):

#Write the decrypted contents to a file
fd = open("gallery/decrypted_img.jpg", "wb")
fd.write(decrypted)
fd.close()

#display decrypted image
cv2.imshow("decrypted image", cv2.imread("gallery/decrypted_im.jpg"))
cv2.waitKey(0)

