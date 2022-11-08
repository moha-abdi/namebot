import requests
import random
import uuid
from pyromod import listen
import requests
import base64
import asyncio
import string
from pymongo.errors import DuplicateKeyError
from pymongo import MongoClient
from datetime import datetime
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import BadRequest
from pyrogram import Client, filters, idle, errors
from pyrogram.types import CallbackQuery, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, \
    InputMediaPhoto, ReplyKeyboardRemove

api_id = (14007265)
api_hash = ("00d4a84c7577da1bfe41ba5ef04906c8")
bot_token = ("5720844205:AAHdRVRoica75hXtbXmrTXYwdn4t6nFjBx0")

bot = Client(
    "namebot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)

adminlist = [1167279502, 5606411960]

cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"

client = MongoClient(cluster)


async def join(uid, client, message):
    chat_id = "sommoney"
    user_id = uid
    try:
        a = await bot.get_chat_member(chat_id, user_id)
        if a.status == ChatMemberStatus.BANNED or a.status == ChatMemberStatus.LEFT:
            chat = await bot.get_chat(chat_id)
            link = chat.invite_link
            return await message.reply("You must join this channel first",
                                       reply_markup=InlineKeyboardMarkup([[
                                           InlineKeyboardButton(chat.title, url=link)
                                       ]])
                                       )
        else:
            await message.reply(f"Hi {message.from_user.mention}")
            pass
    except:
        chat = await bot.get_chat(chat_id)
        link = chat.invite_link
        await message.reply("You must join this channel first",
                            reply_markup=InlineKeyboardMarkup([[
                                InlineKeyboardButton(chat.title, url=link)
                            ]])
                            )
        return


async def pay(num, price, id, mid, cid, id2, username):
    tt = id
    url = "https://api.sifalopay.com/gateway/"
    user = "CaaliSO6K"
    passs = "0067f29b4ac71a8f6cc256aea197a40e6ce7425e"
    userpass = user + ':' + passs
    encoded_u = base64.b64encode(userpass.encode()).decode()

    headers = {
        "Authorization": "Basic %s" % encoded_u
    }

    data = {
        "account": f"{num}",
        "amount": f"{price}",
        "gateway": "zaad",
        "currency": "USD",

    }
    mo = requests.post(url, headers=headers, json=data)
    r = mo.json()
    await errr(r, tt, mid, price, cid, id2, username)


async def errr(r, tt, mid, price, cid, id2, username):
    res = r['response']
    code = r['code']
    #print(code)
    if code == "601":
        #print('ok')
        #print(f"{res}")
        reply_markup = ReplyKeyboardRemove()
        await bot.delete_messages(chat_id=id2, message_ids=mid.id)
        await bot.send_message(chat_id=id2, text=f"✘ {res}", reply_markup=reply_markup)
    elif code == "604":
        #print(f"{res}")
        reply_markup = ReplyKeyboardRemove()
        await bot.delete_messages(chat_id=id2, message_ids=mid.id)
        await bot.send_message(chat_id=id2, text=f"✘ {res}", reply_markup=reply_markup)
    elif code == "600":
        # await add(r, tt, mid, price, cid, id2)
        tid = str(uuid.uuid4())
        tid = tid[:13]
        db = client.approve
        now = datetime.now()
        time = now.strftime("%d:%m:%Y:%H:%M:%S")
        user = {"_id": f"{tt}", "time": f"{time}", "price": f"{price}", "subscription": "monthly", "tl": "2628002.88",
                "TransactionId": f"{tid}"}
        add = db.add
        result = add.insert_one(user)
        #print(result)
        try:
            reply_markup = ReplyKeyboardRemove()
            res = f"✓ Waad ku guulaysatay lacag bixinta, \nWaxa laguu fasaxay dhamaan adeegyada SomInfo Premium\n\n[Yor transaction id is](https://t.me/Som_InfoBot) `{tid}`\n\n**-»** Fadlan copy dhe Transaction Id-gaaga oo u dir @Somali_Hacker hadaad cabasho qabto."
            res2 = "✓ Your transaction is completed."
            res3 = f"✓ @{username}, Waxa uu bixiyay ${price}\n\n[transaction id](https://t.me/Som_InfoBot) `{tid}`"
            await bot.delete_messages(chat_id=id2, message_ids=mid.id)
            await bot.answer_callback_query(cid, f'{res2}', show_alert=True)
            await bot.send_message(chat_id=id2, text=f"{res}", reply_markup=reply_markup, disable_web_page_preview=True)
            await bot.send_message(1167279502, text=f"{res3}", reply_markup=reply_markup, disable_web_page_preview=True)
            await bot.send_message(5606411960, text=f"{res3}", reply_markup=reply_markup, disable_web_page_preview=True)
        except BadRequest:
            reply_markup = ReplyKeyboardRemove()
            res = f"✓ Waad ku guulaysatay lacag bixinta, \nWaxa laguu fasaxay dhamaan adeegyada SomInfo Premium\n\n[Yor transaction id is](https://t.me/Som_InfoBot) `{tid}`\n\n**-»** Fadlan copy dhe Transaction Id-gaaga oo u dir @Somali_Hacker hadaad cabasho qabto."
            res2 = "✓ Your transaction is completed."
            res3 = f"✓ @{username}, Waxa uu bixiyay ${price}\n\n[transaction id](https://t.me/Som_InfoBot) `{tid}`"
            await bot.delete_messages(chat_id=id2, message_ids=mid.id)
            await bot.send_message(chat_id=id2, text=f"{res}", reply_markup=reply_markup, disable_web_page_preview=True)
            await bot.send_message(1167279502, text=f"{res3}", reply_markup=reply_markup, disable_web_page_preview=True)
            await bot.send_message(5606411960, text=f"{res3}", reply_markup=reply_markup, disable_web_page_preview=True)


# add(r, tt, mid, price, cid, res, reply_markup, chat_id)
#async def add(r, tt, mid, price, cid, id2):
    #print("ok")


def main(number):
    global name, saa
    la1 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(8))
    la2 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(4))
    la3 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(4))
    la4 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(4))
    la5 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(12))
    la0 = '-'
    la = la1 + la0 + la2 + la0 + la3 + la0 + la4 + la0 + la5
    sa1 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(8))
    sa2 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(4))
    sa3 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(4))
    sa4 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(4))
    sa5 = ''.join(random.choice(string.digits + string.ascii_letters.upper()) for i in range(12))
    sa0 = '-'
    sa = sa1 + sa0 + sa2 + sa0 + sa3 + sa0 + sa4 + sa0 + sa5
    lca = "EBD894E2-9304-4CEB-8010-571AF6D63E8A"
    r = requests.Session()
    u1 = "https://proxy.waafi.com/api/login"
    u2 = "https://serverb.waafi.com/subscribers/ott/login"

    heads = {'Host': 'proxy.waafi.com', 'Accept': '*/*', 'Content-Type': 'application/json',
             'Accept-Encoding': 'gzip, deflate', 'If-None-Match': 'W/"f64d-H4W52spMA+Fje37WNXpH2qRSGjc"',
             'User-Agent': 'WAAFI/7.0.1 (iPhone; iOS 15.5; Scale/3.00)', 'Accept-Language': 'en-US;q=1, ar-US;q=0.9',
             'Content-Length': '960'}
    headas = {'Host': 'serverb.waafi.com', 'Accept': '*/*', 'Content-Type': 'application/json',
              'Accept-Encoding': 'gzip, deflate', 'If-None-Match': 'W/"f64d-H4W52spMA+Fje37WNXpH2qRSGjc"',
              'User-Agent': 'WAAFI/7.0.1 (iPhone; iOS 15.5; Scale/3.00)', 'Accept-Language': 'en-US;q=1, ar-US;q=0.9',
              'Content-Length': '960'}

    session = ""

    data = {"token": {"schemaVersion": "1.0", "serviceInfo": {
        "requestAttributes": {"deviceIdType": " ", "userPassword": "maalaa09", "subscriptionId": "16465780322",
                              "userType": "CUSTOMER", "authMode": "password", "deviceId": "{}".format(lca),
                              "channelName": "MobileApp", "serviceHeader": "null", "deviceOS": "iOS",
                              "serviceType": "MMT", "sendNotifications": "0", "username": "16465780322",
                              "recieverlocationInformation": {"LACId": "", "MAC": "", "cellId": "", "MCC": "637",
                                                              "longitude": "", "latitude": "", "MNC": "71", "ip": "",
                                                              "locationType": "4", "ipaddress": "",
                                                              "locationInfoType": "NetworkLocation"},
                              "locationInformation": {"LACId": "", "MAC": "", "cellId": "", "MCC": "637",
                                                      "longitude": "", "latitude": "", "MNC": "71", "ip": "",
                                                      "locationType": "4", "ipaddress": "",
                                                      "locationInfoType": "NetworkLocation"}, "sessionId": "null"},
        "serviceName": "CustomerLogin", "serviceCode": "0101"}, "requestId": "{}".format(sa),
                      "timestamp": "1659971102777.958984", "systemInfo": {"systemId": "null", "systemSecret": "null"}}}
    pay = {
        "payload": {"mcc": "637", "deviceId": "33D35C9D-9EAF-46F9-8184-E60067EDE69C", "subscriptionId": "252636321503",
                    "appVersion": "7.2.1", "deviceOs": "iOS", "appPlatform": "iOS"}}
    moha = r.post(u1, headers=heads, json=data)

    sal = moha.json()
    sid = sal["serviceInfo"]["responseAttributes"]["sessionId"]
    no = number

    url = "https://proxyb.waafi.com/api/getInterNetWorkReceiverInformation"
    api = {"token": {"schemaVersion": "1.0", "serviceInfo": {
        "requestAttributes": {"deviceIdType": " ", "subscriptionId": "16465780322", "userType": "CUSTOMER",
                              "channelName": "MobileApp", "serviceHeader": "null", "accountId": "1040053",
                              "serviceType": "MMT", "sessionId": "{}".format(sid),
                              "recieverlocationInformation": {"LACId": "", "MAC": "", "cellId": "",
                                                              "countryName": "Somalia", "MCC": "637", "longitude": "",
                                                              "latitude": "", "MNC": "01", "ip": "",
                                                              "locationType": "4", "ipaddress": "",
                                                              "locationInfoType": "4"},
                              "locationInformation": {"LACId": "", "MAC": "", "cellId": "", "countryName": "Somalia",
                                                      "MCC": "637", "longitude": "", "latitude": "", "MNC": "01",
                                                      "ip": "", "locationType": "4", "ipaddress": "",
                                                      "locationInfoType": "4"}, "receiverMobile": "{}".format(no),
                              "txAmount": "1"}, "serviceName": "GetReceiverInfo", "serviceCode": "0000"},
                     "requestId": "{}".format(la), "systemInfo": {"systemId": "null", "systemSecret": "null"}}}
    mohan = r.post(url, json=api)
    saa = mohan.json()


@bot.on_message(filters.command(commands=['start']) & filters.private)
async def welcome(client, message):
    chat_id = "sommoney"
    user_id = message.from_user.id
    try:
        a = await bot.get_chat_member(chat_id, user_id)
        if a.status == ChatMemberStatus.BANNED or a.status == ChatMemberStatus.LEFT:
            chat = await bot.get_chat(chat_id)
            link = chat.invite_link
            return await message.reply(
                "**-»** Laguuma ogola inaad botka isticmasho. Marka hore kusoo biir channelka hoose.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(chat.title, url=link)
                ]])
                )
        else:
            read = open("trial.txt", "r").read().splitlines()
            write = open("trial.txt", "a")
            #print(read)
            nid = f"{message.chat.id}"
            readd = [i.split("|")[0] for i in read]
            cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
            client = MongoClient(cluster)
            db = client.approve
            add = db.add
            result = add.find_one({"_id": f"{nid}"})
            #print(result)
            if not nid in readd and result is None:
                write.write(f"\n{nid}|20")
                await message.reply_text(
                    text=f"**-»** {message.from_user.mention} kusoo dhawaw SomInfo, waxaad heshay 20 tijaabo oo bilaash ah.\n\n**-»** Si aad tijaboyin badan u hesho soo qor /iibso.",
                    reply_to_message_id=message.id)
            elif result is not None:
                tr = result["tl"]
                st = result["time"]
                noww = datetime.now()
                # dd/mm/YY H:M:S
                dt_string = noww.strftime("%d:%m:%Y:%H:%M:%S")
                t1 = datetime.strptime(st, "%d:%m:%Y:%H:%M:%S")
                #print(t1)
                t2 = datetime.strptime(dt_string, "%d:%m:%Y:%H:%M:%S")
                #print(t2)
                tt = t2 - t1
                #print(tt.total_seconds())
                if tt.total_seconds() >= float(tr):
                    await message.reply_text(
                        text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, Subscription kaagu uu dhacay, soo qor /iibso si aad mar labaad isku diwaangaliso.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                        reply_to_message_id=message.id)
                    add.delete_one({"_id": f"{nid}"})
                elif tt.total_seconds() < float(tr):
                    tot1 = float(tr) - tt.total_seconds()
                    tl = float(tot1)
                    #print(tl)
                    if 86400 > tl > 3600:
                        tot = tot1 / 3600
                        await message.reply_text(
                            text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, waxaa kuu hadhay {int(tot)} saacadood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                            reply_to_message_id=message.id)
                    elif tl <= 60:
                        tot = tot1 / 60
                        await message.reply_text(
                            text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, waxaa kuu hadhay {int(tot)} daqiiqadood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                            reply_to_message_id=message.id)
                    else:
                        #print(tot1)
                        tot = tot1 / 86400
                        #print(tot)
                        await message.reply_text(
                            text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, waxaa kuu hadhay {int(tot)} maalmood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                            reply_to_message_id=message.id)

            else:
                index = readd.index(f"{nid}")
                resu = read[index]
                rem = resu.split("|")[1]
                #print(rem)
                await message.reply_text(
                    text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo, waxaad haysata {rem} tijaabo oo bilaash ah.\n\n**-»** Si aad tijaboyin badan u hesho soo qor /iibso.",
                    reply_to_message_id=message.id)
    except:
        chat = await bot.get_chat(chat_id)
        link = chat.invite_link
        await message.reply("**-»** Laguuma ogola inaad botka isticmasho. Marka hore kusoo biir channelka hoose.",
                            reply_markup=InlineKeyboardMarkup([[
                                InlineKeyboardButton(chat.title, url=link)
                            ]])
                            )
        return


@bot.on_message(filters.command(commands=['start']) & filters.group)
async def welcome(client, message):
    chat_id = "sommoney"
    user_id = message.from_user.id
    try:
        a = await bot.get_chat_member(chat_id, user_id)
        if a.status == ChatMemberStatus.BANNED or a.status == ChatMemberStatus.LEFT:
            chat = await bot.get_chat(chat_id)
            link = chat.invite_link
            return await message.reply(
                "**-»** Laguuma ogola inaad botka isticmasho. Marka hore kusoo biir channelka hoose.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(chat.title, url=link)
                ]])
                )
        else:
            read = open("trial.txt", "r").read().splitlines()
            write = open("trial.txt", "a")
            #print(read)
            nid = f"{message.chat.id}"
            readd = [i.split("|")[0] for i in read]
            cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
            client = MongoClient(cluster)
            db = client.approve
            add = db.add
            result = add.find_one({"_id": f"{nid}"})
            #print(result)
            if result is None:
                ##write.write(f"\n{nid}|20")
                await message.reply_text(
                    text=f"**-»** {message.from_user.mention} kusoo dhawaw SomInfo, groupka ma diwaangashana.\n\n**-»** Si aad u diwaangaliso groupka luuqa iiguso qor /iibso.",
                    reply_to_message_id=message.id)
            elif result is not None:
                tr = result["tl"]
                st = result["time"]
                noww = datetime.now()
                # dd/mm/YY H:M:S
                dt_string = noww.strftime("%d:%m:%Y:%H:%M:%S")
                t1 = datetime.strptime(st, "%d:%m:%Y:%H:%M:%S")
                #print(t1)
                t2 = datetime.strptime(dt_string, "%d:%m:%Y:%H:%M:%S")
                #print(t2)
                tt = t2 - t1
                #print(tt.total_seconds())
                if tt.total_seconds() >= float(tr):
                    await message.reply_text(
                        text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, Subscriptionka groupku uu dhacay, luuqa iigu soo qor /iibso si aad mar labaad u diwaangaliso groupka.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                        reply_to_message_id=message.id)
                    add.delete_one({"_id": f"{nid}"})
                elif tt.total_seconds() < float(tr):
                    tot1 = float(tr) - tt.total_seconds()
                    tl = float(tot1)
                    if 86400 > tl > 3600:
                        tot = tot1 / 3600
                        await message.reply_text(
                            text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, waxaa ka hadhay dhicitanka subscriptionka groupkan {int(tot)} saacadood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                            reply_to_message_id=message.id)
                    elif tl <= 60:
                        tot = tot1 / 60
                        await message.reply_text(
                            text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, waxaa ka hadhay dhicitanka subscriptionka groupkan {int(tot)} daqiiqadood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                            reply_to_message_id=message.id)
                    else:
                        tot = tot1 / 86400
                        await message.reply_text(
                            text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo Premium, waxaa ka hadhay dhicitanka subscriptionka groupkan {int(tot)} maalmood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                            reply_to_message_id=message.id)
            # else:
            # index = readd.index(f"{nid}");
            # resu = read[index];
            # rem = resu.split("|")[1]
            # #print(rem)
            # await message.reply_text(
            # text=f"**-»** {message.from_user.mention} Kusoo dhawaw SomInfo, waxaad haysata {rem} tijaabo oo bilaash ah.\n\n**-»** Si aad tijaboyin badan u hesho soo qor /iibso.",
            # reply_to_message_id=message.id)
    except:
        chat = await bot.get_chat(chat_id)
        link = chat.invite_link
        await message.reply("**-»** Laguuma ogola inaad botka isticmasho. Marka hore kusoo biir channelka hoose.",
                            reply_markup=InlineKeyboardMarkup([[
                                InlineKeyboardButton(chat.title, url=link)
                            ]])
                            )
        return

@bot.on_message(filters.command(commands=['xaqiiji']))
async def xaqiiji(client, message):
    final = 0
    if message.from_user.id in adminlist:
        r = message.text
        niid = r.split()[1]
        tl = float(r.split()[2])
        try:
            chat = await bot.get_chat(f"{niid}")
            nid = chat.id
            cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
            client = MongoClient(cluster)
            tid = str(uuid.uuid4())
            price = 0
            tid = "free"
            db = client.approve
            now = datetime.now()
            time = now.strftime("%d:%m:%Y:%H:%M:%S")
            user = {"_id": f"{nid}", "time": f"{time}", "price": f"{price}", "subscription": "monthly",
                    "tl": f"{tl}",
                    "TransactionId": f"{tid}"}
            noww = datetime.now()
            # dd/mm/YY H:M:S
            dt_string = noww.strftime("%d:%m:%Y:%H:%M:%S")
            # t1 = datetime.strptime(st, "%d:%m:%Y:%H:%M:%S")
            ##print(t1)
            t2 = datetime.strptime(dt_string, "%d:%m:%Y:%H:%M:%S")
            #print(t2)
            tt = t2 - t2
            #print(tt.total_seconds())
            add = db.add
            try:
                result = add.insert_one(user)
                #print(result)
                tot1 = tl - tt.total_seconds()
                if 86400 > tl > 3600:
                    tot = tot1 / 3600
                    await message.reply_text(
                        text=f"**-»** {message.from_user.mention} Operation succeeded, \n@{chat.username} waxa uu helay {int(tot)} saacadood oo free ah.\n\n**-»** Haddii aad free u bahantahay la xidhiidh @Somali_Hacker",
                        reply_to_message_id=message.id)
                elif tl <= 60:
                    tot = tot1 / 60
                    await message.reply_text(
                        text=f"**-»** {message.from_user.mention} Operation succeeded, \n@{chat.username} waxa uu helay {int(tot)} daqiiqo oo free ah.\n\n**-»** Haddii aad free u bahantahay la xidhiidh @Somali_Hacker",
                        reply_to_message_id=message.id)
                else:
                    tot = tot1 / 86400
                    await message.reply_text(
                        text=f"**-»** {message.from_user.mention} Operation succeeded, \n@{chat.username} waxa uu helay {int(tot)} maalin oo free ah.\n\n**-»** Haddii aad free u bahantahay la xidhiidh @Somali_Hacker",
                        reply_to_message_id=message.id)
            except DuplicateKeyError:
                await message.reply_text(
                    text=f"**-»** {message.from_user.mention} Operation failed, \n@{chat.username} uu diwaangashanyahay.\n\n**-»** Haddii aad free u bahantahay la xidhiidh @Somali_Hacker",
                    reply_to_message_id=message.id)
        except BadRequest:
            return await message.reply(
                "**-»** Invalid user.")

    else:
        return final


@bot.on_message(filters.command(commands=['kasaar']))
async def kasaar(client, message):
    final = 0
    if message.from_user.id in adminlist:
        r = message.text
        niid = r.split()[1]
        try:
            chat = await bot.get_chat(f"{niid}")
            nid = chat.id
            cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
            client = MongoClient(cluster)
            db = client.approve
            add = db.add
            user = {"_id": f"{nid}"}
            #try:
            result = add.delete_one(user)
            #print(result)
            #except DuplicateKeyError:
                #await message.reply_text(
                    #text=f"**-»** {message.from_user.mention} Operation failed, \n@{chat.username} uu diwaangashanyahay.\n\n**-»** Haddii aad free u bahantahay la xidhiidh @Somali_Hacker",
                    #reply_to_message_id=message.id)
            await message.reply_text(
                text=f"**-»** {message.from_user.mention} Operation succeeded, \n@{chat.username} waan ka saaray.",
                reply_to_message_id=message.id)
        except BadRequest:
            return await message.reply(
                "**-»** Invalid user.")

    else:
        return final


@bot.on_message(filters.command(commands=['no']))
async def req(client, message):
    final = 0
    chat_id = "sommoney"
    user_id = message.from_user.id
    try:
        a = await bot.get_chat_member(chat_id, user_id)
        if a.status == ChatMemberStatus.BANNED or a.status == ChatMemberStatus.LEFT:
            chat = await bot.get_chat(chat_id)
            link = chat.invite_link
            return await message.reply(
                "**-»** Laguuma ogola inaad botka isticmasho. Marka hore kusoo biir channelka hoose.",
                reply_markup=InlineKeyboardMarkup([[
                    InlineKeyboardButton(chat.title, url=link)
                ]])
            )
        else:
            nid = f"{message.chat.id}"
            cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
            client = MongoClient(cluster)
            db = client.approve
            add = db.add
            result = add.find_one({"_id": f"{nid}"})
            read = open("trial.txt", "r").read().splitlines()
            write = open("trial.txt", "a")
            readd = [i.split("|")[0] for i in read]

            if result is not None:
                tr = result["tl"]
                st = result["time"]
                noww = datetime.now()
                # dd/mm/YY H:M:S
                dt_string = noww.strftime("%d:%m:%Y:%H:%M:%S")
                t1 = datetime.strptime(st, "%d:%m:%Y:%H:%M:%S")
                #print(t1)
                t2 = datetime.strptime(dt_string, "%d:%m:%Y:%H:%M:%S")
                #print(t2)
                tt = t2 - t1
                #print(tt.total_seconds())
                if tt.total_seconds() < float(tr):
                    rs = message.text
                    try:
                        number = rs.split()[1]
                        #print(number)
                        if number.isdigit():
                            main(number)
                            try:
                                name = saa["serviceInfo"]["responseAttributes"]["ReceiverInfo"]['NAME']
                                #print(saa["serviceInfo"]["responseAttributes"]["ReceiverInfo"]['NAME'])
                                await message.reply_text(
                                    text="**-»** 𝐌𝐚𝐜𝐥𝐮𝐦𝐚𝐝𝐤𝐚 𝐍𝐮𝐦𝐛𝐞𝐫𝐤𝐚\n\n**-» NAME:** ||{}||\n\n**-»** 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: @Sommoney".format(
                                        name), reply_to_message_id=message.id)


                            except KeyError:
                                await message.reply_text(
                                    text="**-»** 𝐍𝐮𝐦𝐛𝐞𝐫𝐤𝐚 𝐦𝐚𝐚𝐡𝐚𝐧 𝐦𝐢𝐝 𝐣𝐢𝐫𝐚/𝐍𝐮𝐦𝐛𝐞𝐫𝐤𝐚 𝐦𝐚 𝐝𝐢𝐰𝐚𝐚𝐧 𝐠𝐚𝐬𝐡𝐚𝐧𝐚!!",
                                    reply_to_message_id=message.id)

                        else:
                            await message.reply_text(text="Please send me a number only")
                    except IndexError:
                        return final

                elif tt.total_seconds() >= float(tr):
                    add.delete_one({"_id": f"{nid}"})
                    await message.reply_text(
                        text=f"**-»** Subscriptionkaga uu dhamaday fadlan soo qor /iibso si aad mar labaad isku diwaangliso")

            elif nid in readd:
                index = readd.index(f"{nid}")
                resu = read[index]
                rem = resu.split("|")[1]
                if rem < "1":
                    await message.reply_text(
                        text=f"**-»** Tiaaboyinka bilaashka ah way kaa dhamaden, waxaad haysata {rem} tijaabo.\n\n**-»** Fadlan soo qor /iibso si aad u iibsado tijaboyin unlimited ah kaliya $0.99.")
                else:
                    rs = message.text
                    number = rs.split()[1]
                    #print(number)
                    if number.isdigit():
                        main(number)
                        try:
                            name = saa["serviceInfo"]["responseAttributes"]["ReceiverInfo"]['NAME']
                            tr = int(rem) - 1
                            read[index] = f'{nid}|{tr}'
                            #print(read)
                            write.truncate(0)
                            write.write("\n".join(read))
                            #print(saa["serviceInfo"]["responseAttributes"]["ReceiverInfo"]['NAME'])
                            await message.reply_text(
                                text="**-»** 𝐌𝐚𝐜𝐥𝐮𝐦𝐚𝐝𝐤𝐚 𝐍𝐮𝐦𝐛𝐞𝐫𝐤𝐚\n\n**-» NAME:** ||{}||\n\n**-»** 𝐂𝐡𝐚𝐧𝐧𝐞𝐥: @Sommoney".format(
                                    name), reply_to_message_id=message.id)


                        except KeyError:
                            await message.reply_text(
                                text="**-»** 𝐍𝐮𝐦𝐛𝐞𝐫𝐤𝐚 𝐦𝐚𝐚𝐡𝐚𝐧 𝐦𝐢𝐝 𝐣𝐢𝐫𝐚/𝐍𝐮𝐦𝐛𝐞𝐫𝐤𝐚 𝐦𝐚 𝐝𝐢𝐰𝐚𝐚𝐧 𝐠𝐚𝐬𝐡𝐚𝐧𝐚!!",
                                reply_to_message_id=message.id)

                    else:
                        await message.reply_text(text="Please send me a number only")

    except:
        chat = await bot.get_chat(chat_id)
        link = chat.invite_link
        await message.reply("**-»** Laguuma ogola inaad botka isticmasho. Marka hore kusoo biir channelka hoose.",
                            reply_to_message_id=message.id,
                            reply_markup=InlineKeyboardMarkup([[
                                InlineKeyboardButton(chat.title, url=link)
                            ]])
                            )
        return


@bot.on_message(filters.command(commands=['iibso']) & filters.private)
async def payment(client, message):
    nid = f"{message.chat.id}"
    cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
    client = MongoClient(cluster)
    db = client.approve
    add = db.add
    result = add.find_one({"_id": f"{nid}"})
    if result is not None:
        tr = result["tl"]
        st = result["time"]
        noww = datetime.now()
        # dd/mm/YY H:M:S
        dt_string = noww.strftime("%d:%m:%Y:%H:%M:%S")
        t1 = datetime.strptime(st, "%d:%m:%Y:%H:%M:%S")
        #print(t1)
        t2 = datetime.strptime(dt_string, "%d:%m:%Y:%H:%M:%S")
        #print(t2)
        tt = t2 - t1
        #print(tt.total_seconds())
        tot1 = float(tr) - tt.total_seconds()
        tl = float(tot1)
        if 86400 > tl > 3600:
            tot = tot1 / 3600
            await message.reply_text(
                text=f"**-»** {message.from_user.mention} horay ayaad isku diwaangalisay, subscription-kaga waxaa kuu hadhay {int(tot)} saacadood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                reply_to_message_id=message.id)
        elif tl <= 60:
            tot = tot1 / 60
            await message.reply_text(
                text=f"**-»** {message.from_user.mention} horay ayaad isku diwaangalisay, subscription-kaga waxaa kuu hadhay {int(tot)} daqiiqo.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                reply_to_message_id=message.id)
        else:
            tot = tot1 / 86400
            await message.reply_text(
                text=f"**-»** {message.from_user.mention} horay ayaad isku diwaangalisay, subscription-kaga waxaa kuu hadhay {int(tot)} maalmood.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker",
                reply_to_message_id=message.id)

    else:
        await message.reply_photo(
            "IMG_5012.JPEG",
            caption="**-»** Soo dhawaw macmiil.\nFadlan dooro plan-ka aad rabto inaad iibsato.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Individual - $0.99/month", callback_data="individual")
                    ],
                    [
                        InlineKeyboardButton("Group - $2.95/month", callback_data="group")
                    ]
                ]
            ))


@bot.on_callback_query()
async def callback(message, CallbackQuery):
    final = 0
    if CallbackQuery.data == "individual":
        ##await CallbackQuery.answer()
        await CallbackQuery.edit_message_media(InputMediaPhoto("IMG_5019.PNG",
                                                               caption="[𝗦𝗼𝗺𝗜𝗻𝗳𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻](https://t.me/Som_InfoBot)\nSi aan xadi lahayn u isticmaal SomInfo hal bil oo dhamaystiran. Ka faaidayso qiimo dhimista."),
                                               reply_markup=InlineKeyboardMarkup(
                                                   [
                                                       [
                                                           InlineKeyboardButton("Pay $0.99", callback_data="sind")
                                                       ],
                                                   ]
                                               ))
    elif CallbackQuery.data == "group":
        ##await CallbackQuery.answer()
        await CallbackQuery.edit_message_media(InputMediaPhoto("IMG_5021.PNG",
                                                               caption="[𝗦𝗼𝗺𝗜𝗻𝗳𝗼 𝗣𝗿𝗲𝗺𝗶𝘂𝗺 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗽𝘁𝗶𝗼𝗻](https://t.me/Som_InfoBot)\nSi aan xadi lahayn ku isticmaal SomInfo Premium groupkaga hal bil oo dhamaystiran."),
                                               reply_markup=InlineKeyboardMarkup(
                                                   [
                                                       [
                                                           InlineKeyboardButton("Pay $2.95", callback_data="grp")
                                                       ],
                                                   ]
                                               ))

    elif CallbackQuery.data == "sind":
        price = 0.99
        while True:
            mohh = await bot.ask(CallbackQuery.message.chat.id,
                                 "Fadlan soo qor Numberka aad rabto inaad lacagta ku bixiso.\n**EVC**: [25261xxxxxxx](https://t.me/Som_InfoBot)\n**ZAD**: [25263xxxxxxx](https://t.me/Som_InfoBot)", disable_web_page_preview=True)
            if mohh.text == "/start" or mohh.text == "/iibso" or "/no" in mohh.text:
                return final
            elif not mohh.text.isdigit():
                try:
                    ##await bot.answer_callback_query(cid, text="✘ Numberka waa inuu digits kaliya ahaadaa", show_alert=True)
                    await bot.send_message(CallbackQuery.message.chat.id, "✘ Numberka waa inuu digits kaliya ahaadaa")
                    continue
                except BadRequest:
                    await bot.send_message(CallbackQuery.message.chat.id, "✘ Numberka waa inuu digits kaliya ahaadaa")
                    continue

            elif len(mohh.text) < 9 or len(mohh.text) > 14:
                try:
                    ##await CallbackQuery.answer("✘ Numberka aad galisay waa qalad", show_alert=True)
                    await bot.send_message(CallbackQuery.message.chat.id, "✘ Numberka aad galisay waa qalad")
                    continue
                except BadRequest:
                    await bot.send_message(CallbackQuery.message.chat.id, "✘ Numberka aad galisay waa qalad")
                    continue
            #print("ok")
            num = mohh.text
            id = CallbackQuery.message.chat.id
            id2 = CallbackQuery.message.chat.id
            #print(id)
            REPLY_MESSAGE = "Ma Hubtaa inaad bixiso lacagta"
            INLINE_MESSAGE_BUTTONS = [
                [
                    ("‎")
                ]
            ]
            text = REPLY_MESSAGE
            reply_markup = ReplyKeyboardMarkup(INLINE_MESSAGE_BUTTONS, one_time_keyboard=True, selective=True,
                                               resize_keyboard=True)
            mid = await bot.send_message(CallbackQuery.message.chat.id, "Fadlan xaqiiji lacag bixinta.",
                                         reply_markup=reply_markup)
            chatt = await bot.get_chat(id)
            username = chatt.username
            cid = CallbackQuery.id
            await pay(num, price, id, mid, cid, id2, username)
            return final

    elif CallbackQuery.data == "grp":
        price = 2.95
        while True:
            chat = await bot.ask(CallbackQuery.message.chat.id,
                                 "Fadlan soo dir Usernameka Groupka aad rabto inaad ku isticmasho SomInfo Premium,\n[[Groupka waa inuu PUPLIC ahaadaa]](https://t.me/Som_InfoBot).\n\n**USERNAME**: [@GroupUsername](https://t.me/Som_InfoBot)", disable_web_page_preview=True)
            try:
                chatt = await bot.get_chat(f"{chat.text}")
                #print(chatt)
                id = chatt.id
                nid = f"{id}"
                cluster = "mongodb+srv://mohaa:maalaa09@cluster0.1hd9iha.mongodb.net/approve?retryWrites=true&w=majority"
                client = MongoClient(cluster)
                db = client.approve
                add = db.add
                result = add.find_one({"_id": f"{nid}"})
                if result is not None:
                    tr = result["tl"]
                    st = result["time"]
                    noww = datetime.now()
                    # dd/mm/YY H:M:S
                    dt_string = noww.strftime("%d:%m:%Y:%H:%M:%S")
                    t1 = datetime.strptime(st, "%d:%m:%Y:%H:%M:%S")
                    #print(t1)
                    t2 = datetime.strptime(dt_string, "%d:%m:%Y:%H:%M:%S")
                    #print(t2)
                    tt = t2 - t1
                    #print(tt.total_seconds())
                    tot1 = 2628002.88 - tt.total_seconds()
                    tot = tot1 / 86400
                    await bot.send_message(CallbackQuery.message.chat.id,
                                           text=f"**-»** Groupka {chatt.title} uu diwaangashanyahay, subscription-ka wuxuu dhacayaa {int(tot)} maalmood kadib.\n\n**-»** Haddii aad caawin u bahantahay ama cilld ay kuhaysato la xidhiidh @Somali_Hacker")
                    return final
                else:
                    #print("pass")
                    pass
            except BadRequest:
                await bot.send_message(CallbackQuery.message.chat.id, "✘ Fadlan usernameka groupka qaab saxan usoo dir")
                continue

            mohh = await bot.ask(CallbackQuery.message.chat.id,
                                 "Fadlan soo qor Numberka aad rabto inaad lacagta ku bixiso.\n**EVC**: [25261xxxxxxx](https://t.me/Som_InfoBot)\n**ZAD**: [25263xxxxxxx](https://t.me/Som_InfoBot)", disable_web_page_preview=True)
            if mohh.text == "/start" or mohh.text == "/iibso" or "/no" in mohh.text:
                return final
            elif not mohh.text.isdigit():
                try:
                    ##await CallbackQuery.answer("✘ Numberka waa inuu digits kaliya ahaadaa", show_alert=True)
                    await bot.send_message(CallbackQuery.message.chat.id,
                                           "✘ Numberka waa inuu digits kaliya ahaadaa")
                    continue
                except BadRequest:
                    await bot.send_message(CallbackQuery.message.chat.id,
                                           "✘ Numberka waa inuu digits kaliya ahaadaa")
                    continue

            elif len(mohh.text) < 9 or len(mohh.text) > 14:
                try:
                    ##await CallbackQuery.answer("✘ Numberka aad galisay waa qalad", show_alert=True)
                    await bot.send_message(CallbackQuery.message.chat.id, "✘ Numberka aad galisay waa qalad")
                    continue
                except BadRequest:
                    await bot.send_message(CallbackQuery.message.chat.id, "✘ Numberka aad galisay waa qalad")
                    continue
            #print("ok")
            num = mohh.text
            id2 = CallbackQuery.message.chat.id
            #print(id)
            REPLY_MESSAGE = "Ma Hubtaa inaad bixiso lacagta"
            INLINE_MESSAGE_BUTTONS = [
                [
                    ("‎")
                ]
            ]
            text = REPLY_MESSAGE
            reply_markup = ReplyKeyboardMarkup(INLINE_MESSAGE_BUTTONS, one_time_keyboard=True, selective=True,
                                               resize_keyboard=True)
            mid = await bot.send_message(CallbackQuery.message.chat.id, "Fadlan xaqiiji lacag bixinta.",
                                         reply_markup=reply_markup)
            username = chatt.username
            cid = CallbackQuery.id
            #print(cid)
            await pay(num, price, id, mid, cid, id2, username)
            return final


bot.run()
