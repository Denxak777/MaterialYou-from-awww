**Error Code List and Troubleshooting Guide for "MaterialYou-from-awww"**

If the program closed before completing its task and displayed the message "Please refer to the information on GitHub or in the ERRORS_EN.md file to troubleshoot the program," it means an error occurred at some point. Find your error code below and try the solutions to restore the program's functionality

========================================================================================

**ERROR-000**

* Cause: The awww utility is not working correctly
* Solution:
    1. Check if the ```awww``` program is installed
    2. Make sure you didn't accidentally install an old version of ```swww``` (it is deprecated by the developers and no longer supported by this program)
    3. Ensure that the ```awww-daemon``` is up and running on your PC
    4. Try running the `awww query` command manually in the terminal and make sure it outputs information

**ERROR-001**

* Cause: Pywal failed to generate a color scheme for further use
* Solution:
    1. Check if the ```pywal``` program is installed
    2. Verify if pywal can be launched via the console: run the ```wal``` command and ensure you get the usage instructions rather than an error

**ERROR-002**

* Cause: The script could not find the required files to extract the configurations
* Solution:
    1. Check if the folder at ```~/.cache/wal/``` exists. If it is empty, try to find where the files are being saved, or contact me so we can solve this issue together
    2. If your config files are stored in a non-standard location, update the path in the code by changing ```cache_wal_dir = Path.home() / ".cache" / "wal"``` to your custom location.

**ERROR-003**

* Cause: The script navigated to the specific monitor's folder (e.g., ./DP-1/) but could not find the `colors-vscode.json` file, which should have been copied there from the ```pywal``` cache
* Solution:
    1. Make sure the palette generation step via Material_You() completed successfully without throwing ERROR-001 or ERROR-002
    2. Verify that folders named after your active monitors were actually created in the project root and contain the ```colors-vscode.json``` file

**ERROR-004**

* Cause: The ```colors-vscode.json``` file exists, but Python failed to parse it (the file is empty, corrupted, or contains syntax errors that broke json.loads())
* Solution:
    1. Open the corrupted file in a text editor and check its structure
    2. Ensure your version of ```pywal``` is generating templates correctly and didn't write an empty array due to a failed generation (which can happen with extremely dark or solid-color wallpapers)

**ERROR-005**

* Cause: Python was unable to create the folder structure at ~/.vscode/extensions/materialyou_[monitor_name]/themes/
* Solution:
    1. Check the write permissions for the `.vscode` directory in your home folder. Run ```ls -la ~/.vscode``` in your terminal to ensure your current user has full write access

**ERROR-006**

* Cause: The script failed to write the final ```package.json``` manifest or the ```theme.json``` color scheme to disk, even though the folders were created successfully
* Solution:
    1. Make sure your system drive is not full
    2. Ensure the files are not locked by another process (e.g., if VS Code is running and actively locking the extension files while trying to reload the theme)

**ERROR-007**

* Cause: Python was unable to identify the Linux distribution installed on the PC
* Solution:
    1. Check your Python version and upgrade to a version higher than 3.10 if you are using an older version

**ERROR-008**

* Cause: The program was unable to execute additional functionality
* Solution:
    1. Ensure that the program was installed correctly