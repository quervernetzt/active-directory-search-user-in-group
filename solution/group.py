class Group(object):
    def __init__(self: object, _name: str) -> None:
        self.name: str = _name
        self.groups: list = []
        self.users: list = []

    def add_group(self: object, group: 'Group') -> None:
        self.groups.append(group)

    def add_user(self: object, user: str) -> None:
        self.users.append(user)

    def get_groups(self: object) -> list:
        return self.groups

    def get_users(self: object) -> list:
        return self.users

    def get_name(self: object) -> str:
        return self.name
