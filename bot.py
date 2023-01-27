from random import randint, choice

import discord

import requests

from discord.ext import commands

from youtube_dl import YoutubeDL


from Config import token, FFMPEG_OPTIONS, YDL_OPTIONS, prefix

from brain import hello, bot_answer, what_do_you_can, bye, bye_answer


bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.default().all())

bot.remove_command('help')


@bot.command()
async def play(ctx, url):
    vc = await ctx.message.author.voice.channel.connect()

    with YoutubeDL(YDL_OPTIONS) as ydl:
        if 'https://' in url:
            info = ydl.extract_info(url, download=False)
        else:
            info = ydl.extract_info(f'ytsearch:{url}', download=False)['entries'][0]

    link = info['formats'][0]['url']

    vc.play(discord.FFmpegPCMAudio(executable='ffmpeg\\ffmpeg.exe', source=link, **FFMPEG_OPTIONS))


@bot.command()
async def roll(ctx):
    await ctx.send(randint(0, 100))


@bot.command()
async def question(ctx, *, argum: str):
    answer = wiki(argum)
    if answer != "":
        await ctx.send(answer)
        return
    await ctx.send("В моих базах нет этих данных")


@bot.event
async def on_message(message):
    msg = message.content.lower()
    if msg in hello:
        await message.channel.send(choice(bot_answer))

    if msg in what_do_you_can:
        await message.channel.send("Глупый человек напиши /help, и не лезь ко мне с глупыми вопросами")

    elif msg == "что ты можешь megatron?":
        await message.channel.send("Могу вычислить тебя по IP и стереть!!!Напиши /help и узнаешь что я еще могу сделать с тобой")

    if msg in bye:
        await message.channel.send(choice(bye_answer))

    await bot.process_commands(message)


def wiki(question):
    api_url = "https://7012.deeppavlov.ai/model"
    data = {'question_raw': [question]}
    res = requests.post(api_url, json=data).json()
    return res[0][0]


@bot.command()
async def help(ctx):
    emb = discord.Embed(title="Список команд")
    emb.add_field(name="{}roll".format(prefix),value="Бот выберет случайное число от 0 до 100")
    emb.add_field(name="{}question".format(prefix), value="Задайте вопрос боту (прим:Что такое плазма?)")
    emb.add_field(name="{}play".format(prefix), value="Включите музыку с YouTube , вставьте ссылку на песню")
    emb.add_field(name="Привет megatron", value="Бот поприветствует вас")
    emb.add_field(name="Пока megatron", value="Бот попрощается с вами")
    await ctx.send(embed=emb)

bot.run(token)
