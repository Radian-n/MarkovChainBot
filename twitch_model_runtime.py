"""
Uses the pre-generated markov text model to create messages and send them in specified twitch chat

"""
import markovify
import json
import os
from twitchio.ext import commands
from config.constants import (
    TWITCH_TOKEN,
)  # Create new Constants.py file in the config folder. Create TOKEN variable and assign twitch account token to it.
from config.definitions import ROOT_DIR, FILE_NAME, CHANNEL_LIST


chatter_alt_names_dict = {"Radian": "Radian_n",

                          "Alfa": "AlfaAnanas",
                          "Alfaananas": "AlfaAnanas", 

                          "Lazzie": "LazzieTheDino",
                          "Lazziethedino": "LazzieTheDino",
                          
                          "Zax": "Zaxthedude",
                          "ZaxTheDude": "Zaxthedude"}


def open_model(model_path):
    with open(model_path, "r") as json_in_file:
        return markovify.NewlineText.from_json(json.load(json_in_file))

def generate_model_dictionary():
    models_return = {}
    # Opens models from within the /Models/ sub-directory and add to models dict
    for filename in os.listdir(models_path):
        opened_model = open_model(models_path + filename)
        user = filename[7:].split(".")[0]
        model_type = filename[5:6]

        # For each user (i.e. Radian_n) both the normal and inverted models are added to the user's dictionary
        # The model keys are 'n' for normal model and 'i' for inverted model
        if user not in models_return:
            models_return[user] = {model_type: opened_model}
        else:
            models_return[user][model_type] = opened_model
    return models_return


def generate_text(person:str, word:str=None):
    normal_model = model_dict[person]["n"]
    inverted_model = model_dict[person]["i"]

    if word is None:
        # Generate random markov chain WITHOUT a prompt word
        print("normal model")
        print(person, word, normal_model)
        return normal_model.make_sentence()

    else:
        # normal_text = normal_model.make_sentence_with_start(word, strict=False)
        # Uses the inverted markov model to generate text before the prompt word (prefix).
        # Normal markov model generates text following prompt word (suffix).
        # Then combines the prefix and suffix to form a generate piece of text AROUND the prmopt word
        try:
            prefix_gen = inverted_model.make_sentence_with_start(word, strict=False)[len(word):]  # Remove prompt word otherwise it appears in output twice 
            prefix_gen_text = " ".join(reversed(prefix_gen.split(" "))) # Text from inverted model needs to be reversed back to normal order
            suffix_gen = normal_model.make_sentence_with_start(word, strict=False)
            word_gen = prefix_gen_text + suffix_gen
            print("inverted model")
            return word_gen
        except KeyError:  # Ugly solution to handle broken exception raising in markovify function make_sentence_with_start()
            return f"< hasn't said {word} Sadge >"


def get_chatters() -> str:
    chatter_list = ""
    for key in model_dict.keys():
        chatter_list += key + ", "
    chatter_list = chatter_list[:-2]
    return chatter_list
        


models_path = os.path.join(ROOT_DIR, "Models/")
model_dict = generate_model_dictionary()

print(model_dict)


class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=TWITCH_TOKEN, prefix="?", initial_channels=CHANNEL_LIST)

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f"Logged in as | {self.nick}")
        print(f"User id is | {self.user_id}")

    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return
        # # Print the contents of our message to console...
        # print(message.content)

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f"Hello {ctx.author.name}!")

    @commands.command(name="m")
    async def m(self, ctx: commands.Context):
        # Spilt recieved command into components
        message_content_list = ctx.message.content.split(" ")
        command = message_content_list[0][1:]
        person = message_content_list[1].capitalize()
        print(person)

        # Checks for alternative spellings
        if person in chatter_alt_names_dict.keys():
            person = chatter_alt_names_dict[person]
            print(person)

        # Checks that called model exists
        if person not in model_dict.keys():
            await ctx.send(f"{ctx.author.name} oopsies, try one of these names: {get_chatters()}")
        
        # Generate a random markov chain text
        elif len(message_content_list) == 2:
            generated_text = generate_text(person)
            await ctx.send(generated_text)

        # Generate a markov chain text using a prompt word passed from message argument [2]
        elif len(message_content_list) >= 3:
            word_prompt = message_content_list[2] 
            generated_text = generate_text(person, word_prompt)
            await ctx.send(generated_text)


    @commands.command(name="markov")
    async def markov(self, ctx: commands.Context):
        sender = ctx.author.name
        print(sender)
        await ctx.send(f"@{sender} this command has been changed to ?m <name>. Type ?help for more info ")


    @commands.command(name="help")
    async def help(self, ctx: commands.Context):
        await ctx.send("""To generate user messages: "?m <name>" or "?m <name> <word-prompt>".    To get a list of which people have had chat models generated, type "?chatters". 
                          The <word-promp> argument is kinda buggy so it sometimes doesnt work""")


    @commands.command(name="chatters")
    async def chatters(self, ctx: commands.Context):
        await ctx.send(f"Available markov models for: {get_chatters()}.")




bot = Bot()
bot.run()
