from firebase import firebase


def dep(private_key, encrypted_blob):

    firebase = firebase.FirebaseApplication("https://firebase_database_link.com/", None)

    data ={
        'key': str(private_key),
        'image': str(encrypted_blob)
    }

    result = firebase.post('database_name', data)

    return result