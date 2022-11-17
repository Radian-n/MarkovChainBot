import re

FILE_NAME = "messages.txt"
CLEAN_NAME = "cleaned_messages.txt"
USERNAME = "Radian_n"


def main():
    cleaned_messages = []

    # Imports raw messages 
    f = open(FILE_NAME, "r", encoding="utf8")
    text = f.read()
    f.close()
    text_list = text.split("Moderator6-Month SubscriberArtist")
    

    # Performance can be improved by re-ordering functions?
    # Messages that are not valid become empty strings.
    # non-empty strings are added to the cleaned_messages list.
    for i in range(len(text_list)):
        text_ = text_list[i]
        new_text = remove_timestamp(text_)
        new_text = remove_username(new_text, USERNAME)
        new_text = remove_newlines(new_text)
        new_text = remove_date(new_text)
        new_text = remove_links(new_text)
        new_text = remove_time_out_notifs(new_text)
        # no longer removing commands because "its funny"
        # new_text = remove_commands(new_text)
        if new_text != "":
            cleaned_messages.append(new_text)


    # Writes cleaned_messages to output file
    with open(CLEAN_NAME, "w", encoding="utf-8") as g:
        for message in cleaned_messages:
            print(message)
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
    if bool(re.match("!", chat_message)):
        return ""
    return chat_message



main()