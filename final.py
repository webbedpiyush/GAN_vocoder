from transformers import AutoProcessor, BarkModel
import sys

#  all arguments excluding script name
args = sys.argv[1:]
print("args: ", args)

if len(args) < 2:
    print("Error: Please provide the language code as the second argument.")
    sys.exit(1)  

# args[1] should be the language of the output
audio_filename = args[0]
language_code = args[1]
print(language_code)
# select the first two characters of the language code
first_two_chars = language_code[:2].lower(); 
# print("first_two_chars are: ", first_two_chars)

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")
voice_preset = f"v2/{first_two_chars}_speaker_6"

# print(f"Language code: {language_code}")
# print(f"First two characters (uppercase): {first_two_chars}")
# print(f"Voice preset: {voice_preset}")

# Specify the file name
filename = audio_filename+ ".txt"  # Replace with the actual file name

# Open the file in read mode
with open(filename, "r") as file:
   # Read the entire contents of the file into a string
   contents = file.read()

# Print the contents of the string
print("The contents of the file are: ", contents)


inputs = processor(contents, voice_preset=voice_preset)
audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()

import scipy

sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("bark_out.wav", rate=sample_rate, data=audio_array)
