# Simple Markov Chain Twitch Chat Bot


## How to:
### 1) Initial setup:

1. In the 'config' folder, create `constants.py`
2. In `constants.py` add TWITCH_TOKEN = "your token here" (use [this](https://twitchtokengenerator.com/) to generate your token)


### 2) Clean text using textparser.py:

1. You must be a moderator of the twitch channel you wish to get data from.
2. Substitute the twitch channel you moderate into *TwitchStreamerUsername* and the user's chat messages you wish to access into 
*TwitchChatterUsername*: https://www.twitch.tv/popout/TwitchStreamerUsername/viewercard/TwitchChatterUsername?popout= 
3. Within the "simplebar-content" class div's child, change "position: relative" to "position: absolute" and let the window scroll to the top of the user's chat history.
4. Ctrl + a, and then copy.
5. within Data/RAW/ create a new text file with the user's twitch name (in lowercase) as the file name. e.g: radian_n.txt (Create Data/RAW/ if it doesnt exist)
6. set the chat user's name in FILE_NAME within `definitions.py`
7. fill out the user constants at the top of the file, just below the import statements
8. Run the script and inspect the cleaned output in Data/CLEAN/


**NOTE:** This only needs to be done once, or whenever new data is added.



### 3) Generate chat model from cleaned data

1. Ensure cleaned data is accurate.
2. Ensure FILE_NAME in `definitions.py` is set to the user's name
3. run the script

**NOTE:** This only needs to be done once, or whenever new data is added.

### 4) Twitch model runtime:


Once the models have been generated:
1. in `definitions.py` add the twitch channels you wish to have the bot active in as a python list of strings. e.g. CHANNEL_LIST = ["twitch_channel_1", "twitch_channel_2", "twitch_channel_3"]
2. set any alternative aliases for the chat user models in `chatter_alt_names_dict` in `twitch_model_runtime.py`
3. run the script



## Uses:
- https://github.com/jsvine/markovify
- https://github.com/TwitchIO/TwitchIO



## User chat history url
- https://www.twitch.tv/popout/**TwitchStreamerUsername**/viewercard/**TwitchChatterUsername**?popout=


## TODO:
- Re-make textparser.py to work better
    - make FILE_NAME local to file?
    - make parser require less manual input
    - Parser currently doesnt correctly remove mod messages (i.e. danskacreme timed out <"user">)
- Add instructions to readme


## ISSUES:
### twitch_model_runtime.py
- make_sentence_with_start(strict=False) breaks when it selects a word at the end of the sentence (Still occurs even when single word messages are removed.)
- Punctuation causing issues limiting model depth? 
