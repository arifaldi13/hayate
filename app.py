# Bismillahirrahmanirrahim
# 
# This is the brain of Hayate
# by A. R. Kusuma Putra (2018-2019)
# Model       : HP-1A Mk.V
# Version     : 1.0.0 (Alif)
# Last Deploy :
# Heroku app  : hp1amkiv

import os
import renderer as rndr
from decouple           import config
from flask              import Flask, request, abort
from linebot            import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models     import (
        MessageEvent,
        TextMessage,
        ImageMessage,
        TextSendMessage,
        TemplateSendMessage,
        ButtonsTemplate,
        URIAction
        )

app = Flask(__name__)
line_bot_api = LineBotApi    (config("LINE_CHANNEL_ACCESS_TOKEN",default=os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')))
handler      = WebhookHandler(config("LINE_CHANNEL_SECRET"      ,default=os.environ.get('LINE_CHANNEL_SECRET'      )))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def reply(event):
    text = event.message.text
    if text.find("!sum") == 0:
        rendered = rndr.renderText(text,"!sum",2)
        if rendered[0]:
            value1 = float(rendered[1][0])
            value2 = float(rendered[1][1])
            sumnation = value1 + value2
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                            rndr.renderZero(sumnation)))
    if text.find("!strikebacot") == 0:
        rendered = rndr.renderText(text,"!strikebacot",0)
        if rendered[0]:
            line_bot_api.reply_message(
                    event.reply_token,
                    TemplateSendMessage(
                            "BACOT!!!!",
                            ButtonsTemplate(
                                    "Bacod kou",
                                    "Bacod Kou",
                                    "https://s8.postimg.cc/q7r8awk05/1530265659546.jpg",
                                    "rectangle",
                                    "cover",
                                    "#FFFFFF",
                                    [URIAction("apa lu","https://youtu.be/7WZlgjo6TB0")]
                                    )
                            )
                    )
    if text.find("!infobot") == 0:
        rendered = rndr.renderText(text,"!infobot",0)
        if rendered[0]:
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage("""BOT ver 1.0 (BA ver.)
Source Code akan dirilis pada versi 2 (TSA ver.)
Kontak saya : surel@arifaldi.id

Recent Change : added !sum"""))
    if text.find("Apakah") == 0:
        rendered = rndr.renderList("Apakah","none")
        line_bot_api.reply_message(
                event.reply_token,TextSendMessage(
                        rendered))
    if text.find("Dimanakah") == 0:
        if text.lower().find("allah berada") != -1:
            rendered = rndr.renderList("Dimanakah","Allah berada")
            line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(
                            rendered))
        else:            
            rendered = rndr.renderList("Dimanakah","none")
            line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(
                            rendered))
    if text.find("Kapankah") == 0:
        if text.lower().find("kiamat terjadi") != -1:
            rendered = rndr.renderList("Kapankah","kiamat terjadi")
            line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(
                            rendered))
        if text.lower().find("dajjal datang") != -1:
            rendered = rndr.renderList("Kapankah","Dajjal datang")
            line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(
                            rendered))
        else:            
            rendered = rndr.renderList("Kapankah","none")
            line_bot_api.reply_message(
                    event.reply_token,TextSendMessage(
                            rendered))
    if text.find("Siapakah") == 0:
        rendered = rndr.renderPhrase2(text,"Siapakah"," sebenarnya?")
        if rendered[0]:
            if rendered[1].lower() == "hayate":
                extracted = rndr.renderList("Siapakah","Hayate")
                extracted = extracted.replace("<obj1>",rendered[1])
                line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                extracted))
            else:
                extracted = rndr.renderList("Siapakah","none")
                extracted = extracted.replace("<obj1>",rendered[1])
                line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                extracted))
    if text.find("Bagaimanakah") == 0:
        rendered = rndr.renderPhrase3(text,"Bagaimanakah hubungan cinta","dan","?")
        if rendered[0]:
            extracted =rndr.renderList("Bagaimanakah","none")
            extracted = extracted.replace("<obj1>",rendered[1][0])
            extracted = extracted.replace("<obj2>",rendered[1][1])
            line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                extracted))
    if text.find("Hayate") == 0:
        rendered = rndr.renderList("Hayate","none")
        line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                rendered))
    if text.find("!menu") == 0:
        rendered = rndr.renderText(text,"!menu",0)
        if rendered[0]:
            line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage("""Bismillahirrahmanirrahim

Silakan gunakan saia semau klean. Bot ini juga dilengkapi skill2 bacod agar hari2 unfaedah klean lebih tidak bermakna

Skill2 saia diantara lain :
1. Kamu nanya "Apakah bla bla?" Saia jawab kira2 bener atau salah
2. Kamu nanya "Dimanakah fulan berada?" Saia lacak tuh si fulan
3. Kamu nanya "Bagaimana hubungan cinta fulan dan fulanah?" Saia perkirakan perasaan mereka satu sama lain
4. Kamu nanya "Siapakah fulan sebenarnya?" Dengan skill ke so tau an saia, saia bongkar latar belakangnya
5. Kamu nanya "Kapankah bla bla bla?" Dengan skill ke pesimis an saia, saia terka kapan itu terjadi
6. DI GRUP KAMU ADA YANG NGEBACOD? Tenang, cukup kasih saia perintah "!strikebacot" maka saia bakal bacodin dia balik (karena saia lah raja bacod sesungguhnya)
7. Saia juga dididik sama bapa saia kenal agama, jadi kalo butuh asupan rohani langsung aja bilang "Beri Aku FIOTW"
8. Saya dah bisa penjumlahan, ketik ae "!sum a b" maka saia akan menjumlahkan a dan b
*FIOTW = Faedah Islami of The Week

Oiya, saia itu bukan dukun ea, ini semua candaan semata. Gausah dibawa serius, apalagi sampe baper. Untuk info tentang saia, silakan tulis !infobot
"""))
    if text.find("Test") == 0:
        rendered = rndr.renderText(text,"Test",0)
        if rendered[0]:
            line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                "tist"))
    if text.find("!leave") == 0:
        rendered = rndr.renderText(text,"!leave",0)
        if rendered[0]:
            if event.source.type == "room":
                line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                "Hayate pamit, ja ne!"))
                line_bot_api.leave_room(event.source.room_id)
            elif event.source.type == "group":
                line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                "Hayate pamit, ja ne!"))
                line_bot_api.leave_group(event.source.group_id)
            else:
                line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                "Anda lagi gak di mpc/grup pak, ngaco deh"))
    if text.find("!testSource") == 0:
        rendered = rndr.renderText(text,"!testSource",0)
        if rendered[0]:
            line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                str(event.source)))

@handler.add(MessageEvent, message=ImageMessage)
def repImg(event):
    rendered = rndr.renderList("Img","none")
    line_bot_api.reply_message(
                        event.reply_token,TextSendMessage(
                                rendered))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)