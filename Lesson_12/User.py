class User:
    def __init__(self, role):
        self.role = role

def check_access(func):
    def wrapper(self, user):
        if func(self, user):
            print("Разрешено!")
            return True
        else:
            print("Запрещено!")
            return False
    return wrapper

class Policy:

    @check_access
    def view_data(self, user):
        return user.role in ['admin', 'reader']

    @check_access
    def edit_data(self, user):
        return user.role in ['admin']

admin = User('admin')
reader = User('reader')

policy = Policy()

policy.view_data(admin)
policy.edit_data(admin)
policy.view_data(reader)
policy.edit_data(reader)