from typing import *

def is_list_of_tuple(input: Any) -> bool:
    """
    Check if the input is a list of tuples.

    Parameters
    ----------
    input : Any
        The object to be checked.

    Returns
    -------
    bool
        True if the input is a non-empty list where all elements are tuples,
        False otherwise.

    Examples
    --------
    >>> is_list_of_tuple([(1, 2), (3, 4)])
    True
    >>> is_list_of_tuple([1, 2, 3])
    False
    >>> is_list_of_tuple("not a list")
    False
    >>> is_list_of_tuple([])
    False
    """
    if not isinstance(input, list) or not input:
        return False
    return all(isinstance(item, tuple) for item in input)

def contain_all_items(my_list, items_to_check) -> bool:
    """
    Check if a list contains all items from another list.

    Args:
        my_list (list): The list to check.
        items_to_check (list): The list of items to check for.

    Returns:
        bool: True if my_list contains all items from items_to_check, False otherwise.
    """
    return all(item in my_list for item in items_to_check)

def contain_any_items(my_list, items_to_check) -> bool:
    """
    Check if a list contains all items from another list.

    Args:
        my_list (list): The list to check.
        items_to_check (list): The list of items to check for.

    Returns:
        bool: True if my_list contains all items from items_to_check, False otherwise.
    """
    return any(item in my_list for item in items_to_check)