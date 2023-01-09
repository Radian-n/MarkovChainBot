"""
Parses a copy/pasted twitch chat text feed. Outputs text into a user defined file
"""

import os
import re
from config.definitions import ROOT_DIR, FILE_NAME


# Generates relative path for inputing raw data files: /Data/user.txt
raw_data_location = os.path.join(ROOT_DIR, "Data/RAW/" + FILE_NAME + ".txt")

# Generates a relative path for ouputting cleaned files /Data/CLEAN-user.txt
cleaned_data_location = os.path.join(ROOT_DIR, "Data/CLEAN/CLEAN-" + FILE_NAME + ".txt")


def clean_text():
    cleaned_messages = []

    # Imports raw messages
    f = open(raw_data_location, "r", encoding="utf8")
    text = f.read()
    f.close()
    text_list = text.split("6-Month Subscriber")

    # Performance can be improved by re-ordering functions?
    # Messages that are not valid become empty strings.
    # non-empty strings are added to the cleaned_messages list.
    for i in range(len(text_list)):
        text_ = text_list[i]
        new_text = remove_timestamp(text_)
        new_text = remove_username(new_text, FILE_NAME)
        new_text = remove_newlines(new_text)
        new_text = remove_date(new_text)
        new_text = remove_links(new_text)
        new_text = remove_time_out_notifs(new_text)
        new_text = remove_commands(new_text)
        new_text = remove_single_word_messages(new_text)
        new_text = remove_at_sign(new_text)
        new_text = remove_timed_out(new_text)
        if new_text != "":
            cleaned_messages.append(new_text)

    # Writes cleaned_messages to output file
    with open(cleaned_data_location, "w", encoding="utf-8") as g:
        for message in cleaned_messages:
            # print(message)
            g.write(message)
            g.write("\n")


def remove_timestamp(chat_message: str) -> str:
    output_text = re.sub("[0-9][0-9]:[0-9][0-9]", "", chat_message).strip()
    return output_text


def remove_username(chat_message: str, username: str) -> str:
    output_text = chat_message.replace(username + ": ", "")
    return output_text


def remove_date(chat_message: str) -> str:
    if bool(re.search("[0-3][0-9]/[0-1][0-9]/[2][0-1][0-9]", chat_message)):
        return ""
    return chat_message


def remove_newlines(chat_message: str) -> str:
    return chat_message.replace("\n", "")


def remove_links(chat_message: str) -> str:
    if bool(re.search("(http(s)?:\/\/)", chat_message)):
        return ""
    return chat_message


def remove_time_out_notifs(chat_message: str) -> str:
    if bool(re.search("unknown timed out", chat_message)):
        index = chat_message.find("unknown timed out")
        output_text = chat_message[:index]
        return output_text
    return chat_message


def remove_commands(chat_message: str) -> str:
    if "?m" in chat_message.lower():
        print("------- " + chat_message)
        return ""
    try:
        if (chat_message.lower()[0] == "!") or (chat_message.lower()[0] == "$"):
            return ""
    except IndexError:
        return ""
    return chat_message


def remove_single_word_messages(chat_message: str) -> str:
    if " " not in chat_message:
        print("----" + chat_message)
        return ""
    return chat_message


def remove_at_sign(chat_message:str) -> str:
    while "@" in chat_message:
        index_location = chat_message.find("@")
        if index_location == 0:
            chat_message = chat_message[1:]
        else:
            chat_message = chat_message[:index_location-1] + " " + chat_message[index_location+1:]
    return chat_message

def remove_timed_out(chat_message: str) -> str:
    if "timed out zaxthedude" in chat_message:
        mod_list = ["lasershieldvr", "danskacreme", "jimmydorry", "streamelements", "akiwoo", "radian_n", "dots"]
        for mod in mod_list:
            if mod in chat_message.lower():
                return ""
    return chat_message

clean_text()
