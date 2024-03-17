# Audio Translation Project

This project empowers you to seamlessly break language barriers with audio translation. It converts spoken audio from any language into a human-sounding voice in your desired language, leveraging the power of speech recognition, machine translation, and text-to-speech.

## Features
- ***Multilingual Support***: Translates audio from a wide range of source languages.
- ***Natural-Sounding Output***: Generates high-quality, human-like speech in the target language.
- ***Simplified Workflow***: User-friendly process for effortless audio translation.
## Installation
### Create a Virtual Environment.
Isolate your project's dependencies from your system's global Python environment using a virtual environment. This ensures compatibility and avoids conflicts.

#### bash

``` python

python -m venv venv  # Replace "venv" with your desired environment name
source venv/bin/activate  # Activate the virtual environment (Linux/macOS)
venv\Scripts\activate.bat  # Activate on Windows
```
### Install Dependencies
Once your virtual environment is activated, install the required dependencies using pip:

#### bash

```pip install -r requirements.txt  # Replace with your requirements file path```
### Usage
#### Run the script
Execute the ***process.sh*** script, providing the following arguments:

- audiofilename.mp3: The path to the .mp3 audio file you want to translate.
- target_language: The language code (e.g., en for English, fr for French) for the desired output.
#### bash

```./process.sh audio_file.mp3 target_language```
### Output
The translated audio file will be saved as ***bark_out.wav***.

### Example
#### bash

```./process.sh greetings_in_spanish.mp3 en ```

This translates the Spanish audio file greetings_in_spanish.mp3 into English and saves the output as ***bark_out.wav***.
