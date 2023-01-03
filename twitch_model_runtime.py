import markovify
import json
from twitchio.ext import commands
from Constants import TOKEN

# Open Markov Chain Text Model
with open("Radian_Text_Model.json", "r") as json_import_file:
    reconstituted_model = markovify.NewlineText.from_json(json.load(json_import_file))



class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=TOKEN, prefix='?', initial_channels=['akiwoo'])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')
        
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
        await ctx.send(f'Hello {ctx.author.name}!')


    @commands.command(name="markov")
    async def markov(self, ctx: commands.Context):
        args = ctx.message.content.split(" ")
        
        # Generates markov chat using word in argument as starting point
        if len(args) >= 2:
            # Error is thrown if provided starting word has never been used before
            try:
                generated_message = reconstituted_model.make_sentence_with_start(args[1], strict=False)
            except KeyError:
                generated_message = f"(Radian has never used the word '{args[1]}' in chat) Sadge"

        # Generates markov chain without starting state
        else:
            generated_message = reconstituted_model.make_sentence()

        await ctx.send(generated_message)

bot = Bot()
bot.run()