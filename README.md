# OGG to MP3 Converter

This is a simple Python script that allows users to convert audio files from the OGG format to MP3.

## Requirements

- Python 3.x
- `ffmpeg`
- `pydub`

## Setup and Installation

1. **Clone the repository**
   
   ```bash
   git clone git@github.com:maglez81/ogg-mp3.git
   cd ogg-mp3
   ```

2. **Setting up a virtual environment**

   ```bash
   virtualenv env
   source env/bin/activate
   ```

   Note: On Windows, the activation command might be different, such as `env\Scripts\activate`.

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```


4. **Ensure `ffmpeg` is installed**

   If you're on a Debian/Ubuntu system, you can install it with:

   ```bash
   sudo apt install ffmpeg
   ```
   If you're on a Macos system, you can install it with:

   ```bash
   brew install ffmpeg
   ```

## Usage

Run the script using:

```bash
python main.py
```

You'll be prompted to enter the name of the `.ogg` file you wish to convert, and then the desired name for the resulting `.mp3` file.
