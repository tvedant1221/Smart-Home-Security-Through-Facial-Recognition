import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("smarthomesecuritysystem.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smarthomesecuritysystem-7e9a0-default-rtdb.firebaseio.com/'
})

ref = db.reference('Authorized')

data = {
    '4848':
        {
            'name': 'Vedant Tripathi',
            'last_check_in': '10-28-2023 00:54:23'
        },
    '4001':
        {
            'name': 'Bill',
            'last_check_in': '10-28-2023 00:54:29'
        },
    '4904':
            {
                'name': 'Prashant Rai',
                'last_check_in': '10-28-2023 00:54:30'
            },
    '4905':
            {
                'name': 'Satyarth P. Srivastav',
                'last_check_in': '10-28-2023 00:54:38'
            },
    '4498':
            {
                'name': 'Rimjhim',
                'last_check_in': '10-28-2023 00:54:42'
            }
}

for key, value in data.items():
    ref.child(key).set(value)