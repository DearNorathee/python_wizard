from typing import List, Literal, Union, Any, Tuple
import python_wizard.pw_list as pwl
import unittest
import inspect_py as inp
from inspect_py import Scalar

def test_to_front_of():
    # Test case 1: Basic functionality
    test_list = [1, 2, 3, 4, 5, 6, 7]
    actual01 = pwl.to_front_of(test_list, 5, [2, 7])
    assert actual01 == [1, 3, 4, 2, 7, 5, 6], inp.assert_message(actual01, [1, 3, 4, 2, 7, 5, 6])

    # Test case 2: Items already at the front
    test_list = [1, 2, 3, 4, 5]
    actual02 = pwl.to_front_of(test_list, 4, [1, 2])
    assert actual02 == [ 3, 1, 2, 4, 5], inp.assert_message(actual02, [3, 1, 2, 4, 5])

    # Test case 3: Reference item is the first item
    test_list = [1, 2, 3, 4, 5]
    actual03 = pwl.to_front_of(test_list, 1, [3, 5])
    assert actual03 ==  [3, 5, 1, 2, 4], inp.assert_message(actual03, [3, 5, 1, 2, 4])

    # Test case 4: Non-existent items to move
    test_list = [1, 2, 3, 4, 5]
    try:
        actual04 = pwl.to_front_of(test_list, 3, [6, 7])
    except Exception as error04:
        assert isinstance(error04, ValueError)

    # Test case 5: inplace=False
    test_list05 = [1, 2, 3, 4, 5]
    pwl.to_front_of(test_list05, 4, [1, 5], inplace=True)
    assert test_list05 == [2, 3, 1, 5, 4] , inp.assert_message(test_list05, [2, 3, 1, 5, 4])


    # # Test case 6: Reference item not in list
    try:
        pwl.to_front_of([1, 2, 3], 4, [1]), inp.assert_message(test_list, [1, 3, 4, 2, 7, 5, 6])
    except Exception as error06:
        assert isinstance(error06, ValueError)

    #  # Test case 7: Reference item is infront of items_to_move
    test_list07 = ['col1','col2','col3','col4','col5','col6']
    actual07 = pwl.to_front_of(test_list07, 'col2', ['col4','col5'])
    expect07 = ['col1','col4','col5','col2','col3','col6']
    assert actual07 == expect07 , inp.assert_message(actual07, expect07)

    #  Reference item is the back of items_to_move
    test_list08 = ['col1','col2','col3','col4','col5','col6']
    actual08 = pwl.to_front_of(test_list07, 'col5', ['col1','col2'])
    expect08 = ['col3','col4','col1','col2','col5','col6']
    assert actual08 == expect08 , inp.assert_message(actual08, expect08)

def test_to_back_of():
    # Test case 1: Basic functionality
    test_list = [1, 2, 3, 4, 5, 6, 7]
    actual01 = pwl.to_back_of(test_list, 5, [2, 7])
    assert actual01 == [1, 3, 4, 5, 2, 7, 6], inp.assert_message(actual01, [1, 3, 4, 5, 2, 7, 6])

    # Test case 2: Items already at the front
    test_list = [1, 2, 3, 4, 5]
    actual02 = pwl.to_back_of(test_list, 4, [1, 2])
    assert actual02 == [ 3, 4, 1, 2, 5], inp.assert_message(actual02, [3, 1, 2, 4, 5])

    # Test case 3: Reference item is the first item
    test_list = [1, 2, 3, 4, 5]
    actual03 = pwl.to_back_of(test_list, 1, [3, 5])
    assert actual03 ==  [1,3, 5, 2, 4], inp.assert_message(actual03, [3, 5, 1, 2, 4])

    # Test case 4: Non-existent items to move
    test_list = [1, 2, 3, 4, 5]
    try:
        actual04 = pwl.to_back_of(test_list, 3, [6, 7])
    except Exception as error04:
        assert isinstance(error04, ValueError)

    # Test case 5: inplace=True
    test_list05 = [1, 2, 3, 4, 5]
    pwl.to_back_of(test_list05, 4, [1, 5], inplace=True)
    assert test_list05 == [ 2, 3, 4, 1,5] , inp.assert_message(test_list05, [ 2, 3, 4, 1,5])


    # # Test case 6: Reference item not in list
    try:
        pwl.to_back_of([1, 2, 3], 4, [1]), inp.assert_message(test_list, [1, 3, 4, 2, 7, 5, 6])
    except Exception as error06:
        assert isinstance(error06, ValueError)

    #  # Test case 7: Reference item is infront of items_to_move
    test_list07 = ['col1','col2','col3','col4','col5','col6']
    actual07 = pwl.to_back_of(test_list07, 'col2', ['col4','col5'])
    expect07 = ['col1','col2','col4','col5','col3','col6']
    assert actual07 == expect07 , inp.assert_message(actual07, expect07)

    #  Reference item is the back of items_to_move
    test_list08 = ['col1','col2','col3','col4','col5','col6']
    actual08 = pwl.to_back_of(test_list07, 'col5', ['col1','col2'])
    expect08 = ['col3','col4','col5','col1','col2''col6']
    assert actual08 == expect08 , inp.assert_message(actual08, expect08)


def main():
    test_to_back_of()
    test_to_front_of()

if __name__ == '__main__':
    main()