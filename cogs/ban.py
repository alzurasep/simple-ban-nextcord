from nextcord import *
from nextcord.ext import commands, application_checks
import nextcord



class __alzuBan__(commands.Cog):
    def __init__(self, client):
        self.client = client


    @slash_command(name="ban")
    @application_checks.has_permissions(ban_members=True)
    async def ban(self, ctx : Interaction, kisi: nextcord.User, sebep=None):
        if sebep:
            sebep = f"{sebep} | {ctx.user}"
        if sebep is None:
            sebep = f"Sebep Yok | {ctx.user}"

        async for Yasak in ctx.guild.bans():
            if kisi.id == Yasak.user.id:
                Mesaj = Embed(title=f"{kisi} yasaklanamiyor, cunku banli aq")
                break
        else:
            Mesaj = Embed(title=f'{kisi} yasaklandi, gule gule!')
            Mesaj.add_field(name='Admin: ', value=f"{ctx.user} ({ctx.user.id})")
            Mesaj.add_field(name='Kisi: ', value=f"{kisi} ({kisi.id})")
            await ctx.guild.ban(kisi, reason=sebep)

        await ctx.response.send_message(embed=Mesaj)





    @slash_command(name="unban")
    @application_checks.has_permissions(ban_members=True)
    async def unban(self, ctx : Interaction, kisi: nextcord.User, sebep=None):
        if sebep:
            sebep = f"{sebep} | {ctx.user}"
        if sebep is None:
            sebep = f"Sebep Yok | {ctx.user}"

        async for Yasak in ctx.guild.bans():
            if kisi.id == Yasak.user.id:
                Mesaj = Embed(title=f'{kisi} tahliye edildi!')
                Mesaj.add_field(name='Admin: ', value=f"{ctx.user} ({ctx.user.id})")
                Mesaj.add_field(name='Kisi: ', value=f"{kisi} ({kisi.id})")
                await ctx.guild.unban(kisi, reason=sebep)
                break
        else:
            Mesaj=Embed(title=f'{kisi} yasakli degil amk!')

        await ctx.response.send_message(embed=Mesaj)





def setup(client):
    client.add_cog(__alzuBan__(client))