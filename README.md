# dlpctl

## Setup

This program must run on Windows and is tested on Windows 11 Home as well as Windows 11 IoT LTSC in a virtual machine with USB devices passed through.

1. [Download](https://www.vialux.de/transfer/Marketing/ViALUX-Download/download.html) and install the ViALUX driver for your device. We have only tested using ALP-4.1 as of right now since we only have that hardware.

2. Copy `alp41.dll` from the `C:\Program Files\ALP-4.1\ALP-4.1 high-speed API\x64` folder to this project's root folder. If you chose a non-default install location for the ViALUX driver, please check for the file there.

## Run

There are two supported methods of running the project

### a. Using uv

Astral's [uv](https://docs.astral.sh/uv/getting-started/installation/) software simplifies many tasks with developing and running Python programs.

Simply run `uv sync` in the project's root directory to setup the Python virtual environment (venv). There is no need to manually activate the venv. Simply run `uv run src/main.py` and uv will automatically use the project's venv.

### b. Using Python, pip, and venv

This method only requires a default working Python installation with no external tools.

1. Open a Power Shell prompt in the project's root directory, then run `python -m venv` to create our virtual environment (venv).

2. In the same prompt, run `.venv\Scripts\activate` to activate the venv.

3. Now, run `pip install .` to install the required dependencies into the venv.

4. Finally, you can run `python src/main.py` to start dlpctl.
