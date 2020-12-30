import unittest
from solution.group import Group
from solution.search import Search


class TestCasesSearch(unittest.TestCase):
    def execute_tests_is_user_in_group_none_input(self: object) -> None:
        # Arrange
        root_group: Group = Group("root_group")
        search_instance: Search = Search()

        # Act
        result: bool = search_instance.is_user_in_group("", root_group)
        result_1: bool = search_instance.is_user_in_group("user", None)
        result_2: bool = search_instance.is_user_in_group("", None)

        # Assert
        self.assertFalse(result)
        self.assertFalse(result_1)
        self.assertFalse(result_2)

    def execute_tests_is_user_in_group_user_in_root_group(self: object) -> None:
        # Arrange
        root_group: Group = Group("root_group")
        root_group.add_user("user1")
        root_group.add_user("user2")
        root_group.add_user("user3")
        search_instance: Search = Search()

        # Act
        result: bool = search_instance.is_user_in_group("user2", root_group)

        # Assert
        self.assertTrue(result)

    def execute_tests_is_user_in_group_user_in_sub_group(self: object) -> None:
        # Arrange
        root_group: Group = Group("root_group")
        root_group.add_user("user1")
        root_group.add_user("user2")
        root_group.add_user("user3")

        sub_group: Group = Group("sub_group")
        sub_group.add_user("user11")
        sub_group.add_user("user12")
        root_group.add_group(sub_group)

        search_instance: Search = Search()

        # Act
        result: bool = search_instance.is_user_in_group("user12", root_group)

        # Assert
        self.assertTrue(result)

    def execute_tests_is_user_in_group_user_in_nested_sub_group(self: object) -> None:
        # Arrange
        root_group: Group = Group("root_group")
        root_group.add_user("user1")
        root_group.add_user("user2")
        root_group.add_user("user3")

        sub_group_1: Group = Group("sub_group_1")
        sub_group_1.add_user("user11")
        sub_group_1.add_user("user12")
        sub_group_1.add_user("user13")
        root_group.add_group(sub_group_1)

        sub_group_2: Group = Group("sub_group_2")
        sub_group_2.add_user("user21")
        root_group.add_group(sub_group_2)

        sub_group_3: Group = Group("sub_group_3")
        sub_group_3.add_user("user31")
        sub_group_3.add_user("user32")
        sub_group_3.add_user("user33")
        sub_group_3.add_user("user34")
        sub_group_2.add_group(sub_group_3)

        sub_group_4: Group = Group("sub_group_4")
        sub_group_2.add_group(sub_group_4)

        sub_group_5: Group = Group("sub_group_5")
        sub_group_5.add_user("user51")
        sub_group_5.add_user("user52")
        sub_group_5.add_user("user53")
        sub_group_5.add_user("user54")
        sub_group_5.add_user("user55")
        sub_group_2.add_group(sub_group_5)

        sub_group_6: Group = Group("sub_group_6")
        sub_group_6.add_user("user61")
        sub_group_6.add_user("user62")
        sub_group_6.add_user("user63")
        sub_group_4.add_group(sub_group_6)

        sub_group_7: Group = Group("sub_group_7")
        sub_group_7.add_user("user71")
        sub_group_6.add_group(sub_group_7)

        sub_group_8: Group = Group("sub_group_8")
        sub_group_8.add_user("user81")
        sub_group_8.add_user("user82")
        sub_group_8.add_user("user83")
        sub_group_8.add_user("user84")
        sub_group_6.add_group(sub_group_8)

        search_instance: Search = Search()

        # Act
        result: bool = search_instance.is_user_in_group("user1", root_group)
        result_1: bool = search_instance.is_user_in_group("user5", root_group)

        result_2: bool = search_instance.is_user_in_group("user11", root_group)
        result_3: bool = search_instance.is_user_in_group("user15", root_group)

        result_4: bool = search_instance.is_user_in_group("user21", root_group)
        result_5: bool = search_instance.is_user_in_group("user22", root_group)

        result_6: bool = search_instance.is_user_in_group("user33", root_group)
        result_7: bool = search_instance.is_user_in_group("user38", root_group)

        result_8: bool = search_instance.is_user_in_group("user41", root_group)

        result_9: bool = search_instance.is_user_in_group("user54", root_group)
        result_10: bool = search_instance.is_user_in_group(
            "user59", root_group)

        result_11: bool = search_instance.is_user_in_group(
            "user61", root_group)
        result_12: bool = search_instance.is_user_in_group(
            "user64", root_group)

        result_13: bool = search_instance.is_user_in_group(
            "user71", root_group)
        result_14: bool = search_instance.is_user_in_group(
            "user72", root_group)

        result_15: bool = search_instance.is_user_in_group(
            "user82", root_group)
        result_16: bool = search_instance.is_user_in_group(
            "user86", root_group)

        # Assert
        self.assertTrue(result)
        self.assertFalse(result_1)

        self.assertTrue(result_2)
        self.assertFalse(result_3)

        self.assertTrue(result_4)
        self.assertFalse(result_5)

        self.assertTrue(result_6)
        self.assertFalse(result_7)

        self.assertFalse(result_8)

        self.assertTrue(result_9)
        self.assertFalse(result_10)

        self.assertTrue(result_11)
        self.assertFalse(result_12)

        self.assertTrue(result_13)
        self.assertFalse(result_14)

        self.assertTrue(result_15)
        self.assertFalse(result_16)
