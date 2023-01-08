"""
Generates a markov chain text model, and outputs it as a json file.

"""

import os
import markovify
import json
from config.definitions import ROOT_DIR, FILE_NAME


# Location for opening cleaned text file from textoarser.py
cleaned_data_location = os.path.join(ROOT_DIR, "Data/CLEAN/CLEAN-" + FILE_NAME + ".txt")


# Turn data into a list
with open(cleaned_data_location, "r", encoding="utf-8") as file:
    messages = file.read()


# Generate markov text model using new line delimination
text_model = markovify.NewlineText(messages, state_size=1)


# Create model output path
markov_model_output = os.path.join(ROOT_DIR, "Models/MODEL-" + FILE_NAME + ".json")

# Export text model
model_json = text_model.to_json()
with open(markov_model_output, "w") as json_output_file:
    json.dump(model_json, json_output_file)
