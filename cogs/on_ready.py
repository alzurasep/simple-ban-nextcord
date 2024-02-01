from nextcord import *
from nextcord.ext import commands





class __on_ready__(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print('Started')
def setup(client):
    client.add_cog(__on_ready__(client))