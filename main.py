#pip install discord-py-interactions
import interactions

bot = interactions.Client(token="ODUwMDY5NTQzNjMxNDU0MjM5.GeUASg.4_fLlNpFWjrO18wueQ5SHImD6kbU7257Db4xLo")

@bot.event
async fef on_message():
    if message.author.name.startswith('Rioter'):
        print(f'message from {message.author.name}')

@bot.command(
    name="my_first_command",
    description="This is the first command I made!",
    # 'scope = 0000000000,' leave this blank to implement the command globally, it will take extra time to load globally
)
async def my_first_command(ctx: interactions.CommandContext):
    await ctx.send("Hi there!")


@bot.command(
    name="version",
    description="Check the current version",
    #scope=958765210871685150
)
async def version(ctx: interactions.CommandContext):
    await ctx.send("Current version is 0.1-alpha")

bot.start()
