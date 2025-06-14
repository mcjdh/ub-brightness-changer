# Brightness Changer

A simple and user-friendly GUI application for controlling monitor brightness on Linux systems using `xrandr`.

## Features

- **Easy-to-use GUI**: Clean tkinter interface with a brightness slider
- **Quick presets**: Buttons for 25%, 50%, 75%, and 100% brightness levels
- **Real-time adjustment**: Brightness changes instantly as you move the slider
- **Monitor detection**: Automatically detects your primary monitor
- **No sudo required**: Uses software-based brightness control via `xrandr`
- **Safe limits**: Prevents setting brightness too low (minimum 10%)

## Screenshots

The application provides a simple interface with:
- A brightness percentage display
- A horizontal slider for fine control
- Quick preset buttons for common brightness levels
- Monitor information display

## Requirements

- **Python 3**: The script is written in Python 3
- **tkinter**: GUI library (usually included with Python)
- **xrandr**: X11 display configuration utility (pre-installed on most Linux systems)
- **Linux/X11**: This tool is designed for Linux systems using X11

## Installation

1. Clone or download this repository:
   ```bash
   git clone https://github.com/mcjdh/ub-brightness-changer.git
   cd ub-brightness-changer
   ```

2. Make the shell script executable (optional):
   ```bash
   chmod +x brightness_changer.sh
   ```

## Usage

### Method 1: Using the shell script
```bash
./brightness_changer.sh
```

### Method 2: Running Python directly
```bash
python3 brightness_changer.py
```

### Method 3: Make it executable and run directly
```bash
chmod +x brightness_changer.py
./brightness_changer.py
```

## How It Works

This tool uses `xrandr` to control software-based brightness adjustment. Unlike hardware brightness controls that require system permissions, this method:

- Works on any monitor connected via standard display interfaces
- Doesn't require root/sudo privileges
- Provides smooth brightness transitions
- Is compatible with external monitors that may not support hardware brightness control

The application automatically detects your primary monitor and applies brightness changes in real-time.

## Troubleshooting

**"No monitor found for xrandr control!" error:**
- Ensure you're running on a system with X11 (not Wayland)
- Check that `xrandr` is installed: `xrandr --version`
- Verify your display is detected: `xrandr --listmonitors`

**Brightness doesn't change:**
- Some monitors may not respond to software brightness control
- Try using hardware brightness controls (Fn keys) instead
- Check if your graphics drivers support xrandr brightness control

**Application won't start:**
- Ensure Python 3 and tkinter are installed
- On Ubuntu/Debian: `sudo apt install python3-tk`
- On Fedora: `sudo dnf install python3-tkinter`

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.
