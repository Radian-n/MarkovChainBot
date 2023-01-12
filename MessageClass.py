import re
import os
from config.definitions import ROOT_DIR

FILE_NAME = "Radian_n"




class ChatMessage:
    def __init__(self, raw_chat_message: str="") -> None:
        self.content = raw_chat_message


    def set_content(self, raw_chat_message) -> None:
        self.content = raw_chat_message


    def get_content(self) -> str:
        return self.content
    
    
    def __str__(self) -> str:
        return self.content


    def remove_prefix(self):
        prefix_end_index = self.content.index(": ")
        self.content = self.content[prefix_end_index+2:]  # +2 offset to slice string from ': ' onwards


    def remove_newlines(self):
        self.content = re.sub("\n", "", self.content)


    





def remove_dates(raw_text:str) -> str:
    # Removes dates from bulk text and returns bulk text
    text = re.sub("\n[0-3][0-9]\/[0-1][0-9]\/[1-2][0-1][0-9][0-9]", "", raw_text)
    return text


def split_raw_text_timestamp(raw_text:str) -> list:
    # Splits bulk text every time there is a new line followed by timestamp
    text_list = re.split("\n[0-9][0-9]:", raw_text)
    return text_list


raw_data_location = os.path.join(ROOT_DIR, "Data/RAW/" + FILE_NAME + ".txt")
f = open(raw_data_location, "r", encoding="utf8")
text = f.read()
f.close()

text_list = split_raw_text_timestamp(remove_dates(text)[4:]) # The string slice is there to remove the first colon.

cleaned_messages = []

for text in text_list:
    chat_message = ChatMessage(text)
    chat_message.remove_prefix()
    chat_message.remove_newlines()
    cleaned_messages.append(chat_message.get_content())

with open("_test-output.txt", "w", encoding="utf-8") as file:
    for message in cleaned_messages:
        file.write(message + "\n")
        
