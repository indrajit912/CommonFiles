import tempfile, shutil

_tmp_path = None

def make_temp_dir():
    """
    Create a temporary directory if it doesn't exist.

    Returns
    -------
    str
        The absolute filepath to the created temporary directory.

    Examples
    --------
    >>> make_temp_dir()
    '/path/to/temporary/directory'
    """
    global _tmp_path
    if not _tmp_path:
        _tmp_path = tempfile.mkdtemp(prefix="latexbot-tmp.")
    return _tmp_path

def rm_temp_dir():
    """
    Remove the temporary directory specified in ``_tmp_path``.
    
    Examples
    --------
    >>> rm_temp_dir()
    """
    global _tmp_path
    if _tmp_path:
        shutil.rmtree(_tmp_path)
        _tmp_path = None
