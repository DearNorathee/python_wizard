from typing import List, Literal, Union, Any, Tuple
from typing import *

def flatten(list_of_lists):
    # imported from "C:\Users\Heng2020\OneDrive\Python NLP\NLP 08_VocabList\VocatList_func01.py"
    """Flatten a 2D list to 1D"""
    return [item for sublist in list_of_lists for item in sublist]

def filter_text(input_list:List[str],start_with = "",end_with ="", contain = "", case_sensitive:bool=False) -> List[str]:
    """
    filter a list using text string
    currently only support 1 element of start_with, end_with, contain

    """
    # this is from print_col 
    # !!! TODO start_with, end_with, contain is list
    # add 2 logic options

    
    if start_with != "":
        if case_sensitive:
            out_list = [x for x in input_list if x.startswith(start_with) ]
        else:
            out_list = [x for x in input_list if x.lower().startswith(start_with.lower()) ]
        
    
    if end_with != "":
        if case_sensitive:
            out_list = [x for x in input_list if x.endswith(end_with) ]
        else:
            out_list = [x for x in input_list if x.lower().endswith(end_with.lower()) ]
    
    if contain != "":
        if case_sensitive:
            out_list = [x for x in input_list if contain in x]
        else:
            out_list = [x for x in input_list if contain.lower() in x.lower()]
    
    return out_list


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