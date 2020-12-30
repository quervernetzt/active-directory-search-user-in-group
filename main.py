from tests.tests_search import TestCasesSearch
from solution.group import Group
from solution.search import Search

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests: TestCasesSearch = TestCasesSearch()

    tests.execute_tests_is_user_in_group_none_input()
    tests.execute_tests_is_user_in_group_user_in_root_group()
    tests.execute_tests_is_user_in_group_user_in_sub_group()
    tests.execute_tests_is_user_in_group_user_in_nested_sub_group()

    ###################################
    # Demo
    ###################################
    search_instance: Search = Search()

    root_group: Group = Group("root_group")
    root_group.add_user("user1")
    root_group.add_user("user2")
    root_group.add_user("user3")

    sub_group: Group = Group("sub_group")
    sub_group.add_user("user11")
    sub_group.add_user("user12")
    root_group.add_group(sub_group)

    result: bool = search_instance.is_user_in_group("user12", root_group)
    result_1: bool = search_instance.is_user_in_group("user5", root_group)
    print(result) # -> True
    print(result_1) # -> False


