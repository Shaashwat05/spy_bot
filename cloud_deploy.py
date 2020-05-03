from firebase import firebase

firebase = firebase.FirebaseApplication("https://firebase_database_link.com/", None)



fd = open("gallery/encrypted_img.jpg", "rb")
encrypted_blob = fd.read()
fd.close()

fd = open("private_key.pem", "rb")
private_key = fd.read()
fd.close()

data ={
    'key': str(private_key),
    'image': str(encrypted_blob)
}

result = firebase.post('database_name', data)
print(result)