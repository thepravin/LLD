from user import User
from userRepository import UserRepository


if __name__ == '__main__':
    user_obj = User("Pravin", 23, "pravin@gmail.com")
    user_repo = UserRepository("userDB", "root", "root")

    user_obj.get_user_info()

    user_repo.save_to_database(user_obj)