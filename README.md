## wofi-scripts
Scripts for wofi, a wayland compatible program launcher.

## Installation

- clone anywhere
- (optional) assign hotkey via sway config file


## Scripts

### Window switcher (windows.py)

Python based, fast window switcher.

- Extracts normal and floating windows from the json tree returned by swaymsg.
- Wofi selection is done without appending the id of the window to the window name, providing a cleaner interface.
- The JSON tree is parsed in python without jq, vastly improving the scripts performance, especially on laptops running in battery mode.

### SSH session launcher (ssh.py)

Python based, fast and very simple ssh launcher.

- Extracts ssh hosts from .ssh/config
- Directly starts the ssh session
- You need to state your terminal command
- With termite you would call the script like this:

		'./ssh.py "termite -e"

## Dependencies

- python3
- wofi

## Version History

#### 0.2
- Adds ssh launcher

#### 0.1
- Initial version
- Window switcher