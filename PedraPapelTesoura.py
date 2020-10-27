# -*- coding: utf-8 -*-

import configs
import random
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Pedra Papel Tesoura'))
    print("BOT is online...")
    
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Esse comando não existe.')
        
@client.event                              
async def on_member_join(member):
    print(f"{member} entrou no servidor.")

@client.event
async def on_member_remove(member):
    print(f"{member} saiu do servidor.")
    
@client.command(aliases=['JOKENPO'])
async def jokenpo(ctx, *, question):

    pc = random.choice(["pedra","papel","tesoura"])

    await ctx.send(f'{ctx.author}: {question.lower()}\nComputador: {pc}')
    
    #Pedra      
    if question.lower() == "pedra":
        if pc == "tesoura":
            await ctx.send("Você ganhou!")
            
        elif pc == "papel":
            await ctx.send("Você perdeu!")
            
        elif question.lower() == "pedra":
            await ctx.send("Empate")

    #Papel    
    elif question.lower() == "papel":
        if pc == "pedra":
            await ctx.send("Você ganhou!")
        
        elif pc == "tesoura":
            await ctx.send("Você perdeu!")
        
        elif question.lower() == "papel":
            await ctx.send("Empate")

    #Tesoura
    elif question.lower() == "tesoura":
        if pc == "papel":
            await ctx.send("Você ganhou!")
            
        elif pc == "pedra":
            await ctx.send("Você perdeu!")
            
        elif question.lower() == "tesoura":
            await ctx.send("Empate")
    
    else:
        await ctx.send("Inválido")
        
@jokenpo.error
async def jokenpo_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor escolha um objeto para jogar.')

@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit = amount + 1)
   
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency: {round(client.latency*1000)}ms.')        

client.run(f"{configs.token}")