"""
Generates a markov chain text model, and outputs it as a json file.

"""

import markovify
import json

# Training data file name
TEXT_DATA = "cleaned_messages2.txt"


# Turn data into a list
with open(TEXT_DATA, "r", encoding="utf-8") as file:
    messages = file.read()


# Generate markov text model using new line delimination
text_model = markovify.NewlineText(messages, state_size=1)


# Export text model
model_json = text_model.to_json()
with open("Radian_Text_Model.json", "w") as json_output_file:
    json.dump(model_json, json_output_file)


# #Import Json
# with open("Radian_Text_Model.json", "r") as json_import_file:
#     reconstituted_model = markovify.NewlineText.from_json(json.load(json_import_file))
# print(reconstituted_model.make_sentence())
