from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass


class Admin(User):
    count = 0  

    def __init__(self, username):
        super().__init__(username)
        Admin.count += 1

    def login(self):
        print(f"[ADMIN LOGIN] {self.username} logged in.")

    def logout(self):
        print(f"[ADMIN LOGOUT] {self.username} logged out.")

    def delete_user(self, user):
        # simulate deleting a member
        Member.member_count -= 1
        print(f"[ADMIN ACTION] {self.username} deleted user: {user.username}")


class Member(User):
    member_count = 0  

    def __init__(self, username):
        super().__init__(username)
        Member.member_count += 1

    def login(self):
        print(f"[MEMBER LOGIN] {self.username} logged in.")

    def logout(self):
        print(f"[MEMBER LOGOUT] {self.username} logged out.")

    def view_content(self):
        print(f"[VIEW] {self.username} is viewing content.")


admin1 = Admin("admin_user")
member1 = Member("member_user1")
member2 = Member("member_user2")


admin1.login()
admin1.delete_user(member1)
admin1.logout()

member1.login()
member1.view_content()
member1.logout()


member2.login()
member2.view_content()
member2.logout()

print("Admin count:", Admin.count)
print("Member count:", Member.member_count)
