
from typing import List, Literal,Union
import numpy as np

def create_year_month_list(
        start_year: int, 
        end_year: int, 
        return_type: Literal["list", "np_array"] = "list") -> Union[List[str],np.ndarray]:
    # medium tested
    """
    Generates a list of yyyymm strings or a NumPy array of yyyymm strings from start_year to end_year (inclusive).
    
    Args:
    - start_year (int): The starting year.
    - end_year (int): The ending year, inclusive.
    - return_type (Literal["list", "np_array"]): Specifies the return type of the result ("list" or "np_array").

    Returns:
    - List[str] or np.ndarray: A list or NumPy array of yyyymm formatted strings.
    """
    # Initialize an empty list to store the year-month combinations
    year_month_list = []
    
    # Iterate through each year in the range
    for year in range(start_year, end_year + 1):
        # Iterate through each month (from 1 to 12)
        for month in range(1, 13):
            # Format year and month into 'yyyymm' and append to the list
            year_month_list.append(f"{year}{month:02d}")
    
    # Return the appropriate type based on return_type
    if return_type == "list":
        return year_month_list
    elif return_type == "np_array":
        return np.array(year_month_list)

