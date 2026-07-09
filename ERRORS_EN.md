**Error Code List and Troubleshooting Guide for "MaterialYou-from-awww"**

If the program closed before completing its task and displayed the message "Please refer to the information on GitHub or in the ERRORS_EN.md file to troubleshoot the program," it means an error occurred at some point. Find your error code below and try the solutions to restore the program's functionality

=============================================================================================================================================================

**ERROR-000**

* Cause: The awww utility is not working correctly and failed to retrieve information about your PC's monitors
* Solution:
    1. Check if the ```awww``` program is installed
    2. Make sure you didn't accidentally install an old version of ```swww``` (it is deprecated by the developers and no longer supported by this program)
    3. Ensure that the ```awww-daemon``` is up and running on your PC
    4. Try running the ```awww query``` command manually in the terminal and verify that it lists all your monitors

**ERROR-001**

* Cause: The script successfully identified your monitor but could not locate your wallpaper
* Solution:
    1. Check if a wallpaper has been set on your PC via ```awww```
    2. Try running the ```awww query``` command manually in the terminal and verify that it outputs the correct path to your wallpaper
    3. Ensure that the wallpaper path is valid (contains no special characters, unexpected spaces, or unusual symbols)

**ERROR-002**

* Cause: Pywal failed to generate a color scheme for further use
* Solution:
    1. Check if the ```pywal``` program is installed
    2. Verify if pywal can be launched via the console: run the ```wal``` command and ensure you get the usage instructions rather than an error

**ERROR-003**

* Cause: The script could not find the required files to extract the configurations
* Solution:
    1. Check if the folder at ```~/.cache/wal/``` exists. If it is empty, try to find where the files are being saved, or contact me so we can solve this issue together
    2. If your config files are stored in a non-standard location, update the path in the code by changing ```cache_wal_dir = Path.home() / ".cache" / "wal"``` to your custom location.