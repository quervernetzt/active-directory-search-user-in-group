from typing import Union
from solution.group import Group


class Search(object):
    def __init__(self: object) -> None:
        """
        Constructor.
        """
        pass

    def is_user_in_group(self: object, user_id: str, group: Group) -> bool:
        """
        Return True if user is in the group, False otherwise.

        Parameters
        ----------
        user_id: str, required
            The user id.
        group: Group, required 
            Group to check user membership against.

        Returns
        ----------
        bool
            Returns True if user is in group, else False.
        """
        if user_id and group:
            group_name: str = group.get_name()
            #print(f"Working with user '{user_id}' and root group '{group_name}'...")
            search_result: bool = self.search_user(user_id, group)
            
            if search_result:
                return True
            else:
                return False
        else:
            #print("User or group are None / empty...")
            return False

    def search_user(self: object, user_id: str, group: Group) -> Union[bool, None]:
        """
        Recursive function to search for user in group and related subgroups.

        Parameters
        ----------
        user_id: str, required
            The user id.
        group: Group, required 
            Group to check user membership against.

        Returns
        ----------
        bool
            Returns True if user is in group, else None.
        """
        group_name: str = group.get_name()
        #print(f"Searching user '{user_id}' in group '{group_name}'...")

        if user_id in group.get_users():
            return True
        else:
            for sub_group in group.get_groups():
                result: bool = self.search_user(user_id, sub_group)
                if result is True:
                    return result
