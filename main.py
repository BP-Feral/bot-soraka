import discord
from discord import app_commands
import os
import time
import platform
from colorama import Back, Fore, Style
from keep_alive import keep_alive

bot_token = os.environ['bot_token']


class aclient(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents().all(),
                     maxShards='auto',
                     restMode=True)

  async def on_ready(self):
    prfx = (Back.BLACK + Fore.GREEN +
            time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET +
            Fore.WHITE + Style.BRIGHT)
    print(prfx + " Logged in as " + Fore.YELLOW + client.user.name)
    print(prfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
    print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
    print(prfx + " Python Version " + Fore.YELLOW +
          str(platform.python_version()))
    synced = await tree.sync()
    print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced)) +
          " Commands")


client = aclient()
tree = app_commands.CommandTree(client)


@client.event
async def on_message(message):
  if message.author.id == 268746806521888768:
    if message.content[0:18] == ("give me info about"):
      users = message.content[19:].split(',')
      await message.reply(f"I found this users at ")
      for user in users:
        await message.channel.send("https://www.op.gg/summoners/eune/" +
                                   str(user).replace(" ", "%20"))

    if message.content == "can you please sync commands?" or message.content == "sync commands":
      synced = await tree.sync()
      print(" Slash CMDs Synced " + str(len(synced)) + " Commands")
      await message.reply(f"synced {str(len(synced))} commands.")


@tree.command(name="test", description="testing")
async def test(interaction: discord.Interaction):
  await interaction.response.send_message(f"Hello! I am still working!")


@tree.command(name="version", description="Check bot version")
async def version(interaction: discord.Interaction):
  await interaction.response.send_message("Current bot version 0.0.1-alpha")


@tree.command(name="sum", description="add 2 numbers")
async def badge(interaction: discord.Interaction, first: int, second: int):
  await interaction.response.send_message(
    f"The sum of {first} and {second} is {first + second}")


@tree.command(name="anothercommand", description="another command")
async def anotherCommand(interaction: discord.Interaction):
  await interaction.response.send_message("this one works too")

client.run(bot_token)
