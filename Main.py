from nextcord.ext import commands, application_checks
import nextcord
import os


alzuApp = commands.Bot( command_prefix=">>", intents=nextcord.Intents.default().all())




for alzuFile in os.listdir("./cogs"):
    if alzuFile.endswith(".py"):
        alzuApp.load_extension(f"cogs.{alzuFile[:-3]}")




if __name__=="__main__":
    alzuApp.run("your-token")
