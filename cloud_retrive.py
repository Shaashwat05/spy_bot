from firebase import firebase


firebase = firebase.FirebaseApplication("https://firebase_database_link.com/", None)

data = firebase.get('database_name', 'name')