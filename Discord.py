import discord
from discord.ext import commands
from os import path, listdir
from random import choice
from discord import File

TOKEN = 'ТОКЕН'

bot = commands.Bot(command_prefix='>')

Kurumi = path.join(path.dirname(__file__), "Images/Kurumi/")
Kurumi_galery = [Kurumi + c for c in listdir(Kurumi)]

Violet = path.join(path.dirname(__file__), "Images/Violet/")
Violet_galery = [Violet + c for c in listdir(Violet)]

Nao = path.join(path.dirname(__file__), "Images/Nao/")
Nao_galery = [Nao + c for c in listdir(Nao)]

Aisaka = path.join(path.dirname(__file__), "Images/Aisaka/")
Aisaka_galery = [Aisaka + c for c in listdir(Aisaka)]

Koneko = path.join(path.dirname(__file__), "Images/Koneko/")
Koneko_galery = [Koneko + c for c in listdir(Koneko)]

Mirai = path.join(path.dirname(__file__), "Images/Mirai/")
Mirai_galery = [Mirai + c for c in listdir(Mirai)]

Shinoa = path.join(path.dirname(__file__), "Images/Shinoa/")
Shinoa_galery = [Shinoa + c for c in listdir(Shinoa)]


@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Hello, {author.mention}!')
    await ctx.send('Для начала работы с ботом, напишите >start')


@bot.event
async def on_ready():
    print(f'Готов приступить к работе {bot.user.name}')


@bot.command()
async def start(zxc):
    new_text = 'Можете выбрать следующих персонажей: \n 1) Куруми \n 2) Вайлет \n 3) Нао \n 4) Аисака' \
               '  \n 5)Мирай \n 6)Конеко \n 7)Шиноа'
    await zxc.channel.send(new_text)
    await zxc.message.channel.send('Если вы хотите посмотреть фотографии, напишите в чат ">Galery"'
                                   ' и цифру от одного до семи, в зависимости от того,'
                                   ' какого персонажа вы хотите увидеть')


bot.remove_command('help')


@bot.command()
async def help(ctx):
    await ctx.channel.send('Если вы хотите посмотреть фотографии, напишите в чат ">Galery"'
                           ' и цифру от одного до семи, в зависимости от того, какого персонажа выхотите увидеть')


@bot.command()
async def Galery(gl):
    new_text1 = gl.message.content
    if '1' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Kurumi_galery))))
    elif '2' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Violet_galery))))
    elif '3' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Nao_galery))))
    elif '4' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Aisaka_galery))))
    elif '5' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Mirai_galery))))
    elif '6' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Koneko_galery))))
    elif '7' == new_text1.split()[-1]:
        await gl.channel.send(file=File((choice(Shinoa_galery))))
    else:
        await gl.channel.send('Сообщение не распознано, пожалуйста повторите попытку')
        new_text = 'Можете выбрать следующих персонажей: \n 1) Куруми \n 2) Вайлет \n 3) Нао \n 4) Аисака' \
                   ' \n 5) Мирай \n 6) Конеко \n 7) Шиноа'
        await gl.channel.send(new_text)


bot.run(TOKEN)
