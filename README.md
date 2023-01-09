# Simple Markov Chain Twitch Chat Bot


## Uses:
- https://github.com/jsvine/markovify
- https://github.com/TwitchIO/TwitchIO



## User chat history url
- https://www.twitch.tv/popout/akiwoo/viewercard/radian_n?popout=


## TODO:
- Re-make textparser.py to work better
    - make FILE_NAME local to file?
    - make parser require less manual input
    - Parser currently doesnt correctly remove mod messages (i.e. danskacreme timed out <user>)
- Add instructions to readme


## ISSUES:
### twitch_model_runtime.py
- make_sentence_with_start(strict=False) breaks when it selects a word at the end of the sentence (Still occurs even when single word messages are removed.)
