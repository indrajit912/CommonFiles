import platform, subprocess, os

def open_file(file_path, in_browser=False):
    """
    Opens a file using the default system application or web browser.

    Parameters:
        file_path (str): The path to the file to be opened.
        in_browser (bool, optional): If True, open the file's parent directory in the web browser (if applicable).

    Raises:
        OSError: If the operating system is not recognized or supported.

    Examples:
        >>> open_file('document.pdf')
        >>> open_file('image.png', in_browser=True)
    """
    current_os = platform.system()
    if current_os == "Windows":
        os.startfile(file_path if not in_browser else file_path.parent)
    else:
        if current_os == "Linux":
            commands = ["xdg-open"]
            file_path = file_path if not in_browser else file_path.parent
        elif current_os.startswith("CYGWIN"):
            commands = ["cygstart"]
            file_path = file_path if not in_browser else file_path.parent
        elif current_os == "Darwin":
            commands = ["open"] if not in_browser else ["open", "-R"]
        else:
            raise OSError("Unable to identify your operating system...")
        commands.append(file_path)
        subprocess.Popen(commands)
