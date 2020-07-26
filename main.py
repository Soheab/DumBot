from discord.ext.commands import Bot, Cog, BucketType, Context, command, cooldown  # <3 Lucas
import discord
from discord.ext import commands

client = Bot(command_prefix = "!", help_command = None, description = "im a bot to make you rage lmaooooooo")
client.remove_command("help")  # need to be sure it's removed ofc.

"""
not case insensitive
most used prefix
ya see what i did there
no help command, have fun
"""


@client.event
async def on_ready():
    print("lmao hi")


@client.event
async def on_message(ctx):  # yes, we have ctx now :)
    message = await client.get_context(ctx)  # we need a message object, not ctx!
    if message.message.author.id == message.bot.user.id or ctx.author.bot:
        return
    ctx: discord.Message
    message: Context
    if ctx.content.lower().startswith("lol"):
        await message.message.channel.send("lmao, yes")
    if message.message.author.id == 670972734960042005:
        await ctx.delete()  # delete messages of annoying user. :)
    await message.bot.process_commands(ctx)


@client.command()
async def hi(ctx):
    await ctx.guild.ban(ctx.author, reason = "lmao bye")
    await ctx.send("ok bye")


class MyCog(Cog):  # extension in separate file? no need.
    def __init__(self, kekw):
        self.bot = kekw
        print("cog loaded!")

    @command()
    async def amiadmin(self, lmao):  # who calls it ctx?
        ctx = await lmao.bot.get_context(lmao.message)  # need ctx!
        if lmao.channel.permissions_for(lmao.message.author).administrator:
            await ctx.message.channel.send("no, you aren't a admin in {}".format(lmao.guild))
            return
        await ctx.message.channel.send("yes {} you are a admin here.".format(lmao.message.author))
        return

    @Cog.listener()
    async def on_command_error(self, lol, nope):
        return


def setup(kekw):
    kekw.add_cog(MyCog(kekw))


client.add_cog(MyCog(client))
client.run("NTc2ODEyNTg3Njk0Njg2MjA4.XNb8lQ.Wi23lpZ7FwIx5dmUeOkjy-1PoTU")
