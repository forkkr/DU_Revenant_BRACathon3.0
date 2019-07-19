from Database.database import db


# def save_login_info(data):
#     user_id = db.users.insert_one(data).inserted_id
#     return user_id

def validatioin(data):
    user = db.users.find_one({'username': data['username']})
    if user == None:
        return False, user
    else:
        return False,  user


def save_register_info(data):
    print(data)
    return
