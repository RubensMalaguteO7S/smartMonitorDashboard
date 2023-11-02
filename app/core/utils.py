from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    out = False
    if (username == "omega7") and (password == 'senhaomegasete'):
        out = True

    return out


def auth_user(user, passwd):
    out = False
    if(user == "omega7") and (passwd == 'senhaomegasete'):
        out = True

    return out
