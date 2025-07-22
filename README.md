# dlpctl

## About

This program helps us run our microbubble experiments by allowing someone to view a camera feed while controlling a DLP and function generator.

## Peripherals

The following specific peripherals are used:

### Basler Camera

- The exact model used is a Basler `acA1300-200um`.
- The [pypylon](https://github.com/basler/pypylon) library provided by Basler allows controlling and reading from the camera with the Python programming language. The [pylon driver](https://www.baslerweb.com/en/downloads/software/3032421996/) also appears to be required despite `pypylon`'s README stating otherwise.
- The camera is connected to the computer using a USB cable.

### Texas Instruments / ViALUX DLP kit

- The exact model of development kit used is Texas Instruments' `DLP Discovery 4100`.
- [ALP4lib](https://github.com/wavefrontshaping/ALP4lib/tree/master) library allows controlling the DLP with Python. The required file `alp41.dll` is provided by the [ViALUX ALP-4.1 Driver](https://www.vialux.de/transfer/Marketing/ViALUX-Download/download.html)
- The DLP development kit is connected to the computer using a USB cable.

### Agilent Function Generator

- The exact model used is an Agilent 20MHz Function / Arbitrary Waveform Generator `33220A`.
- The [PyVISA](https://github.com/pyvisa/pyvisa) library allows controlling equipment conforming to the [VISA](https://en.wikipedia.org/wiki/Virtual_instrument_software_architecture) communication protocol using Python. The function generator can be used by this library, but requires the additional installation of National Instruments' proprietary [NI-VISA](https://www.ni.com/en/support/downloads/drivers/download.ni-visa.html) drivers.
- The function generator is connected to the computer using a USB cable.

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
