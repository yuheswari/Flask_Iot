from src import get_config
from src.User import User

#uid = User.register("yuheswari", "password", "password")
#print(uid)
try:
    User.login("yuheswari","password")
    print("Login success")
except Exception as e:
    print("Login failed",e)