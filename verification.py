import requests
from async_mcrcon import MinecraftClient
import time
import os
import asyncio
import argparse

#name = input("请输入您的Minecraft ID:")
#print("========================================")
#print("  新玩家【"+name+"】申请加入桉树叶")
p = argparse.ArgumentParser(description="Whitelist X RCON")
p.add_argument(
    '-name',
    dest="name",
    default="",
    help="Minecraft accounts' display name, must be verified")
#add1 = "https://api.mojang.com/users/profiles/minecraft/"
#r = requests.get(add1 + name)
#t = r.text

try:
    args = vars(p.parse_args())
except Exception as e:
    print(e)
    sys.exit()
if (not args.get('name', None)):
    print("name not specified")
    exit(1)

#if "name" and "id" and name in t:
    #print("========================================")
    #print("         Step1.MOJANG验证通过 :)")
    #print("========================================")
    #time.sleep(1)
    #print("         Step2.已批准用户进入QQ群")
    #print("========================================")
    #time.sleep(1)
    #print("         Step3.即将联立服务器白名单")
    #print("========================================")
    #time.sleep(1)
    #MCRCON插件Github地址 “https://github.com/MrReacher/async-mcrcon” wiki-RCON官方地址 “https://wiki.vg/RCON”
    #MinecraftClient('地址',端口,'密码')  【务必注意引号】
    #async_mcrcon.py里面需要填写地址、端口、密码，请设置！！！
async def updateWhitelist():
    async with MinecraftClient('127.0.0.1', 2112, 'f5NnECg3KgDc') as mc:
        output = await mc.send('whitelist add ' + args.get('name', None))
        print(output)
asyncio.run(updateWhitelist())

'''else:
    print("========================================")
    print("           MOJANG验证失败 :(")
    print("========================================")
'''
