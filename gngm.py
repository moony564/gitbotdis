import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Bot Online')
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("!흫훟 명령어")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "!훟흫 명령어":
        await message.channel.send("총2개")
        await message.channel.send("!훟흫 명령어")
        await message.channel.send("!훟흫 마크1.16.5")
    if message.content == "!훟흫 마크1.16.5":
        await message.channel.send("1.16.5 버전")
        await message.channel.send("moonypgm.aternos.me")
        await message.channel.send("서버가 안열려 있을땐 관리자에게 문의하세요")
    if message.content == "!훟흫 버전":
        await message.channel.send("2.0(정식)")

client.run("ODAyMTEwNDU1NTQ3NDI4OTEy.YAqdkw.SmSX3qisp4qUSVhjV4e4DiRlo1o")
