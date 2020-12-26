# coding=utf-8
import discord
import random

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content=="ルール":
        rulelist = ["エリア","ヤグラ"]
        await message.channel.send(random.choice(rulelist))
    if message.content=="王様":
        kinglist = ["まつちよ","しゅっち"]
        await message.channel.send(random.choice(kinglist))

#すごろくプラベ
    if message.content=="1d4":
        dicelist = ["1","2","3","4"]
        reply = message.author.name + "さんは" + random.choice(dicelist) + "が出ました!"
        await message.channel.send(reply)
    if message.content=="1d4win":
        dicelist2 = ["2","3","4","5","6","7","8"]
        reply2 = message.author.name + "さんは" + random.choice(dicelist2) + "が出ました!"
        await message.channel.send(reply2)
    if message.content=="!ura":
        uramissionlist = ["a","b","c","d","e","f","g"]
        reply3 = "裏ミッションは" + random.choice(uramissionlist) + "です!"
        await message.channel.send(reply3)
    if message.content=="!bukisyu":
        bukisyulist = ["スプラシューター、52ガロン、zap、わかば","ロング、ホット、ノヴァ、クラブラ","スプラチャージャー、リッター4kスコープ、スクイク、ソイチューバー","エクス、バケツ、洗濯機、ヒッセン","スプラローラー、カーボン、ヴァロー、ダイナモ"]
        reply4 = "武器種は" + random.choice(bukisyulist) + "です!"
        await message.channel.send(reply4)
    if message.content=="!rule":
        rulelist2 = ["エリア","ヤグラ","ホコ","アサリ","ナワバリ"]
        reply5 = "ルールは" + random.choice(rulelist2) + "です!"
        await message.channel.send(reply5)
    if message.content=="!pos":
        poslist = ["1位の後ろに行けます","1d5のサイコロを二回振れます","3マス進めます","自分より順位が一つ上の人を2マス戻せます","自分以外のプレイヤーを1マス戻せます"]
        reply6 = message.author.name + "さんは" + random.choice(poslist)
        await message.channel.send(reply6)
    if message.content=="1d5l":
        dicelist3 = ["2","3","4","5","6","7","8","9","10"]
        reply7 = message.author.name + "さんは" + random.choice(dicelist3) + "が出ました!"
        await message.channel.send(reply7)
    if message.content=="!bukito":
        bukitouitulist = ["竹","お風呂","キャンプ","パブロ","スパイガジェット","クアッドホッパー","クーゲル"]
        reply8 = "武器統一は" + random.choice(bukitouitulist) + "です!"
        await message.channel.send(reply8)



client.run("NzIwMDAyODE0Nzg4NTAxNjc4.Xt_puQ.vB3iJHpi2sUPSeQ-yI6K9KO8xXw")