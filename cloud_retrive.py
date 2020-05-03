from firebase import firebase

def retrive():
    firebase = firebase.FirebaseApplication("https://firebase_database_link.com/", None)

    data = firebase.get('database_name', 'name')

    private_key = data['key']

    encrypted_image = data['image']

    return private_key, encrypted_image
    