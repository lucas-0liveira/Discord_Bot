import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents)
guild = bot.get_guild(801672343055147901) #É importante que o mesmo número de ID que você pega do canal seja o mesmo da variavel "bem_vindo_id"

@bot.event #evento do seu bot
async def on_member_join(member):
    bem_vindo_id = 801672343055147901 #Aqui é aonde você vai pegar o ID do canal que você deseja que seu Bot interaja, Ex: Canal de bem-vindo.
    bem_vindo = bot.get_channel(bem_vindo_id)

    guild_id = 942419519258945152 #Aqui é aonde você vai copiar o ID do servidor que você quer hospedar o seu bot
    guild = bot.get_guild(guild_id)

    #O bot irá gerar uma descrição no servidor de forma bem váriavel, sem precisar colocar o nome de forma manual, ou seja, ele já vai colocar o nome do seu servidor que você adicionou de forma automatizado.
    embed = discord.Embed(
        title=f"{member.name} | Bem-vindo(a)!",
        description=f"Salve {member.mention} Você acabou de entrar no servidor {guild.name}, cheia de pessoas incríveis e conversas fascinantes. Sinta-se à vontade para explorar o server {guild.name}, conversar sobre suas coisas favoritas e muito mais!",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=member.avatar.url)

    if guild.icon: #utiliza o perfil que você colocou no seu servidor.
      embed.set_image(url=guild.icon.url)
    else: #caso contrário, o bot vai fornecer uma foto de perfil que já deixei programado para ele adicionar no seu servidor.
      embed.set_image(url='https://logodownload.org/wp-content/uploads/2017/11/discord-logo-1-1.png')
 
    embed.set_footer(text=f'Atenciosamente, {guild.name}', icon_url='https://cdn-icons-png.flaticon.com/512/6364/6364343.png')

    await bem_vindo.send(embed=embed)



bot.run('bot_token') #aqui é aonde vai o token do seu bot para fazer com que ele funcione no servidor. Obs: não esqueça de colocar o token do bot dentro da aspas simples ('').