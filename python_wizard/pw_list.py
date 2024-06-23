from typing import List, Literal, Union, Any, Tuple


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