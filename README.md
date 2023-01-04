# Simple Markov Chain Twitch Chat Bot


## Uses:
- https://github.com/jsvine/markovify
- https://github.com/TwitchIO/TwitchIO



## User chat history url
- https://www.twitch.tv/popout/akiwoo/viewercard/radian_n?popout=


## ISSUES:
### twitch_model_runtime.py
- make_sentence_with_start(strict=False) breaks when it selects a word at the end of the sentence (Still occurs even when single word messages are removed.)
