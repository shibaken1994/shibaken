# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'Njk0MTUyMzQzNTU3NzY3MjQ5.XoZIkA.aC-5MulEcPTjLdfYHbd6sRUK-MA'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('ハサキィ！！！')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
