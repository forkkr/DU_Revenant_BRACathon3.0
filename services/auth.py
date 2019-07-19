from Database.database import db


# def save_login_info(data):
#     user_id = db.users.insert_one(data).inserted_id
#     return user_id

def validation(data):
    print(data)
    user = db.users.find_one({'username': data['username']})
    if user == None:
        return False, user
    if user['rank'] != data['rank']:
        return False, None
    return True,  user


def save_register_info(data):
    # print(data)
    info = {'username': data['username'], 'password': data['password'],
            'gender': data['gender'], 'rank': data['occupation'], 'email': data['email'],
            'bday': data['birthday'], 'terms': data['terms']}
    db.users.insert_one(info)
    return

