import fnmatch

def filename_matches_patterns(filename, patterns):
    """
    Checks if the given filename matches one of the patterns in the patterns list.
    
    Parameters:
        filename (str): The filename to check.
        patterns (list): List of patterns to match against the filename.
                        e.g - ["*.txt", "data_*.csv", "*.png"]
        
    Returns:
        bool: True if the filename matches one of the patterns, False otherwise.
        
    Author: Indrajit Ghosh
    Date: Sep 27, 2023
    """
    return any(fnmatch.fnmatch(filename, pattern) for pattern in patterns)
