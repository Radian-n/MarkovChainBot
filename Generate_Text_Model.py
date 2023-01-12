"""
Generates a markov chain text model, and outputs it as a json file.

"""

import os
import markovify
import json
from config.definitions import ROOT_DIR, FILE_NAME


def main():
    # Location for opening cleaned text file from textparser.py
    cleaned_data_location = os.path.join(ROOT_DIR, "Data/CLEAN/CLEAN-" + FILE_NAME + ".txt")

    # Reads data 
    with open(cleaned_data_location, "r", encoding="utf-8") as file:
        messages = file.read()
    
    # Generate markov text models
    normal_model = generate_normal_markov_model(messages)
    inverse_model = generate_inverse_markov_model(messages)

    # Generate names & relative paths for the model outputs
    normal_model_output = os.path.join(ROOT_DIR, "Models/MODELn-" + FILE_NAME + ".json")
    inverse_model_output = os.path.join(ROOT_DIR, "Models/MODELi-" + FILE_NAME + ".json")

    # Output models
    output(normal_model, normal_model_output)
    output(inverse_model, inverse_model_output)


def generate_normal_markov_model(corpus:str):
    # Generate markov text model using new line delimination
    normal_model = markovify.NewlineText(corpus, state_size=2)
    return normal_model


def generate_inverse_markov_model(corpus:str):
    # Reverse corpus string
    corpus_list = corpus.split("\n")
    corpus_rev = ""
    for line in corpus_list:
        line_rev = reversed(line.split(" "))
        corpus_rev += " ".join(line_rev) + "\n"

    # Generate inverse model from reversed corpus
    inverse_model = markovify.NewlineText(corpus_rev, state_size=2)
    return inverse_model


def output(model, output_path):
    model_json = model.to_json()
    with open(output_path, "w") as json_output_file:
        json.dump(model_json, json_output_file)
    print("output model")


main()