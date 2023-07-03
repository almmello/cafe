# Caffeine - Prevent Your PC From Sleeping

This is a simple application that prevents your PC from going into sleep mode when activated. It sits in your system tray and can be toggled on and off.

## Features

- Easy to use: Just click to activate or deactivate
- No installation required: Simply run the executable
- Lightweight: Uses minimal system resources

## Usage

1. Run `cafe.exe`.
2. Find the new icon in your system tray.
3. Right-click on the icon to see the options.
4. Select "Switch On" to prevent your PC from sleeping. The icon will change to indicate that Caffeine is active.
5. Select "Switch Off" to allow your PC to sleep. The icon will change back to indicate that Caffeine is inactive.

## Building from Source

### Prerequisites

- Python 3.6 or higher
- PyQt5
- PyInstaller (for creating the standalone executable)

### Steps

1. Clone this repository.
2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. (Optional) If you want to create a standalone executable, install the development dependencies:

    ```bash
    pip install -r dev-requirements.txt
    ```

4. Run the script:

    ```bash
    python cafe-script.py
    ```

5. (Optional) To create a standalone executable:

    ```bash
    pyinstaller --onefile --windowed --name cafe cafe-script.py
    ```

This will create `cafe.exe` in the `dist` directory. You can run this on any Windows system, even if Python is not installed.

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more details.
