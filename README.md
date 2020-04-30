# wofi-scripts
Scripts for wofi, a wayland compatible program launcher

# Installation

- clone
- place anywhere
- assign hotkey via sway config file


# Scripts

## Window switcher (windows.py)

Python based, fast window switcher.

- Extracts normal windows and floating windows from the json tree returned by swaymsg
- Wofi selection is done without appending the id of the window to the window name, providing a cleaner interface
- The JSON tree is parsed in python without jq, vastly improving the scripts performance

## SSH session launcher (ssh.py)

tbd

# Dependencies

- Python3
- wofi

# Version History

### 0.1
- Initial version
- Window switcher