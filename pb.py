# -*- coding: utf-8 -*-
#thanks to allfams

from linepy import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, multiprocessing, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib3, urllib.parse, html5lib, wikipedia, atexit, timeit, pafy, youtube_dl, traceback
from gtts import gTTS
from googletrans import Translator
#from zalgo_text import zalgo
from threading import Thread,Event
#import requests,uvloop
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()

cl = LINE()
#cl = LINE("TOKEN")
#cl = LINE("Email","Password")
cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
cl.log("Channel Token : " + str(channelToken))

ki = LINE()
#ki = LINE("TOKEN")
#ki = LINE("Email","Password")
ki.log("Auth Token : " + str(ki.authToken))
channelToken = ki.getChannelResult()
ki.log("Channel Token : " + str(channelToken))

kk = LINE()
#kk = LINE("TOKEN")
#kk = LINE("Email","Password")
kk.log("Auth Token : " + str(kk.authToken))
channelToken = kk.getChannelResult()
kk.log("Channel Token : " + str(channelToken))

kc = LINE()
#kc = LINE("TOKEN")
#kc = LINE("Email","Password")
kc.log("Auth Token : " + str(kc.authToken))
channelToken = kc.getChannelResult()
kc.log("Channel Token : " + str(channelToken))


#kb = LINE("u8cba2a07291fc16e605ddd3fae4334bb:aWF0OiAxNTUyMDEyOTg0OTAyCg==..NmHWZJcQtsCCSnyA/ggnKbDsvmg=")
#kb.log("Auth Token : " + str(kb.authToken))


#kd = LINE("ue464b9df1caff7a5bec27897cb686054:aWF0OiAxNTUyMDEzMzI4MzkxCg==../wucqtMjMyocmN4TB+LsQIb/mJs=")
#kd.log("Auth Token : " + str(kd.authToken))


#ke = LINE("ua90b8c43ce9a4518a0391699b6819938:aWF0OiAxNTUyMDE0Njc4ODAyCg==..iMfWvD1TBziiJ1jBQ8pTaSeW9JI=")
#ke.log("Auth Token : " + str(ke.authToken))

#kf = LINE("u72942a440baa6a968c77e009facb25e5:aWF0OiAxNTUyMDE1MDE1NjQ2Cg==..kpxRhA+C22AvZNx7b6TlWcYxYUM=")
#kf.log("Auth Token : " + str(kf.authToken))


#kg = LINE("u1585d66bf6e61f5662bf9d8d2a9d78b8:aWF0OiAxNTUxNDM0MDc2MzMzCg==..X6OZFWkDPyM9YyaFEIhJ1KJMe8k=")
#kg.log("Auth Token : " + str(kg.authToken))


#kh = LINE("ua7ff1a841a04c9e54a662b665bd84900:aWF0OiAxNTUxNDU2NDk3NTY5Cg==..GIzqB77O697YitsrJ5PkAMpP9qY=")
#kh.log("Auth Token : " + str(kh.authToken))


#kj = LINE("u25fe5d03e77aba441a7ed116005eaa91:aWF0OiAxNTUxNDUxMDg5MDIyCg==..DxUJTs/l9QahrpsRqvJxCD8S/wk=")
#kj.log("Auth Token : " + str(kj.authToken))

#sw = LINE("ub658f98ac9721d6a7fc3fdad171b77fa:aWF0OiAxNTUyMDE2MDU1MzQ2Cg==..hW1nIWbEmdG7Cq/bB2DqA/guKx4=")
#sw.log("Auth Token : " + str(sw.authToken))



oepoll = OEPoll(cl)
call = cl
creator = ["u4d27e75137126f5e208daf06c0d8f9e5"]
owner = ["u4d27e75137126f5e208daf06c0d8f9e5"]
admin = ["u4d27e75137126f5e208daf06c0d8f9e5"]
staff = ["u4d27e75137126f5e208daf06c0d8f9e5"]

lineProfile = cl.getProfile()
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
#Dmid = kb.getProfile().mid
#Emid = kd.getProfile().mid
#Fmid = ke.getProfile().mid
#Gmid = kf.getProfile().mid
#Hmid = kg.getProfile().mid
#Imid = kh.getProfile().mid
#Jmid = kj.getProfile().mid
#Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc]
ABC = [cl,ki,kk,kc]
#GHOST = [kj,sw]
Bots = [mid,Amid,Bmid,Cmid]
Saints = admin + owner + staff
Team = creator + owner + admin + staff + Bots
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

protectqr = []
protectinvite = []
left = []
welcome = []
protectkick = []
protectcancel = []
welcome = []
targets = []
protectname = []
prohibitedWords = ['Asu', 'Jancuk', 'Tai', 'Kickall', 'Ratakan', 'Cleanse']
userTemp = {}
userKicked = []
msg_dict = {}
msg_dict1 = {}
dt_to_str = {}
temp_flood = {}
groupName = {}
groupImage = {}
list = []
ban_list = []
warmode = []
ghost = []
offbot = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
#responsename4 = kb.getProfile().displayName
#responsename5 = kd.getProfile().displayName
#responsename6 = ke.getProfile().displayName
#responsename7 = kf.getProfile().displayName
#responsename8 = kg.getProfile().displayName
#responsename9 = kh.getProfile().displayName


settings = {
    "autoBlock": False,
    "autoRead": False,
    "welcome": False,
    "leave": False,
    "mid": False,
    "keyCommand": "dent ",
    "commentPost": "AutoLikeTL\nBy:Pandawa",
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": True,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "dhenza":{},
    "likeOn": True,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "unsend":True,
    "selfbot":True,
    "mention":"Masuk say ngitip bacok",
    "Respontag":"Cuy ngetag mele..",
    "welcome":"Wellcome",
    "comment":"Auto like By Pandawa",
    "comment1":"Auto like PandawaBot",
    "message":"Ciee nge add kepo ye..\nThanks for add me.."
}
protect = {
    "pqr":[],
    "pinv":[],
    "proall":[],
    "antijs":[],
    "protect":[]
}

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dzProfile = cl.getProfile()
myProfile["displayName"] = dzProfile.displayName
myProfile["statusMessage"] = dzProfile.statusMessage
myProfile["pictureStatus"] = dzProfile.pictureStatus

Setbot = codecs.open("setting.json","r","utf-8")   
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def logError(text):
    cl.log("[ PANDAWA BOTS ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Makassar")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as error:
        error.write("\n[{}] {}".format(str(time), text))

def sendTemplates(to, data):
    data = data
    url = "https://api.line.me/message/v3/share"
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Note 5 Build/OPM1.171019.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 Line/8.1.1'  
    headers['Content-Type'] = 'application/json'  
    headers['Authorization'] = 'Bearer eyJhbGciOiJIUzI1NiJ9.5uMcEEHahauPb5_MKAArvGzEP8dFOeVQeaMEUSjtlvMV9uuGpj827IGArKqVJhiGJy4vs8lkkseiNd-3lqST14THW-SlwGkIRZOrruV4genyXbiEEqZHfoztZbi5kTp9NFf2cxSxPt8YBUW1udeqKu2uRCApqJKzQFfYu3cveyk.GoRKUnfzfj7P2uAX9vYQf9WzVZi8MFcmJk8uFrLtTqU'
    sendPost = requests.post(url, data=json.dumps(data), headers=headers)
    print(sendPost)
    return sendPost
def sendTextTemplate(to, text):
    data = {
            "type": "flex",
            "altText": "pandawabots",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#00FFFF",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)

def sendTextTemplateku(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Klik cover dan add owner Pandawa".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF00FF"
    },
    "header": {
      "backgroundColor": "#FF00FF"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://i.pinimg.com/originals/fd/47/e5/fd47e55dfb49ae1d39675d6eff34a729.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "PANDAWA BOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate5(to, text):
    data = {
            "type": "flex",
            "altText": "PANDAWA BOTS",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#F0F8FF"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00008B"
    },
    "header": {
      "backgroundColor": "#00008B"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "sÉªÊá´Êá´á´É´ á´ÉªÊÉªÊ",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ð¶SOUNDCLOUDð¶",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate1(to, text):
    data = {
                "type": "template",
                "altText": "pandawabots",
                "contents": {
                    "type": "bubble",
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                               "text": text,
                               "size": "sm",
                               "margin": "none",
                               "color": "#8B008B",
                               "wrap": True,
                               "weight": "regular",
                               "type": "text"
                            }
                        ]
                    }
                }
            }
    cl.postTemplate(to, data)

def sendTextTemplate2(to, text):
    data = {
            "type": "flex",
            "altText": "pandawabots",
            "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#0000CD"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": text,
                "size": "md",
                "margin": "none",
                "color": "#FFFF00",
                "wrap": True,
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  }
}
}
    cl.postTemplate(to, data)
    
def sendTextTemplate3(to, text):
    data = {
            "type": "flex",
            "altText": "PandawaBot",
            "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "sm",
            "weight": "bold",
            "wrap": True,
            "color": "#CCFF33"
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF00FF"
    },
    "header": {
      "backgroundColor": "#FF00FF"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "PANDAWABOTS",
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)

def sendStickerTemplate(to, text):
    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
    to = op.param1
    data = {
                          "type": "template",
                          "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                          "template": {
                             "type": "image_carousel",
                             "columns": [
                              {
                                  "imageUrl": text,
                                  "size": "full", 
                                  "action": {
                                      "type": "uri",
                                      "uri": "http://line.me/ti/p/~tetsunaki"
           }                                                
 }
]
                          }
                      }
    cl.postTemplate(to, data)

def sendTextTemplate4(to, text):
    data = {
                                "type": "flex",
                                "altText": "{} Klik cover add owner Pandawa".format(cl.getProfile().displayName),
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": text,
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#40E0D0",
            "align": "center"
          },
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FFFF00"
    },
    "header": {
      "backgroundColor": "#FFFF00"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "http://www.gambaranimasi.org/data/media/561/animasi-bergerak-pacar-kekasih-0108.gif",
    "size": "full",
    "margin": "xl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1602687308-GXq4Vvk9/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "PANDAWA BOT",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
    cl.postTemplate(to, data)

    
def logError(text):
    cl.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))
        
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]
            
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def downloadImageWithURL (mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)
    
def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendImage(to, path, name="image"):
    try:
        if settings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)

def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 3*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        cl.sendMessage(tmp, "Bot kembali aktif")
                    except Exception as error:
                        logError(error)
                        
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
                        
def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = cl.genOBSParams({'oid': mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        cl.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))

def changeProfileVideo(to):
    if settings['changeProfileVideo']['picture'] == None:
        return cl.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changeProfileVideo']['video'] == None:
        return cl.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changeProfileVideo']['video']
        files = {'file': open(path, 'rb')}
        obs_params = cl.genOBSParams({'oid': cl.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = cl.server.postContent('{}/talk/vp/upload.nhn'.format(str(cl.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return cl.sendMessage(to, "Gagal update profile")
        path_p = settings['changeProfileVideo']['picture']
        settings['changeProfileVideo']['status'] = False
        cl.updateProfilePicture(path_p, 'vp')

def cloneProfile(mid):
    contact = cl.getContact(mid)
    if contact.videoProfile == None:
        cl.cloneContactProfile(mid)
    else:
        profile = cl.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = cl.getProfileDetail(mid)['result']['objectId']
    cl.updateProfileCoverById(coverId)

def restoreProfile():
    profile = cl.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        cl.updateProfileAttribute(8, profile.pictureStatus)
        cl.updateProfile(profile)
    else:
        cl.updateProfile(profile)
        pict = cl.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = cl.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    cl.updateProfileCoverById(coverId)
    
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)

def backupProfile():
    profile = cl.getContact(mid)
    settings['myProfile']['displayName'] = profile.displayName
    settings['myProfile']['pictureStatus'] = profile.pictureStatus
    settings['myProfile']['statusMessage'] = profile.statusMessage
    settings['myProfile']['videoProfile'] = profile.videoProfile
    coverId = cl.getProfileDetail()['result']['objectId']
    settings['myProfile']['coverId'] = str(coverId)
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += settings["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        sendTextTemplate(to, "salkomsel")

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "welcome"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
      #  client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def leaveMembers(to, mid):
    try:
        arrData = ""
        textx = " ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += "babay"
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n???[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n???[ Success ]"
        #client.sendMessage(to, textx)
    except Exception as error:
        cl.sendMessage(to)
        
def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"\nJam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\nGroup : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nxpired : In "+hari+"\nVersion : Sempak Bot\nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain['keyCommand']):
        cmd = pesan.replace(Setmain['keyCommand'],"")
    else:
        cmd = "command"
    return cmd


def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protect["pqr"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            Ticket = cl.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            sw.kickoutFromGroup(op.param1,[op.param2]) 
                            sw.leaveGroup(op.param1)
                            kj.leaveGroup(op.param1)
                            cl.updateGroup(X)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                Ticket = ki.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                sw.leaveGroup(op.param1)
                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                kj.kickoutFromGroup(op.param1,[op.param2])
                                kj.leaveGroup(op.param1)
                                ki.updateGroup(X)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    Ticket = kk.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    kj.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(X)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kj.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(X)
                            except:
                                try:
                                    if km.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(X)
                                except:
                                    try:
                                        if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kd.reissueGroupTicket(op.param1)
                                                X = kd.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                Ticket = kb.reissueGroupTicket(op.param1)
                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                kj.kickoutFromGroup(op.param1,[op.param2])
                                                kd.updateGroup(X)
                                    except:
                                        try:
                                            if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ke.reissueGroupTicket(op.param1)
                                                    X = ke.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    Ticket = kb.reissueGroupTicket(op.param1)
                                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                    kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                    kj.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.updateGroup(X)            
                                        except:
                                            try:
                                                if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kf.reissueGroupTicket(op.param1)
                                                        X = kf.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        Ticket = kb.reissueGroupTicket(op.param1)
                                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                                        kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                        kj.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.updateGroup(X)         
                                            except:
                                                try:
                                                    if kg.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            kg.reissueGroupTicket(op.param1)
                                                            X = kg.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            Ticket = kb.reissueGroupTicket(op.param1)
                                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                            kj.kickoutFromGroup(op.param1,[op.param2])
                                                            kg.updateGroup(X)         
                                                except:
                                                    try:
                                                        if kh.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                kh.reissueGroupTicket(op.param1)
                                                                X = kh.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                Ticket = kb.reissueGroupTicket(op.param1)
                                                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                                                kj.kickoutFromGroup(op.param1,[op.param2])
                                                                kh.updateGroup(X)
                                                               # cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                    except:
                                                        pass
                      
        if op.type == 11:
            if op.param1 in warmode:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            wait["blacklist"][op.param2] = True
                            try:ki.kickoutFromGroup(op.param1,[op.param2])
                            except:
                            	try:kk.kickoutFromGroup(op.param1,[op.param2])
                            	except:
                            	    try:kc.kickoutFromGroup(op.param1,[op.param2])
                            	    except:
                            	        try:kb.kickoutFromGroup(op.param1,[op.param2])
                            	        except:
                            	            try:kd.kickoutFromGroup(op.param1,[op.param2])
                            	            except:
                            	                try:ke.kickoutFromGroup(op.param1,[op.param2])
                            	                except:
                            	                    try:kf.kickoutFromGroup(op.param1,[op.param2])
                            	                    except:
                            	                        try:kg.kickoutFromGroup(op.param1,[op.param2])
                            	                        except:
                            	                            try:kh.kickoutFromGroup(op.param1,[op.param2])
                            	                            except:pass
                            warmode.remove(op.param1)
                except:pass
       
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                   try:ki.kickoutFromGroup(op.param1,[op.param2])
                   except:
                    try:kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:kc.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:kb.kickoutFromGroup(op.param1,[op.param2])
                            except:
                            	   try:kd.kickoutFromGroup(op.param1,[op.param2])
                            	   except:
                            	       try:ke.kickoutFromGroup(op.param1,[op.param2])
                            	       except:
                            	           try:kf.kickoutFromGroup(op.param1,[op.param2])
                            	           except:
                            	               try:kg.kickoutFromGroup(op.param1,[op.param2])
                            	               except:
                            	                   try:kh.kickoutFromGroup(op.param1,[op.param2])
                            	                   except:
                            	                       try:cl.kickoutFromGroup(op.param1,[op.param2])
                            	                       except:pass
                   cl.reissueGroupTicket(op.param1)
                   X = cl.getGroup(op.param1)
                   X.preventedJoinByTicket = True
                   cl.updateGroup(X)
                   warmode.append(op.param1)
                else:
                   pass
#========================== PROTECTUPDATEGROUP                          
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplateku(op.param1,"Sorry anda bukan admin kami\nSelamat tinggal " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplateku(op.param1,"Hy salken " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplateku(op.param1,"Salken ,I m happy 's to mert you " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        sendTextTemplateku(op.param1,"Salken I'm happy 's to meet you " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)                        
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)                                             
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)                        
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)                       
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)                       
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)                      
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        km.acceptGroupInvitation(op.param1)
                        ginfo = km.getGroup(op.param1)                        
                        km.leaveGroup(op.param1)
                    else:
                        km.acceptGroupInvitation(op.param1)                        
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)                        
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)                       

            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)                        
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)                                             
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)                        
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)                       
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)                       
                        kg.leaveGroup(op.param1)
                    else:
                        kg.acceptGroupInvitation(op.param1)                      
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)                        
                        kh.leaveGroup(op.param1)
                    else:
                        kh.acceptGroupInvitation(op.param1)

        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                            sw.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                            sw.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        try:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                invsend = 0
                                Ticket = kk.reissueGroupTicket(op.param1)
                                sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                sw.kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                                sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                sw.leaveGroup(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)
                        except:
                            try:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    invsend = 0
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                    sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                    sw.leaveGroup(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                            except:
                                try:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        G = kb.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kb.updateGroup(G)
                                        invsend = 0
                                        Ticket = kb.reissueGroupTicket(op.param1)
                                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        sw.kickoutFromGroup(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                        sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                        sw.leaveGroup(op.param1)
                                        X = kb.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kb.updateGroup(X)
                                except:
                                    try:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.updateGroup(G)
                                            invsend = 0
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.kickoutFromGroup(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                            sw.sendMessage(op.param1,"Wah kiker tempe main kick orang minta di hajar")
                                            sw.leaveGroup(op.param1)
                                            X = ke.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ke.updateGroup(X)       
                                    except:
                                        pass

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                	pass
#____________________________________________________________________
 
        if op.type == 13:
            if op.param1 in protect['pinv']:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        try:
                                            group = kd.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for _mid in gMembMids:
                                                random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])
                                        except:
                                            try:
                                                group = ke.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for _mid in gMembMids:
                                                    random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])      
                                            except:
                                                try:
                                                    group = kf.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for _mid in gMembMids:
                                                        random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])   
                                                except:
                                                    try:
                                                        group = kh.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for _mid in gMembMids:
                                                            random.choice(ABC).cancelGroupInvitation(op.param1,[_mid])     
                                                    except:
                                                        pass                                    

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                    	kb.cancleGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kd.cancleGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                        	    ke.cancleGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                        	        kf.cancleGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                        	            kg.cancleGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                        	                kh.cancleGroupInvitation(op.param1,[op.param2])
                                                        except:
                                        	                pass
                return
                                            
#__________________________________ 
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kd.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                        	    ke.kickoutFromGroup(op.param1,[op.param2])
                                            except:
                                                try:
                                        	        kf.kickoutFromGroup(op.param1,[op.param2])
                                                except:
                                                    try:
                                        	            kg.kickoutFromGroup(op.param1,[op.param2])
                                                    except:
                                                        try:
                                        	                kh.kickoutFromGroup(op.param1,[op.param2])
                                                        except:
                                        	                pass
                return
#____________________________________________________________________               
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True                    
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                    	kb.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                        	kd.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                        	pass
                return
#________________________________                                            
        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        cl.acceptGroupInvitation(op.param1)
                        kk.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            cl.acceptGroupInvitation(op.param1)
                            kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            kc.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                cl.acceptGroupInvitation(op.param1)
                                kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitation(op.param1)
                                    kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        cl.acceptGroupInvitation(op.param1)
                                        kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                                ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                kf.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kg.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        kh.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)    
                                                            kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            cl.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            pass
                return
            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                kd.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)     
                                        ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        kf.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kf.kickoutFromGroup(op.param1,[op.param2])
                                                kf.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                kg.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                    kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kh.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                        kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                                            ki.acceptGroupInvitation(op.param1)    
                                                            cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            ki.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        kb.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            kd.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                ke.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)     
                                        kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                            kc.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kg.kickoutFromGroup(op.param1,[op.param2])
                                                kg.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                                kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                kh.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                                    kh.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                    kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                        cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        ki.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.acceptGroupInvitation(op.param1)    
                                                            ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            kk.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        kd.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            ke.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                kf.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    kg.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)     
                                        kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                                kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                cl.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                    cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    ki.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                        ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        kk.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.acceptGroupInvitation(op.param1)    
                                                            kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            kb.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            pass
                return

            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        ke.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            kf.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                kg.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                    kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    kh.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)     
                                        kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                                cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                ki.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                    ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                        kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.acceptGroupInvitation(op.param1)    
                                                            kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                        	pass
                return

            if Emid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                        ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        kf.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kf.kickoutFromGroup(op.param1,[op.param2])
                            kf.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                            kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            kg.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kg.kickoutFromGroup(op.param1,[op.param2])
                                kg.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                                kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                kh.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                    kh.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                    kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)     
                                        cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1)
                                                ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.acceptGroupInvitation(op.param1)
                                                    kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        kd.acceptGroupInvitation(op.param1)
                                                        kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.acceptGroupInvitation(op.param1)    
                                                            kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            ke.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                        	pass
                return

            if Fmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        kg.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kg.kickoutFromGroup(op.param1,[op.param2])
                            kg.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                            kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            kh.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kh.kickoutFromGroup(op.param1,[op.param2])
                                kh.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                                kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                cl.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                    cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    ki.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)     
                                        cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        ki.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                            kf.updateGroup(G)
                                            Ticket = kg.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                                kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                kc.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                    kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        kd.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            ke.acceptGroupInvitation(op.param1)    
                                                            kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                        	pass
                return

            if Gmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        kg.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                        kg.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                            kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                                cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                    ki.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)     
                                        kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kg.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                            kg.updateGroup(G)
                                            Ticket = kg.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kg.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kg.updateGroup(G)
                                            Ticket = kg.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                kf.acceptGroupInvitation(op.param1)
                                                kc.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    kf.acceptGroupInvitation(op.param1)
                                                    kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.acceptGroupInvitation(op.param1)
                                                        kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            kf.acceptGroupInvitation(op.param1)    
                                                            ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                        	pass                                    
                return

            if Hmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kh.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                        kh.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                            cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                                cl.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kg.acceptGroupInvitation(op.param1)
                                    kk.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)     
                                        kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                        kd.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kh.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                            kh.updateGroup(G)
                                            Ticket = kh.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            G = kh.getGroup(op.param1)
                                            G.preventedJoinByTicket = True
                                            kh.updateGroup(G)
                                            Ticket = kh.reissueGroupTicket(op.param1)
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                kg.acceptGroupInvitation(op.param1)
                                                kb.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    kg.acceptGroupInvitation(op.param1)
                                                    kd.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        kg.acceptGroupInvitation(op.param1)
                                                        ke.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            kg.acceptGroupInvitation(op.param1)    
                                                            kf.inviteIntoGroup(op.param1,[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid])
                                                            cl.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                        	pass
                return

        if op.type == 19:
            if Imid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kj.kickoutFromGroup(op.param1,[op.param2])
                        kj.inviteIntoGroup(op.param1,[op.param3])
                        sw.acceptGroupInvitation(op.param1)
                        kj.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            sw.acceptGroupInvitation(op.param1)
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                sw.acceptGroupInvitation(op.param1)
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    sw.acceptGroupInvitation(op.param1)
                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        sw.acceptGroupInvitation(op.param1)
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            sw.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                sw.acceptGroupInvitation(op.param1)
                                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    sw.acceptGroupInvitation(op.param1)
                                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        sw.acceptGroupInvitation(op.param1)
                                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            sw.acceptGroupInvitation(op.param1)
                                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                kg.kickoutFromGroup(op.param1,[op.param2])
                                                                kg.inviteIntoGroup(op.param1,[op.param3])
                                                                sw.acceptGroupInvitation(op.param1)
                                                                kg.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   kh.kickoutFromGroup(op.param1,[op.param2])
                                                                   kh.inviteIntoGroup(op.param1,[op.param3])
                                                                   sw.acceptGroupInvitation(op.param1)
                                                                   kh.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass   
                                            
                return


            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,admin)
                                                    kf.inviteIntoGroup(op.param1,admin)
                                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,admin)
                                                        kg.inviteIntoGroup(op.param1,admin)  
                                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                                    except:  
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,admin)
                                                            kh.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                 try:
                                                     kf.kickoutFromGroup(op.param1,[op.param2])
                                                     kf.findAndAddContactsByMid(op.param1,admin)
                                                     kf.inviteIntoGroup(op.param1,admin)
                                                 except:
                                                     try:
                                                         kg.kickoutFromGroup(op.param1,[op.param2])
                                                         kg.findAndAddContactsByMid(op.param1,admin)
                                                         kg.inviteIntoGroup(op.param1,admin)  
                                                     except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,admin)
                                                            kh.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass
                                                           
            
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass       
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass         

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass          

                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass
                                                           
                return

            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                           try:
                                               ke.kickoutFromGroup(op.param1,[op.param2])
                                               ke.findAndAddContactsByMid(op.param1,admin)
                                               ke.inviteIntoGroup(op.param1,admin)
                                           except:
                                               try:
                                                   kf.kickoutFromGroup(op.param1,[op.param2])
                                                   kf.findAndAddContactsByMid(op.param1,admin)
                                                   kf.inviteIntoGroup(op.param1,admin)
                                               except:
                                                   try:
                                                       kg.kickoutFromGroup(op.param1,[op.param2])
                                                       kg.findAndAddContactsByMid(op.param1,admin)
                                                       kg.inviteIntoGroup(op.param1,admin)  
                                                   except:
                                                       try:
                                                           kh.kickoutFromGroup(op.param1,[op.param2])
                                                           kh.findAndAddContactsByMid(op.param1,admin)
                                                           kh.inviteIntoGroup(op.param1,admin)  
                                                       except:
                                                           pass           
                                
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,staff)
                            ki.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,staff)
                                kk.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,staff)
                                    kc.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,staff)
                                        kb.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,staff)
                                            kd.nviteIntoGroup(op.param1,staff)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,staff)
                                                ke.inviteIntoGroup(op.param1,staff)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,staff)
                                                    kf.inviteIntoGroup(op.param1,staff)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,staff)
                                                        kg.inviteIntoGroup(op.param1,staff)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,staff)
                                                            kh.inviteIntoGroup(op.param1,staff)  
                                                        except:
                                                            pass
                                    
                                    
                
                                            
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,staff)
                            ki.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,staff)
                                kk.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,staff)
                                    kc.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,staff)
                                        kb.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,staff)
                                            kd.nviteIntoGroup(op.param1,staff)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,staff)
                                                ke.inviteIntoGroup(op.param1,staff)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,staff)
                                                    kf.inviteIntoGroup(op.param1,staff)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,staff)
                                                        kg.inviteIntoGroup(op.param1,staff)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,staff)
                                                            kh.inviteIntoGroup(op.param1,staff)  
                                                        except:
                                                            pass
                                            
                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,staff)
                            ki.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,staff)
                                kk.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,staff)
                                    kc.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,staff)
                                        kb.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,staff)
                                            kd.nviteIntoGroup(op.param1,staff)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,staff)
                                                ke.inviteIntoGroup(op.param1,staff)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,staff)
                                                    kf.inviteIntoGroup(op.param1,staff)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,staff)
                                                        kg.inviteIntoGroup(op.param1,staff)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,staff)
                                                            kh.inviteIntoGroup(op.param1,staff)  
                                                        except:
                                                            pass
                                            
                return

            if member in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in member:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,member)
                        cl.inviteIntoGroup(op.param1,member)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,member)
                            ki.inviteIntoGroup(op.param1,member)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,member)
                                kk.inviteIntoGroup(op.param1,member)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,member)
                                    kc.inviteIntoGroup(op.param1,member)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,member)
                                        kb.inviteIntoGroup(op.param1,member)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,member)
                                            kd.nviteIntoGroup(op.param1,member)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,member)
                                                ke.inviteIntoGroup(op.param1,member)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,member)
                                                    kf.inviteIntoGroup(op.param1,member)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,member)
                                                        kg.inviteIntoGroup(op.param1,member)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,member)
                                                            kh.inviteIntoGroup(op.param1,member)  
                                                        except:
                                                            pass         
                                            
                return
        if op.type == 46:
            if op.param2 in mid:
                cl.kickout.AllMessages("kickall")
            if op.param2 in Amid:                
                ki.kickout.AllMessages("malam")
            if op.param2 in mid:
                kk.kickoutAllMessages("siang")
            if op.param2 in Bmid:                
                kc.kickout.AllMessages("maaf")
            if op.param2 in Cmid:                
                kc.kickout.AllMessages("salken")
            if op.param2 in Dmid:                
                kb.kickout.AllMessages("lope")
            if op.param2 in Emid:                
                kd.kickAllMessages("jancok")
            if op.param2 in Fmid:                
                ke.kickout.AllMessages("asu")
            if op.param2 in Gmid:                
                kf.kickout.AllMessages("loha")
            if op.param2 in Hmid:                
                kg.kickout.AllMessages("tes")
            if op.param2 in Imid:                
                kh.kickout.AllMessages("hay")
                    
                return

                            

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                welcomeMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2)
                data = {
                        "type": "flex",
                        "altText": "pandawabot",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "ð  WELCOME TO THE ROOM ð ",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFD700"
          },
          {
            "type": "text",
            "text": "â£ Jangan Lupa Cek Note\nâ£ Ciptakan Keamanan Room,\nâ£ Dan Harmoni Persahabatan\nâ£ Karena Kita Semua\nâ£ Sahabat Disini\nâ£ Terimakasih",
            "size": "md",
            "weight": "bold",
            "color": "#ADFF2F",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#0000FF"
    },
    "footer": {
      "backgroundColor": "#DC143C"
    }
  },
  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BOSS",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                cl.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://i.ibb.co/rGSVfNg/89933.gif")
            
        if op.type == 15:
            if op.param1 in welcome:
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])
                contact = cl.getContact(op.param2).picturePath
                data = {
                        "type": "flex",
                        "altText": "pandawabot",
                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "flex": 2,
            "text": "{}".format(cl.getContact(op.param2).displayName),
            "size": "md",
            "wrap": True,
            "weight": "bold",
            "gravity": "center",
            "color": "#FF0000"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "type": "text",
            "text": "ð  GOOD BYE ð ",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#FFD700"
          },
          {
            "type": "text",
            "text": "â£ Selamat Jalan Saudara\nâ£ Smoga Smakin Sukses\nâ£ Dan Kami Dari Pengurus,\nâ£ Minta Maaf Jikalau\nâ£ Selama Kita Bersama\nâ£ Kami Salah Dalam Berkata\nâ£ Terimakasih",
            "size": "md",
            "weight": "bold",
            "color": "#ADFF2F",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#0000FF"
    },
    "footer": {
      "backgroundColor": "#DC143C"
    }
  },
  
  "hero": {
    "aspectRatio": "20:13",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "BOSS",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#7CFC00",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#E5E4E2"
      },
      {
        "type": "text",
        "text": "ORDER",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "line://app/1603968955-ORWb9RdY/?type=text&text=Order"
        },
        "align": "center"
      }
    ]
  }
}
}
                cl.postTemplate(op.param1, data)
                sendStickerTemplate(op.param1, "https://i.ibb.co/WGt0yGK/animasi-bergerak-selamat-tinggal-0020.gif")

                
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param3 in Bots:
                    if op.param2 not in Bots and op.param2 not in Team:
                        wait["blacklist"][op.param2] = True
                        try:
                            if op.param3 not in wait["blacklist"]:
                                random.coice(ABC).findAndAddContactsByMid(op.param1,[Zmid])
                                random.coice(ABC).kickoutFromGroup(op.param1,[op.param2])
                                random.coice(ABC).inviteIntoGroup(op.param1,[Zmid])
                        except:
                            pass

        if op.type == 32:
            if op.param3 in Zmid:
              if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                  wait["blacklist"][op.param2] = True
                  try:
                      if op.param3 not in wait["blacklist"]:
                          ki.kickoutFromGroup(op.param1,[op.param2])
                          ki.inviteIntoGroup(op.param1,[Zmid])
                          cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                  except:
                      try:
                          if op.param3 not in wait["blacklist"]:
                              kk.kickoutFromGroup(op.param1,[op.param2])
                              kk.inviteIntoGroup(op.param1,[Zmid])
                              cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                      except:
                          try:
                              if op.param3 not in wait["blacklist"]:
                                  kc.kickoutFromGroup(op.param1,[op.param2])
                                  kc.inviteIntoGroup(op.param1,[Zmid])
                                  cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                          except:
                              try:
                                  if op.param3 not in wait["blacklist"]:
                                      kb.kickoutFromGroup(op.param1,[op.param2])
                                      kb.inviteIntoGroup(op.param1,[Zmid])
                                      cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                              except:
                                  try:
                                      if op.param3 not in wait["blacklist"]:
                                          kd.kickoutFromGroup(op.param1,[op.param2])
                                          kd.inviteIntoGroup(op.param1,[Zmid])
                                          cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                  except:
                                      try:
                                          if op.param3 not in wait["blacklist"]:
                                              ke.kickoutFromGroup(op.param1,[op.param2])
                                              ke.inviteIntoGroup(op.param1,[Zmid])
                                              cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                      except:
                                          try:
                                              if op.param3 not in wait["blacklist"]:
                                                  kf.kickoutFromGroup(op.param1,[op.param2])
                                                  kf.inviteIntoGroup(op.param1,[Zmid])
                                                  cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                          except:
                                              try:
                                                  if op.param3 not in wait["blacklist"]:
                                                      kg.kickoutFromGroup(op.param1,[op.param2])
                                                      kg.inviteIntoGroup(op.param1,[Zmid])
                                                      cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                              except:
                                                  try:
                                                      if op.param3 not in wait["blacklist"]:
                                                          kh.kickoutFromGroup(op.param1,[op.param2])
                                                          kh.inviteIntoGroup(op.param1,[Zmid])
                                                          cl.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                                  except:
                                                      try:
                                                          if op.param3 not in wait["blacklist"]:
                                                              cl.kickoutFromGroup(op.param1,[op.param2])
                                                              cl.inviteIntoGroup(op.param1,[Zmid])
                                                              ki.sendMessage(op.param1, "🇦🇱JΔΠGΔΠ DI CΔΠCΣL CUΨ ҜPΔҜSΔ ΔIM CIPΩҜ🇦🇱")
                                                      except:
                                                         pass
              return
#___________________________________________________________________
        if op.type == 19:
            if op.param1 in protect["proall"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in wait["blacklist"]:
                        pass
                    else:
                        random.coice(ABC).findAndAddContactsByMid(op.param3)                       
                        wait["blacklist"][op.param2] = True

            if op.param1 in protect["protect"]:
                if op.param2 in Bots:
                    pass
                elif op.param2 in owner:
                    pass
                elif op.param2 in admin:
                    pass
                elif op.param2 in staff:
                    pass
                elif op.param2 in Bots:
                    pass
                else:
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    
            if op.param1 in protect["antijs"]:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    elif op.param2 in Bots:
                        pass
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    else:
                        kj.acceptGroupInvitation(op.param1)
                        sw.acceptGroupInvitation(op.param1)
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kj.kickoutFromGroup(op.param1,[op.param2])
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = True
                        sw.updateGroup(G)
                        wait["blacklist"][op.param2] = True
                        sw.leaveGroup(op.param1)
                        kj.leaveGroup(op.param1)
                        cl.inviteIntoGroup(op.param1,[Jmid,Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
            try:
                if op.param3 in owner:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in admin:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                if op.param3 in staff:
                    if op.param2 in Bots:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in staff:
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                    elif op.param2 in owner:
                        pass
                    elif op.param2 in admin:
                        pass
                    elif op.param2 in staff:
                        pass
                    elif op.param2 in Bots:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        if op.param2 in Bots:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True              
            except:
                pass
                
        if op.type == 25 or op.type == 26:
          if settings['SpamInvite'] == True:
            msg = op.message
            sender = msg._from
            receiver = msg.to
            if msg.contentType == 13:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendMessage(msg.to, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ki.findAndAddContactsByMid(target)                                
                                kk.findAndAddContactsByMid(target)
                                kc.findAndAddContactsByMid(target)
                                kb.findAndAddContactsByMid(target)
                                kd.findAndAddContactsByMid(target)
                                ke.findAndAddContactsByMid(target)
                                kf.findAndAddContactsByMid(target)
                                kg.findAndAddContactsByMid(target)
                                kh.findAndAddContactsByMid(target)
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT                                
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT                                
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT                                
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kk.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kc.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kb.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kb.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kd.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kd.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ke.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                ke.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kf.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kf.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kg.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kg.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                kh.createGroup("TES BOT PUBLIK",[target]) # HANYA SPAM VIA CONTACT 
                                ki.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kk.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kc.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kb.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kd.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                ke.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kf.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kg.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                kh.sendMessage(msg.to, "Spam Invite ke " + korban + "\nSUCCESS..")
                                settings['SpamInvite'] = False
                            except:             
                                 cl.sendMessage(msg.to, 'Contact error')
                                 settings['SpamInvite'] = False
                                 break
                                 
        if op.type == 26:
            try:
                msg = op.message
                text = str(msg.text)
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                terminal = command(text)
                for terminal in terminal.split(" & "):
                    setKey = settings["keyCommand"].title()
                    if settings["setKey"] == False:
                        setKey = ''
                    if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                        if msg.toType == 0:
                            if sender != cl.profile.mid:
                                to = sender
                            else:
                                to = receiver
                        elif msg.toType == 1:
                            to = receiver
                        elif msg.toType == 2:
                            to = receiver
                        if msg.contentType == 0:
                            if to in offbot:
                                return
                        elif msg.contentType == 16:
                            if settings["checkPost"] == True:
                                try:
                                    ret_ = "Details Post"
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        contact = cl.getContact(sender)
                                        auth = "\nPenulis : {}".format(str(contact.displayName))
                                    else:
                                        auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                    purl = "\nURL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                    ret_ += auth
                                    ret_ += purl
                                    if "mediaOid" in msg.contentMetadata:
                                        object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                        if msg.contentMetadata["mediaType"] == "V":
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                                murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                            ret_ += murl
                                        else:
                                            if msg.contentMetadata["serviceType"] == "GB":
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            else:
                                                ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        ret_ += ourl
                                    if "stickerId" in msg.contentMetadata:
                                        stck = "\nStiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                        ret_ += stck
                                    if "text" in msg.contentMetadata:
                                        text = "\nTulisan :\n{}".format(str(msg.contentMetadata["text"]))
                                        ret_ += text
                                    ret_ += "\nFinish"
                                    cl.sendMessage(to, str(ret_))
                                except:
                                    sendTextTemplate(to, "Post tidak valid")
                            if msg.toType in (2,1,0):
                                purl = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                                adw = cl.likePost(purl[0], purl[1], random.choice([1001,1002,1003,1004,1005]))
                                adws = cl.createComment(purl[0], purl[1], settings["commentPost"])
                                sendTextTemplate(to, "Done Like Boss !")
            except Exception as error:
                logError(error)
#==========================================================================================================    
        if op.type in [25, 26]:           
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != mid: to = sender
                else: to = receiver
                #if receiver in temp_flood:
                    #if temp_flood[receiver]["expire"] == True:
                        #if cmd == "open" and sender == mid:
                            #temp_flood[receiver]["expire"] = False
                            #temp_flood[receiver]["time"] = time.time()
                            #cl.sendMessage(to, "Bot kembali aktif")
                        #return
                    #elif time.time() - temp_flood[receiver]["time"] <= 5:
                        #temp_flood[receiver]["flood"] += 1
                        #if temp_flood[receiver]["flood"] >= 20:
                            #temp_flood[receiver]["flood"] = 0
                            #temp_flood[receiver]["expire"] = True
                            #ret_ = "Spam terdeteksi, Bot akan silent selama 30 detik pada ruangan ini atau ketik {}Open untuk mengaktifkan kembali.".format(setKey)
                            #cl.sendMessage(to, str(ret_))
                    #else:
                         #temp_flood[receiver]["flood"] = 0
                         #temp_flood[receiver]["time"] = time.time()
                #else:
                    #temp_flood[receiver] = {
    	                #"time": time.time(),
    	                #"flood": 0,
    	                #"expire": False
                    #}
#____________________________________________________________________                
        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 55:            
            try:
                if op.param1 in read["readPoint"]:
                    if op.param2 in read["readMember"][op.param1]:
                        pass
                    else:
                        read["readMember"][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = cl.getContact(op.param2)
                        data = {
                                "type": "flex",
                                "altText": "sider",
                                "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "Terciduk",
            "size": "xl",
            "weight": "bold",
            "wrap": True,
            "color": "#FFFF00",
            "align": "center"
          },
          {
            "type": "text",
            "text": "Sini sob gabung chat..biar ramai nih room",
            "size": "md",
            "weight": "bold",
            "color": "#40E0D0",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF00FF"
    },
    "header": {
      "backgroundColor": "#FF00FF"
    }
  },  
  "hero": {
    "type": "image",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(op.param2).pictureStatus),
    "size": "full",
    "margin": "xxl"
  },
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "CREATOR",
        "size": "xxl",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      }
    ]
  },
  "header": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(cl.getContact(op.param2).displayName),
        "size": "md",
        "wrap": True,
        "weight": "bold",
        "color": "#F0F8FF",
        "align": "center"
      }
    ]
  }
}
}
                        cl.postTemplate(op.param1, data);

            if msg.contentType == 16:
                       url = msg.contentMetadata["postEndUrl"]
                       cl.like(url[25:58], url[66:], likeType=1001)
                       ki.like(url[25:58], url[66:], likeType=1001)
                       kk.like(url[25:58], url[66:], likeType=1001)
                       cl.comment(url[25:58], url[66:], wait["comment"])
                       cl.comment(url[25:58], url[66:], wait["comment"])
                       ki.comment(url[25:58], url[66:], wait["comment"])
                       kk.comment(url[25:58], url[66:], wait["comment"])                 
        
                                                        
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          cl.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              ki.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              try:
                                  kk.kickoutFromGroup(msg.to, [msg._from])
                              except:
                                  try:
                                  	kc.kickoutFromGroup(msg.to, [msg._from])
                                  except:
                                      try:
                                      	kb.kickoutFromGroup(msg.to, [msg._from])
                                      except:
                                          try:
                                          	kd.kickoutFromGroup(msg.to, [msg._from])
                                          except:
                                              try:
                                              	ke.kickoutFromGroup(msg.to, [msg._from])
                                              except:
                                                  try:
                                                  	kf.kickoutFromGroup(msg.to, [msg._from])
                                                  except:
                                                      pass


               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   #name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           sendTextTemplateku(msg.to, wait["Respontag"])
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   #name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           #cl.mentiontag(msg.to,[msg._from])
                           sendTextTemplate4(msg.to, "No tag me....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#=======================================================================
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots&media
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["AddstickerTag"]["status"] == True:
                         settings["AddstickerTag"]["sid"] = msg.contentMetadata["STKID"]
                         settings["AddstickerTag"]["spkg"] = msg.contentMetadata["STKPKGID"]
                         cl.sendMessage(msg.to, "Sticker respon hasben changed")
                         settings["AddstickerTag"]["status"] = False
                         
               if msg.contentType == 2:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','video.mp4')
                            cl.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in admin:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            cl.downloadObjectMsg(msg_id,'path','image.jpg')
                            cl.nadyacantikimut('video.mp4','image.jpg')
                            cl.sendMessage(msg.to,"Change Video Profile Success!!!")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah") 
                        elif Emid in Setmain["ARfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")   
                        elif Fmid in Setmain["ARfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")     
                        elif Gmid in Setmain["ARfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")       
                        elif Hmid in Setmain["ARfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")        
                        elif Imid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Imid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Jmid]
                            kj.updateProfilePicture(path)
                            kj.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     path5 = kd.downloadObjectMsg(msg_id)
                     path6 = ke.downloadObjectMsg(msg_id)
                     path7 = kf.downloadObjectMsg(msg_id)
                     path8 = kg.downloadObjectMsg(msg_id)
                     path9 = kh.downloadObjectMsg(msg_id)
                     path10 = kj.downloadObjectMsg(msg_id)
                     path11 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path3)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path3)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path3)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path3)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kg.updateProfilePicture(path3)
                     kg.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kh.updateProfilePicture(path3)
                     kh.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kj.updateProfilePicture(path3)
                     kj.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path3)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                            
               if msg.contentType == 1:
                  if msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = cl.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      cl.sendChatChecked(msg.to, msg_id)
                      print ("Read")
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                          if msg._from in mid:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               cl.sendSticker(to, spkg, sid)
                         for image in images:
                          if msg._from in mid:
                            if text.lower() == image:
                               cl.sendImage(msg.to, images[image])
                         for audio in audios:
                          if msg._from in mid:
                            if text.lower() == audio:
                               cl.sendAudio(msg.to, audios[audio])
                         for video in videos:
                          if msg._from in mid:
                            if text.lower() == video:
                               cl.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Succes add to staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes expel to staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Succes Add to Admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Succes to expel admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in owner:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Nothing in Talkban")
#UPDATE FOTO
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")


               if msg.contentType == 1:
                 if msg._from in owner:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes change pict group")


               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == ".help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage = help()
                               sendTextTemplate3(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                sendTextTemplate(msg.to, "Bot telah di aktifkan")
                                
                        elif cmd == "off":
                            if msg._from in owner or msg._from in admin:
                                wait["selfbot"] = False
                                sendTextTemplate(msg.to, "Bot off smentara waktu")
                                
                        elif cmd == 'vp':
                        	if msg._from in owner or msg._from in admin:
                                 me = cl.getContact(mid)
                                 cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                                            
                        elif cmd == ".help2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               helpMessage2 = helpbot()
                               sendTextTemplate3(msg.to, str(helpMessage2))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "   Pandawa\n\n"
                                if wait["sticker"] == True: md+="【✔】Sticker\n"
                                else: md+="【✘】Sticker\n"
                                if wait["contact"] == True: md+="【✔】Contact\n"
                                else: md+="【✘】Contact\n"
                                if wait["detectMention"] == True: md+="【✔】Respon\n"
                                else: md+="【✘】Respon\n"
                                if wait["autoJoin"] == True: md+="【✔】Autojoin\n"
                                else: md+="【✘】Autojoin\n"
                                if settings["autoJoinTicket"] == True: md+="【✔】Jointicket\n"
                                else: md+="【✘】Jointicket\n"
                                if settings["unsendMessage"] == True: md+="【✔】Unsend\n"
                                else: md+="【✘】Unsend\n"
                                if wait["autoAdd"] == True: md+="【✔】Autoadd\n"
                                else: md+="【✘】Autoadd\n"
                                if msg.to in welcome: md+="【✔】Welcome\n"
                                else: md+="【✘】Welcome\n"
                                if wait["autoLeave"] == True: md+="【✔】Autoleave\n"
                                else: md+="【✘】Autoleave\n"
                                if msg.to in protect["pqr"]: md+="【✔】Skurl\n"
                                else: md+="【✘】Skurl\n"
                                if msg.to in protect["proall"]: md+="【✔】Proall\n"
                                else: md+="【✘】Proall\n"
                                if msg.to in protect["protect"]: md+="【✔】Protect\n"
                                else: md+="【✘】Protect\n"
                                if msg.to in protect["pinv"]: md+="【✔】Skinvite\n"
                                else: md+="【✘】Skinvite\n"
                                if msg.to in protect["antijs"]: md+="【✔】Js\n"
                                else: md+="【✘】Js\n"
                                if msg.to in protectcancel: md+="【✔】Procancel\n"
                                else: md+="【✘】Procancel\n"
                                sendTextTemplate3(msg.to, md+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")

                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "   Pandawa\n\n"
                                if wait["sticker"] == True: md+="【✔】Sticker\n"
                                else: md+="【✘】Sticker\n"
                                if wait["contact"] == True: md+="【✔】Contact\n"
                                else: md+="【✘】Contact\n"
                                if wait["detectMention"] == True: md+="【✔】Respon\n"
                                else: md+="【✘】Respon\n"
                                if wait["autoJoin"] == True: md+="【✔】Autojoin\n"
                                else: md+="【✘】Autojoin\n"
                                if settings["autoJoinTicket"] == True: md+="【✔】Jointicket\n"
                                else: md+="【✘】Jointicket\n"
                                if settings["unsendMessage"] == True: md+="【✔】Unsend\n"
                                else: md+="【✘】Unsend\n"
                                if wait["autoAdd"] == True: md+="【✔】Autoadd\n"
                                else: md+="【✘】Autoadd\n"
                                if msg.to in welcome: md+="【✔】Welcome\n"
                                else: md+="【✘】Welcome\n"
                                if wait["autoLeave"] == True: md+="【✔】Autoleave\n"
                                else: md+="【✘】Autoleave\n"
                                if msg.to in protect["pqr"]: md+="【✔】Protecturl\n"
                                else: md+="【✘】Protecturl\n"
                                if msg.to in protect["proall"]: md+="【✔】Proall\n"
                                else: md+="【✘】Proall\n"
                                if msg.to in protect["protect"]: md+="【✔】Protect\n"
                                else: md+="【✘】Protect\n"
                                if msg.to in protect["pinv"]: md+="【✔】Protectinvite\n"
                                else: md+="【✘】Protectinvite\n"
                                if msg.to in protect["antijs"]: md+="【✔】Js\n"
                                else: md+="【✘】Js\n"
                                if msg.to in protectcancel: md+="【✔】Procancel\n"
                                else: md+="【✘】Procancel\n"
                                if msg.to in ghost: md+="【✔】Ghost\n"
                                else: md+="【✘】Ghost\n"
                                if msg.to in protectkick: md+="【✔】Protectkic\n"
                                else: md+="【✘】Protectkick\n"
                                sendTextTemplate3(msg.to, md+"\nDate : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")                              

                        elif cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "【✔】Key\n"
"【✔】Key1\n"
"【✔】Key2\n"
"【✔】Key3\n"
"【✔】Protect\n"
"【✔】Menu\n"
"【✔】Like @\n"
"【✔】Creator\n"
"【✔】Order\n"
"【✔】Team\n"
"【✔】Kibar tmp\n"
"【✔】Gass tmp\n"
"【✔】Bcast:「Text」\n"
"【✔】Bc1:「Text」\n"
"【✔】Bc2:「Text」\n"
"【✔】Bc3:「Text」\n"
"【✔】Bc4:「Text」\n"
"【✔】Sticker1\n"
"【✔】Sticker2")

                        elif cmd == "sticker1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "「🔑]Menu Sticker\n"
"【✔】Sepi\n"
"【✔】Kampret\n"
"【✔】Wkwk\n"
"【✔】Malas\n"
"【✔】Kifli\n"
"【✔】Creator\n"
"【✔】Welcome\n"
"【✔】Apa\n"
"【✔】Maju\n"
"【✔】Asem\n"
"【✔】Cinta\n"
"【✔】Cium\n"
"【✔】Sedih\n"
"【✔】Hah\n"
"【✔】Sue\n"
"【✔】Hade")


                        elif cmd == "sticker2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "「🔑]Menu Sticker\n"
"【✔】Sunyi\n"
"【✔】Asslam\n"
"【✔】Masuk\n"
"【✔】Kabur\n"
"【✔】Obat\n"
"【✔】Baik\n"
"【✔】Naik\n"
"【✔】Cuek\n"
"【✔】Ngambek\n"
"【✔】Makasih\n"
"【✔】Sue\n"
"【✔】Jomblo\n"
"【✔】Sedih")

                        elif cmd == "protect":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "              「🔑]Menu Protect\n"
"【✔】Spaminvite on \n"
"【✔】Spaminvite off \n"
"【✔】Protectkick on\off\n"
"【✔】Protectinvite on\off\n"
"【✔】Protectjoin on\off\n"
"【✔】Protectcancel on\off\n"
"【✔】Stay\n"
"【✔】Js on\off\n"
"【✔】Ghost on\off")

                        elif cmd == "key":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "「🔑]PANDAWA\n"
"【✔】Me\n"
"【✔】Sp\n"
"【✔】Mybot\n"
"【✔】Kepo @\n"
"【✔】Get id @\n"
"【✔】Settings\n"
"【✔】Name\n"
"【✔】Get mid @\n"
"【✔】About\n"
"【✔】Cpp\n"
"【✔】time\n"
"【✔】Creator\n"
"【✔】Ginfo @\n"
"【✔】Open\n"
"【✔】Close\n"
"【✔】Url grup\n"
"【✔】Glist\n"
"【✔】Stafflist\n"
"【✔】Botlist\n"
"【✔】Hapus chat\n"
"【✔】Sider on\off\n"
"【✔】Upfoto\n"
"【✔】Upgrup\n"
"【✔】Bcast:「Text」\n"
"【✔】Set name\n"
"【✔】Spesan: text\n"
"【✔】Swelcome: text\n"
"【✔】Ssider: text\n"
"【✔】Srepson: text\n"
"【✔】Sider on\off\n"
"【✔】Cpesan/off\n"
"【✔】Crespon\n"
"【✔】Cwelcome\n"
"【✔】Sticker「on/off\n"
"【✔】Respon「on/off」\n"
"【✔】Unsend「on/off] ")

                        elif cmd == "key1":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "【✔】「Autoblock on\off\n"
"【✔】「Welcome on\off\n"
"【✔】「Joox judul penyany\n"
"【✔】「Ytmp3: Judul lagu\n"
"【✔】「Ytmp4: Judul lagu\n"
"【✔】「Changedual \n"
"【✔】「Changedualurl: •link•\n"
"【✔】「Img food: produk\n"
"【✔】「Profilesmule: id\n"
"【✔】「Profileig: id\n"
"【✔】「Meme@nama@kata1@kata2\n"
"【✔】「Addimg •nama•\n"
"【✔】「Dellimg •nama•\n"
"【✔】「Listimg •nama•\n"
"【✔】「Addvideo •nama•\n"
"【✔】「Dellvideo •nama•\n"
"【✔】「Listvideo •nama•\n"
"【✔】「Addsticker •nama•\n"
"【✔】「Dellsticker •nama•\n"
"【✔】「Liststicker •nama•\n"
"【✔】「Addaudio •nama•\n"
"【✔】「Dellaudio •nama•\n"
"【✔】「Listaudio •nama•\n"
"【✔】「Kick @\n"
"【✔】「Vc @ \n"
"【✔】「Mainkan @\n"
"【✔】「Invite \n"
"【✔】「Bl \n"
"【✔】「Refresh \n"
"【✔】「Gas \n"
"【✔】「Killban \n"
"【✔】「Banlist\n"
"【✔】「Ban all\n"
"【✔】「Clearban")


                        elif cmd == "key2":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "[PandawaBot]\n"
"【✔】「Admin:on @\n"
"【✔】「Adminadd @\n"
"【✔】「Admindell @\n"
"【✔】「Staffadd @\n"
"【✔】「Staffdell @\n"
"【✔】「Botadd @\n"
"【✔】「Botdell @\n"
"【✔】「Owner:on\n"
"【✔】「Staff:on\n"
"【✔】「Staff:on @\n"
"【✔】「Staffexpl:on\n"
"【✔】「Bot:on\n"
"【✔】「Bot:off\n"
"【✔】「Ban:on @\n"
"【✔】「Unban:on @\n"
"【✔】「Talkban:on @\n"
"【✔】「Untalkban:on @\n"
"【✔】「Talkbanlist\n"
"【✔】「.Bye/Bye[1/4]\n"
"【✔】「Leave「Namagrup」\n"
"【✔】「Ghost「in」\n"
"【✔】「Ghost「out」\n"
"【✔】「Infogrup「angka」\n"
"【✔】「Infomem「angka」\n"
"【✔】「Autojointicket on/off\n"
"【✔】「Pasukan [kickall]")
                               
                        elif cmd == "key3":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate3(msg.to, "「🔑]Bc1:,2,3,4 [text]\n"
"【✔】「Midku\n"
"【✔】「Midbot\n"
"【✔】「Youtube judul\n"
"【✔】「Bcast: [text]\n"
"【✔】「Bubar [kickall]\n"
"【✔】「Gass [kickall]\n"
"【✔】「Harga\n"
"【✔】「Reinvite\n"
"【✔】「Time\n"
"【✔】「Reject\n"
"【✔】「Name\n"
"【✔】「Respon\n"
"【✔】「Autojoin on/off\n"
"【✔】「Jointicket on/off\n"
"【✔】「Autoadd on/off\n"
"【✔】「leave on/off\n"
"【✔】「Youtube judul\n"
"【✔】「Ghost in\n"
"【✔】「Cek kesehatan\n"
"【✔】「Allpro on\n"
"【✔】「Kibar tmp[kickall]\n"
"【✔】「Ytmp4: Judul \n"
"【✔】「Pandawa [kickall]")

                        elif cmd.startswith("mid "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)

                               
                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendMention(msg.to, sender, "🔴My Creator\n\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == ".me" or text.lower() == ',me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:                                               
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': msg._from}
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                                path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                                image = 'http://dl.profile.line.naver.jp'+path
                                cl.sendImageWithURL(msg.to, image)
                                                                       
                        elif text.lower() == "midku":
                               sendTextTemplate(msg.to, msg._from)
                        elif text.lower() == 'ass':
                               sendTextTemplate(msg.to, "Assalamu'alaikum Wr. Wb")
                               sendTextTemplate(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")
                        elif text.lower() == 'wss':
                               sendTextTemplate(msg.to, "Wa'alaikumsallam.Wr,Wb")
                               sendTextTemplate(msg.to, "ُوَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")
                        elif text.lower() == 'bot':
                               sendTextTemplateku(msg.to, "Bot Hadir om")

                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate3(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Kepo " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               sendTextTemplate3(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd  == "mybot":
                          if msg._from in admin:
                              cl.sendContact(to, mid)
                              cl.sendContact(to, Amid)
                              cl.sendContact(to, Bmid)
                              cl.sendContact(to, Cmid)
                              cl.sendContact(to, Dmid)
                              cl.sendContact(to, Emid)
                              cl.sendContact(to, Fmid)
                              cl.sendContact(to, Gmid)
                              cl.sendContact(to, Hmid)
                              cl.sendContact(to, Imid)
                              cl.sendContact(to, Jmid)
                              cl.sendContact(to, Zmid)
                               
                        elif cmd  == "midbot":
                          if msg._from in admin:
                              cl.sendMessage(msg.to,mid)
                              ki.sendMessage(msg.to,Amid)
                              kk.sendMessage(msg.to,Bmid)
                              kc.sendMessage(msg.to,Cmid)
                              kb.sendMessage(msg.to,Dmid)
                              kd.sendMessage(msg.to,Emid)
                              ke.sendMessage(msg.to,Fmid)
                              kf.sendMessage(msg.to,Gmid)
                              kg.sendMessage(msg.to,Hmid)
                              kh.sendMessage(msg.to,Imid)
                              cl.sendMessage(msg.to,Jmid)
                              cl.sendMessage(msg.to,Zmid)
                               
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                      ki.rejectGroupInvitation(gid)
                                      ka.rejectGroupInvitation(gid)
                                  sendTextTemplate(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  sendTextTemplate(to, "sᴇᴍᴜᴀ ɢʀᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴀᴛᴀʟᴋᴀɴ")

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   kj.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   sendTextTemplate(msg.to,"Bersih bos")
                               except:
                                   pass

                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   sendTextTemplateku(group,"🔴Broadcast \n\n" + str(pesan))

                        elif text.lower() == "sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               sendTextTemplate(msg.to, "🔴 Sname \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("setsname "):
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   sendTextTemplate(msg.to, "Succes change Sname")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   sendTextTemplate3(msg.to, "🔴Sname change \n\nSname succes change to {}".format(str(key).lower()))

                        elif text.lower() == "reset sname":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               Setmain["keyCommand"] = ""
                               sendTextTemplate(msg.to, "Succes Reset Sname ")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               cl.sendMessage(msg.to, "please wait")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               sendTextTemplate(msg.to, "Done...")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               sendTextTemplate(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                sendTextTemplate3(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                sendTextTemplate(msg.to, str(e))

                        elif cmd == "team":
                                with open("team.json","r") as f:
                                    data = json.load(f)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                            if len(ret_) >= 20:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "{}".format(str(fn["name"])),
                                                        "uri": "{}".format(str(fn["linkliff"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                                "type": "template",
                                                "altText": "Help Message",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": ret_[aa*10 : (aa+1)*10]
                                                }
                                            }
                                        cl.postTemplate(to, data)
                                        
                        elif cmd == "menu":
                                with open("help.json","r") as f:
                                    data = json.load(f)
                                if data["result"] != []:
                                    ret_ = []
                                    for fn in data["result"]:
                                            if len(ret_) >= 20:
                                                pass
                                            else:
                                                ret_.append({
                                                    "imageUrl": "{}".format(str(fn["link"])),
                                                    "action": {
                                                        "type": "uri",
                                                        "label": "{}".format(str(fn["name"])),
                                                        "uri": "{}".format(str(fn["linkliff"]))
                                                        }
                                                    }
                                                )
                                    k = len(ret_)//10
                                    for aa in range(k+1):
                                        data = {
                                                "type": "template",
                                                "altText": "Help Message",
                                                "template": {
                                                    "type": "image_carousel",
                                                    "columns": ret_[aa*10 : (aa+1)*10]
                                                }
                                            }
                                        cl.postTemplate(to, data)
                                        
                        elif cmd == "me":
                                contact = cl.getProfile()
                                mids = [contact.mid]
                                status = cl.getContact(sender)                               	
                                data = {
                                        "type": "flex",
                                        "altText": "Me Message",
                                        "contents": {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "flex": 2,
        "contents": [
          {
            "type": "text",
            "text": "PANDAWABOT",
            "size": "md",
            "weight": "bold",
            "wrap": True,
            "color": "#7FFF00"
          },
          {
            "type": "text",
            "text": "{}".format(status.statusMessage),
            "align": "center",
            "size": "sm",
            "weight": "bold",
            "color": "#FF00FF",
            "wrap": True
          }
        ]
      }
    ]
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#FF1493"
    },
    "header": {
      "backgroundColor": "#FF1493"
    }
  },  
  "footer": {
    "type": "box",   
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "ORDER",
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "action": {
          "type": "uri",
          "uri": "http://line.me/ti/p/~tetsunaki"
        },
        "align": "center"
      }
    ]
  },
  "hero": {
    "aspectMode": "cover",
    "aspectRatio": "20:13",
    "type": "image",
    "url": "https://obs.line-scdn.net/{}".format(cl.getContact(sender).pictureStatus),
    "size": "full",
    "align": "center",
  },
  "header": {
    "type": "box",   
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "{}".format(status.displayName),
        "size": "xl",
        "wrap": True,
        "weight": "bold",
        "color": "#FFD700",
        "align": "center"
      }
    ]
  }
}
}
                                cl.postTemplate(to, data)

                        elif cmd == "order":
                            if msg._from in admin:
                                saya = cl.getGroupIdsJoined()
                                for groups in saya:
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/M6YPtGn/1547611926518.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~tetsunaki",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "「OPEN ORDER」",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "SelfBot",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "50k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "SB+3Asist+1Ghost/Antijs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "SB+5Asist+1Ghost/Antijs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "Protect Room Smule & Event",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CLICK HERE",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PANDAWA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"                            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                                    cl.postFlex(groups, data)

                        elif cmd == "promo":
                            if msg._from in admin:
                                saya = cl.getGroupIdsJoined()
                                for groups in saya:
                                    data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.ibb.co/M6YPtGn/1547611926518.jpg",
        "action": {
          "uri": "http://line.me/ti/p/~tetsunaki",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#00008B"
        },
        "header": {
          "backgroundColor": "#00008B"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "text": "「OPEN ORDER」",
            "color": "#00FFFF",
            "wrap": True,
            "weight": "bold",
            "type": "text",
            "size": "lg",
            "align": "center"
          },
          {
            "type": "separator",
            "color": "#6F4E37"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "SelfBot",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          
          {
            "text": "50k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "SB+3Asist+1Ghost/Antijs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "SB+5Asist+1Ghost/Antijs",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "250k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          },
          {
            "contents": [
              {
                "contents": [
                  {
                    "size": "xl",
                    "type": "icon",
                    "url":"https://i.ibb.co/W3Nsdx1/1547610440856.jpg",
                  },
                  {
                    "text": "Protect Room Smule & Event",
                    "color": "#FFFF00",
                    "flex": 0,
                    "weight": "bold",
                    "type": "text",
                    "margin": "none"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "text": "200k/Bln",
            "size": "xs",
            "align": "end",
            "color": "#00FF00",
            "wrap": True,
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "CLICK HERE",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PANDAWA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"                            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}

                                    cl.postFlex(groups, data)
                                
                        elif cmd.startswith("bc1: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.pinimg.com/originals/fd/47/e5/fd47e55dfb49ae1d39675d6eff34a729.gif",
        "action": {
          "uri": "http://line.me/ti/p/~tetsunaki",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF1493"
        },
        "header": {
          "backgroundColor": "#FF1493"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BRODCAST",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FF00FF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PANDAWA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   cl.postFlex(group, data)

                        elif cmd.startswith("bc2: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://2.bp.blogspot.com/-OoippIonQX4/WDZymmRdW2I/AAAAAAADyf4/2oXRHOOcMGEt2tqxLCCB1YEl66WTLIwcgCLcB/s1600/AS000681_20.gif",
        "action": {
          "uri": "http://line.me/ti/p/~tetsunaki",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF1493"
        },
        "header": {
          "backgroundColor": "#FF1493"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BRODCAST",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FF00FF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PANDAWA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   cl.postFlex(group, data)

                        elif cmd.startswith("bc3: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://i.pinimg.com/originals/e7/79/e6/e779e6cde47381c840846a16a4eb063d.gif",
        "action": {
          "uri": "http://line.me/ti/p/~tetsunaki",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF1493"
        },
        "header": {
          "backgroundColor": "#FF1493"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BRODCAST",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FF00FF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "PANDAWA",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   cl.postFlex(group, data)


                        elif cmd.startswith("bc4: "):
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   data = {
  "contents": [
    {
      "hero": {
        "aspectMode": "cover",
        "url": "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage",
        "action": {
          "uri": "http://line.me/ti/p/~tetsunaki",
          "type": "uri"
        },
        "type": "image",
        "size": "full"
      },
      "styles": {
        "body": {
          "backgroundColor": "#000000"
        },
        "footer": {
          "backgroundColor": "#FF1493"
        },
        "header": {
          "backgroundColor": "#FF1493"
        }
      },
      "type": "bubble",
      "body": {
        "contents": [
          {
            "contents": [
              {
                "contents": [
                  {
                    "text": pesan,
                    "color": "#FF0000",
                    "wrap": True,
                    "weight": "bold",
                    "type": "text",
                    "size": "lg",
                    "align": "center"
                  }
                ],
                "type": "box",
                "layout": "baseline"
              }
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical"
      },
      "type": "bubble",
      "footer": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "BRODCAST",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FF00FF",
            "action": {
              "type": "uri",
              "uri": "http://line.me/ti/p/~tetsunaki"
            },
            "align": "center"            
          }
        ]
      },
      "type": "bubble",
      "header": {
        "type": "box",   
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Pandawa",
            "size": "xl",
            "wrap": True,
            "weight": "bold",
            "color": "#FFFFFF",
            "align": "center"            
          }
        ]
      }
    }
  ],
  "type": "carousel"
}
                                   cl.postFlex(group, data)
                                   
                        elif cmd.startswith("joox"):
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                data = {
                                        "type": "flex",
                                        "altText": "Musik",
                                        "contents": {
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#9932CC"
    }
  },
  "type": "bubble",
  "body": {
    "contents": [
      {
        "contents": [
          {
            "url": g,
            "type": "image"
          },
          {
            "type": "separator",
            "color": "#FF0000"
          },
          {
            "text": "Pandawa-Bot\n\nMP3",
            "size": "sm",
            "color": "#FF0000",
            "wrap": True,
            "weight": "bold",
            "type": "text"
          }
        ],
        "type": "box",
        "spacing": "md",
        "layout": "horizontal"
      },
      {
        "type": "separator",
        "color": "#800080"
      },
      {
        "contents": [
          {
            "contents": [
              {
                "text": hasil,
                "size": "xs",
                "margin": "none",
                "color": "#FF6347",
                "wrap": True,
                "weight": "regular",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "vertical"
      }
    ],
    "type": "box",
    "spacing": "md",
    "layout": "vertical"
  },
  "footer": {
    "contents": [
      {
        "contents": [
          {
            "contents": [
              {
                "text": "PLAY di bawah",
                "size": "xxl",
                "weight": "bold",
                "action": {
                  "uri": e,
                  "type": "uri",
                  "label": "Audio"
                },
                "margin": "xl",
                "align": "start",
                "color": "#FFD700",
                "weight": "bold",
                "type": "text"
              }
            ],
            "type": "box",
            "layout": "baseline"
          }
        ],
        "type": "box",
        "layout": "horizontal"
      }
    ],
    "type": "box",
    "layout": "vertical"
  }
}
}
                                cl.postTemplate(to, data)
                                cl.sendAudioWithURL(to,e)
                            except Exception as error:
                                sendTextTemplate(to, "error\n" + str(error))
                                logError(error)
                         
                        elif "hah" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-W_bn2qqdYXE/Wyhbjj2wqKI/AAAAAAANIz4/KQVsbq-aXm0kZNfFOS5SN8fqCvQ18xnUACLcBGAs/s1600/AW1238502_03.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                        elif "sedih" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data) 
                        elif "hade" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/dJ1H13M/Benjol.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                        elif "sue" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/y0wP3fJ/tai-line.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "cium" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/f2/65/ed/f265ed4b3f708bd84d3f58b7dafd6b75.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "cinta" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/04/ca/f6/04caf6a76cdcd28d03618d45fb51debd.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "asem" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/04/ca/f6/04caf6a76cdcd28d03618d45fb51debd.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "maju" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://media0.giphy.com/media/eR7OEDQDyA7Cg/giphy.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "apa" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-ttFqfJGPCN4/WDZykgy-yPI/AAAAAAADyfs/WTuKOd-mMOg7PwBVbgivxNBvud0b2u6KwCLcB/s1600/AS000681_17.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "creator" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/5Y351sq/1550920210634.jpg",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "welcome" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://2.bp.blogspot.com/-OoippIonQX4/WDZymmRdW2I/AAAAAAADyf4/2oXRHOOcMGEt2tqxLCCB1YEl66WTLIwcgCLcB/s1600/AS000681_20.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "Lybee" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/5Y351sq/1550920210634.jpg",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "malas" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://2.bp.blogspot.com/-B3VYD8fyY9s/WDZyj9RA9lI/AAAAAAADyfk/IFXPFfnL25YcVnL2tNTgxpmlfUmxleMzgCLcB/s1600/AS000681_15.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "wkwk" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.pinimg.com/originals/9e/bb/f7/9ebbf7a320a06fb9a254b2f521bbd4ec.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                     
                        elif "kampret" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/CVMQ40k/7c8ab257ee3b7e1ef283b7c0a35d9d2c.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "sepi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://i.ibb.co/hHG5Mwb/AW316819-05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif "sedih" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-OfIz4mSIumw/WbLEZw7l6nI/AAAAAAARd6Y/Dxzos1SA_5MU32bXFTKToLDndM7YpV7WACLcBGAs/s1600/AW529310_04.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "jomblo" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-f1Ac9hha1NA/WE_QkvJGBEI/AAAAAAAFMuA/xNeS9_M2O0M3t2cv6YFjHSLlD8TcAW6GwCLcB/s1600/AW293929_02.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "sue" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-CXej0VEJkps/WDv1XSwipPI/AAAAAAALlNU/UjrTOos8KF86vkw05SE25bUkAQc86b2pwCLcB/s1600/AS001630_08.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
  
                        elif "makasih" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-DcGGuaPMWUk/WVRjBYIJa5I/AAAAAAAIo5k/YyEwYgikZa8p1d05X04bB3rhqCMgL52ewCLcBGAs/s1600/AS002777_01.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
       
                        elif "ngambek" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://mastergolflivestream.com/images/clipart-monkey-gif-animation-8.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
   
                        elif "cuek" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://mastergolflivestream.com/images/clipart-monkey-gif-animation-8.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
     
                        elif "naik" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-H6CCaBKZx80/WymRq9o_HMI/AAAAAAAgatE/TGJNvRBure4TBDdqFelwB0r4UE0FkGg7wCLcBGAs/s1600/AW1238435_06.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
     
                        elif "bye" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://2.bp.blogspot.com/-JYruBBpWAT8/WN5gF4SZvzI/AAAAAAAOTwA/cQm1k193EtY0Q5Bb7RpsX8px2mfaxsSMACLcB/s1600/AW400539_23.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
#####              
                        elif "obat" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-brGGfEhQiq8/WymK5LjZvlI/AAAAAAAgZ54/yiXZCOXNo_EMpqVm50ztSJJ0zvIbd4LgwCLcBGAs/s1600/AW1238279_05.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
  
                        elif "kabur" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://3.bp.blogspot.com/-cpA0qRAqi1k/WymK7QB3O-I/AAAAAAAgZ6I/hGoxo__H4yMEWk-K7WgShHTD__qY6Uf-ACLcBGAs/s1600/AW1238279_09.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
             
                        elif "masuk" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://1.bp.blogspot.com/-BexgMzXNxDg/WRpgX4uw1RI/AAAAAAAHjc0/IUIU2CiLZisdfcJGEZ2ofCKXfrEpbDeOACLcB/s1600/AS002623_07.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                           
                        elif "assalam" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://thumbs.gfycat.com/FirstPeriodicChimpanzee-size_restricted.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)
                                    
                        elif "sunyi" in msg.text.lower():
                                    url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/sendMessage"
                                    to = msg.to
                                    data = {
                                                "type": "template",
                                                "altText": "{} sent a sticker".format(cl.getProfile().displayName),
                                                "template": {
                                                   "type": "image_carousel",
                                                   "columns": [
                                                    {
                                                        "imageUrl": "https://4.bp.blogspot.com/-nJ4iMqsxTQc/WwJ97etgoiI/AAAAAAAIoGM/_mG-H0OhIPMLPdJ85ApFDB9Nzxqr_74IwCLcBGAs/s1600/AW1084508_09.gif",
                                                        "size": "full", 
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": "http://line.me/ti/p/~tetsunaki"
                                 }                                                
                       }
                      ]
                                                }
                                            }
                                    cl.postTemplate(to, data)

                        elif cmd.startswith("infogrup "):
                          if msg._from in owner or msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "Team Sempak Grup Info\n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                sendTextTemplate3(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave "):
                          if msg._from in owner or msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    cl.leaveGroup(i)
                                    sendTextTemplate3(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               sendTextTemplate3(msg.to,"??FRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")

                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               sendTextTemplate3(msg.to,"🔴GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   sendTextTemplate(msg.to, "Url Closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "upgrup":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                sendTextTemplate(msg.to,"Send Picture")                     

                        elif cmd == "cpp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                sendTextTemplate(msg.to,"Kirim fotonya.....")

                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARvideo"][mid] = True
                                sendTextTemplate(msg.to,"Kirim videonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                sendTextTemplate(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("get-mimpi "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            mimpi = msg.text.replace(sep[0] + " ","")  
                            with requests.session() as s:
                                s.headers['user-agent'] = 'Mozilla/5.0'
                                r = s.get("http://primbon.com/tafsir_mimpi.php?mimpi={}&submit=+Submit+".format(urllib.parse.quote(mimpi)))
                                soup = BeautifulSoup(r.content, 'html5lib')
                                for anu in soup.find_all('i'):
                                    ret_ = anu.get_text()
                                    sendTextTemplate(msg.to,ret_)

                        elif cmd == "restart2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.sendMention(msg.to, sender, "「 Restarting 」\nUser ", "\nTunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                settings["ARGfoto"][mid] = True
                                sendTextTemplate(msg.to,"Send picture")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["ARGfoto"][mid] = True
                                sendTextTemplate(msg.to,"Send picture")
                      
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                settings["ARfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                settings["ARfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                settings["ARfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                settings["ARfoto"][Dmid] = True
                                kb.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot5up":
                            if msg._from in admin:
                                settings["ARfoto"][Emid] = True
                                kd.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot6up":
                            if msg._from in admin:
                                settings["ARfoto"][Fmid] = True
                                ke.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot7up":
                            if msg._from in admin:
                                settings["ARfoto"][Gmid] = True
                                kf.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot8up":
                            if msg._from in admin:
                                settings["ARfoto"][Hmid] = True
                                kg.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "bot9up":
                            if msg._from in admin:
                                settings["ARfoto"][Imid] = True
                                kh.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot10up":
                            if msg._from in admin:
                                settings["ARfoto"][Jmid] = True
                                kj.sendMessage(msg.to,"Send picture")

                        elif cmd == "bot11up":
                            if msg._from in admin:
                                settings["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send picture")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")    
   
                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                kh.sendMessage(msg.to,"Nama diganti jadi " + string + "")       

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                kj.updateProfile(profile)
                                kj.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot11name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")


                        elif cmd == "reinvite":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                #kj.leaveGroup(msg.to)
                                #sw.leaveGroup(msg.to)
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                #kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                #sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                ki.updateGroup(G)

                        elif cmd == "stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Jmid,Zmid])
                                    sendTextTemplate(msg.to,"Grup 「"+str(ginfo.name)+"」 Aman Dari JS")
                                except:
                                    pass

                        elif "Gass" in msg.text:
                           if msg._from in Bots:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Gass","")
                               gs = ki.getGroup(msg.to)
                               gs = kk.getGroup(msg.to)
                               gs = kc.getGroup(msg.to) 
                               gs = kb.getGroup(msg.to)    
                               gs = kd.getGroup(msg.to)
                               gs = ke.getGroup(msg.to)
                               gs = kf.getGroup(msg.to)
                               gs = kg.getGroup(msg.to)
                               gs = kh.getGroup(msg.to)
                              #gs = #kj.getGroup(msg.to)
                              #gs = #sw.getGroup(msg.to)
                              # gs = #k3.getGroup(msg.to)
                               #gs = #k4.getGroup(msg.to)
                               #gs = #k5.getGroup(msg.to)
                              # gs = #k6.getGroup(msg.to)
                               #gs = #k7.getGroup(msg.to)
                               cl.sendMessage(to,"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ASSALAMUALAIKUM\n"
"  ╭━Ⓓ✒Ⓡ✒ⒼⓄ✒Ⓝ✒\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HLO▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MENGGUSUR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[██████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"👿━━━━━━━━━━━━━👿"
"Ⓣⓜⓟⓐ Ⓑⓐⓢⓐ_Ⓑⓐⓢⓘ\n"
"Ⓡⓐⓣⓐ ⓖⓐ ⓡⓐⓣⓐ\n" 
"Ⓨⓖ ⓟⓝⓣⓘⓝⓖ ⓚⓘⓑⓐⓡ\n"
"Ⓣⓐⓝⓖⓚⓘⓢ Ⓖⓞⓑⓛⓞⓚ\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗         ╔╦╗\n"
	"╚╗╗║         ║╔╝\n"
	"╔╩╝║         ║╚╗\n"
	"╚══╝         ╚╩╝\n"
"👿━━━━━━━━━━━━━👿\n"        
"Ⓓⓡⓐⓖⓞⓝ_Ⓚⓘⓛⓛⓔⓡ\n"
"Ⓟⓤⓝⓨⓐ👿━━👿Ⓡⓐⓣⓐ Ⓝⓘ\n" 
"Ⓜⓐⓗ━👿━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
">>>Ⓑⓨⓔ_Ⓑⓨⓔ ⒼⒸ Ⓛⓐⓚⓝⓐⓣ>><\nⒹⓝⓓⓐⓜ Ⓒⓐⓡⓘ Ⓚⓜⓘ\n<<<<<<<<<>>\nhttp://line.me/ti/p/~reza.p.i.p\nhttp://line.me/ti/p/~tetsunaki")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Bots:
                                      try:
                                          klist=[ki,kk,kc,kb,kd,ke,kf,kg,kh] #kj,sw]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          kc.sendMessage(msg.to,"I'm Sory")
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass


                        #elif cmd == "ghost in":
                            #if msg._from in admin:
                                #G = cl.getGroup(msg.to)
                                #ginfo = cl.getGroup(msg.to)
                               #G.preventedJoinByTicket = False
                                #cl.updateGroup(G)
                                #invsend = 0
                                #Ticket = cl.reissueGroupTicket(msg.to)
                                #kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                                #kj.sendMessage(msg.to, "Ghost masuk "+str(G.name))
                                #sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                #sw.sendMessage(msg.to, "Ghost masuk "+str(G.name))
                                #G = sw.getGroup(msg.to)
                                #G.preventedJoinByTicket = True
                                #sw.updateGroup(G)

                        #elif cmd == "ghost out":
                            #if msg._from in admin:
                                #G = cl.getGroup(msg.to)
                                #kj.sendMessage(msg.to, "Ghost dipaksah Out "+str(G.name))
                                #kj.leaveGroup#(msg.to)
                                #sw.sendMessage(msg.to, "Ghost dipaksah Out "+str(G.name))
                                #sw.leaveGroup(msg.to)

                        elif cmd == "cek kesehatan":
                            if msg._from in admin:
                                try:cl.inviteIntoGroup(to, ["u85f884a251b5bda40b68616c0c2b5692"]);has = "OK"
                                except:has = "NOT"
                                try:cl.kickoutFromGroup(to, ["u85f884a251b5bda40b68616c0c2b5692"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                cl.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:ki.inviteIntoGroup(to, ["u43ff627f8b7fb7f63fc5b109c06c21a9"]);has = "OK"
                                except:has = "NOT"
                                try:ki.kickoutFromGroup(to, ["u43ff627f8b7fb7f63fc5b109c06c21a9"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                ki.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kk.inviteIntoGroup(to, ["u53c22150dca9303128072e561640c3ac"]);has = "OK"
                                except:has = "NOT"
                                try:kk.kickoutFromGroup(to, ["u53c22150dca9303128072e561640c3ac"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kk.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kc.inviteIntoGroup(to, ["ufc4305c7942a70d9e5173e2f7cb3acd7"]);has = "OK"
                                except:has = "NOT"
                                try:kc.kickoutFromGroup(to, ["ufc4305c7942a70d9e5173e2f7cb3acd7"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kc.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kb.inviteIntoGroup(to, ["uc408ebe1b52285977ac7f772bca383ba"]);has = "OK"
                                except:has = "NOT"
                                try:kb.kickoutFromGroup(to, ["uc408ebe1b52285977ac7f772bca383ba"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kb.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kd.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kd.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kd.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:ke.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:ke.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                ke.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kf.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kf.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kf.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kg.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kg.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kg.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kh.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kh.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kh.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kj.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kj.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                kj.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:sw.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:sw.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "sehat"
                                else:sil = "sakit"
                                if has1 == "OK":sil1 = "sehat"
                                else:sil1 = "sakit"
                                sw.sendMessage(to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))

                        #elif cmd == "tmp kesehatan":
                            #if msg._from in admin:
                                #try:cl.inviteIntoGroup(to, ["uc5abb77929c76b5f91f4beaecd88e5e2"]);has = "OK"
                                #except:has = "NOT"
                                #try:cl.kickoutFromGroup(to, ["uc5abb77929c76b5f91f4beaecd88e5e2"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #cl.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:ki.inviteIntoGroup(to, ["u7abc6bc75b34fc0c545fe46c43cff380"]);has = "OK"
                                #except:has = "NOT"
                                #try:ki.kickoutFromGroup(to, ["u7abc6bc75b34fc0c545fe46c43cff380"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #ki.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kk.inviteIntoGroup(to, ["ub4b2144cb807203fe8ab26ee90ea3804"]);has = "OK"
                                #except:has = "NOT"
                                #try:kk.kickoutFromGroup(to, ["ub4b2144cb807203fe8ab26ee90ea3804"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kk.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kc.inviteIntoGroup(to, ["uae95a5f98fec6ca04407a4fba451662f"]);has = "OK"
                                #except:has = "NOT"
                                #ltry:kc.kickoutFromGroup(to, ["uae95a5f98fec6ca04407a4fba451662f"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kc.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kb.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:kb.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kb.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kd.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:kd.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kd.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:ke.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:ke.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #ke.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kf.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:kf.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kf.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kg.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:kg.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kg.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kh.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:kh.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kh.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:kj.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:kj.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #kj.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))
                                #try:sw.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                #except:has = "NOT"
                                #try:sw.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                #except:has1 = "NOT"
                                #if has == "OK":sil = "sehat"
                                #else:sil = "sakit"
                                #if has1 == "OK":sil1 = "sehat"
                                #else:sil1 = "sakit"
                                #sw.sendTextTemplate(msg.to, "kesehatan\nKick : {} \nInvite : {}".format(sil1,sil))

                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"Succes Add Admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate(msg.to,"Succes Add staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"Succes Addbot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"Succes Hpus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate(msg.to,"Succes Clear staff")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"Succes hapus bot")
                                       except:
                                           pass

                        #elif cmd == "harga":
                          #if wait["selfbot"] == True:
                            #if msg._from in admin:
                               #sendTextTemplate(msg.to, "â­ââââââââââ\nââ«â[     DAFTAR HARGA     ]ââ« \nâSELFBOT ONLY = 75K /BLN\nâ2 ASSIST = 100K /BLN\nâ5 ASSIST = 200K /BLN\nâ10 ASSIST = 300K /BLN\nâ\nâPROTECT ANTIJS\nâ\nâ2 BOT + ANTIJS = 150K /BLN\nâ5 BOT + ANTIJS = 300K /BLN\nâ10 BOT + ANTIJS = 500K /BLN\nâ\nââà¦\âANDA BERMINAT\nâ SILAHKAN ADD CONTACT \nâ DIBAWAH INI   \nâ\nâhttp://line.me/ti/p/~reza.p.i.p\nâ       TERIMA KASIH      \nâ\nâ°ââââââââââââ")
                               #sendTextTemplate(msg.to, "Yuck di Order.... ")

                        elif msg.text in ["Cipok","Tagall","Desah","Emuach","Pagi","Siang","Sore","Malam","Nah","All"]:
                               if wait["selfbot"] == True:
                                if msg._from in admin:
                                 group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    sensTextTemplate3(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)  

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"ã Daftar User Bot ã\n\n"+ma+"\nTotalã%sãList Bots" %(str(len(Bots))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    a = a + 1
                                    end = '\n'
                                    mb += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    a = a + 1
                                    end = '\n'
                                    mc += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"ã Daftar Admin ã\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotalã%sãPengguna Selfbot" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd.startswith("youtube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "âââ[ Êá´sá´Êá´ Êá´á´á´á´Êá´ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\nâ ââ£{} ]".format(str(data["title"]))
                                    ret_ += "\nâ â https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\nâââ[ á´á´á´á´Ê {} á´ Éªá´á´á´ ]".format(len(datas))
                                sendTextTemplate(to, str(ret_))
#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == 'desah':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 20:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)

                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"🔴Botlist🔴\n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))

                        elif cmd == "pandawa.stay":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Jmid,Zmid])
                                    sendTextTemplate(msg.to,"Redy stay "+str(ginfo.name)+" Siap Backup")
                                except:
                                    pass

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate3(msg.to,"🔴Adminlist🔴\n\n🔴Owner\n"+ma+"\n🔴Admin\n"+mb+"\n🔴Staff:\n"+mc+"\n%s Adminlist" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                mg = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                g = 0
                                f = 0
                                gid = protect["pqr"]
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["protect"]
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["proall"]
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["pinv"]
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                    mf += str(f) + ". " +cl.getGroup(group).name + "\n"
                                gid = protect["antijs"]
                                for group in gid:
                                    g = g + 1
                                    end = '\n'
                                    mg += str(g) + ". " +cl.getGroup(group).name + "\n"
                                sendTextTemplate3(msg.to,"Settings Protection\n\nProurl :\n"+ma+"\nProall:\n"+mb+"\nProtect:\n"+mf+"\nProtect Cancel:\n"+mc+"\nProinvite:\n"+md+"\nProtectJS:\n"+mg+"\nProtectlist %s Grup protect" %(str(len(protect["pqr"])+len(protect["protect"])+len(protect["antijs"])+len(protect["proall"])+len(protectcancel)+len(protect["pinv"]))))

                        elif cmd == "pandawaname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                kb.sendMessage(msg.to,responsename4)
                                kd.sendMessage(msg.to,responsename5)
                                ke.sendMessage(msg.to,responsename6)
                                kf.sendMessage(msg.to,responsename7)
                                kg.sendMessage(msg.to,responsename8)
                                kh.sendMessage(msg.to,responsename9)
                               #kj.sendMessage(msg.to,responsename10)                                
                               #sw.sendMessage(msg.to,responsename11)                                
                                
                        elif cmd == "masuk":
                         if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               ki.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kk.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kc.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kb.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kd.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               ke.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kf.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kg.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               kh.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               
                        elif cmd == "name":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.sendMessage(msg.to, "ⓅⒶⓃⒹⒶⓌⒶⒷⓄⓉ")
                               kk.sendMessage(msg.to, "ⓅⒶⓃⒹⒶⓌⒶⒷⓄⓉ")
                               kc.sendMessage(msg.to, "ⓅⒶⓃⒹⒶⓌⒶⒷⓄⓉ")
                               kb.sendMessage(msg.to, "ⓅⒶⓃⒹⒶⓌⒶⒷⓄⓉ")
                               kd.sendMessage(msg.to, "ⓅⒶⓃⒹⒶⓌⒶⒷⓄⓉ")
                               #ke.sendMessage(msg.to, "ⓅⒶⓃⒹⒶⓌⒶⒷⓄⓉ")
                               #kf.sendMessage(msg.to, "۞❂✪Dragon- ₭ιll₠₹ ⋮➲➤➤")
                               #kg.sendMessage(msg.to, "۞❂✪Dragon-₭ιll₠₹ ⋮➲➤➤")
                               #kh.sendMessage(msg.to, "۞❂✪Dragon- ₭ιll₠₹ ⋮➲➤➤")

                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost sudah aktif"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost Diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "ãDiaktifkanã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost Dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost Sudah Tidak Aktif"
                                    sendTextTemplate(msg.to, "ãDinonaktifkanã\n" + msgs)
                 
                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                ki.leaveGroup(msg.to)
                                
                        elif cmd == "bye1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kk.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kk.leaveGroup(msg.to)
                                
                        elif cmd == "bye2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kc.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kc.leaveGroup(msg.to)
                                
                        elif cmd == "bye3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kb.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kb.leaveGroup(msg.to)
                                
                        elif cmd == "bye4":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                kd.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kd.leaveGroup(msg.to)
                                
                        elif cmd == "kicker out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.sendMessage(msg.to, "Pulang dulu "+str(G.name))
                                kj.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "kicker in":
                          if msg._from in admin:
                           if msg.toType == 2:
                               group = cl.getGroup(to)
                               group.preventedJoinByTicket = False
                               cl.updateGroup(group)
                               invsend = 0
                               ticket = cl.reissueGroupTicket(to)
                               kj.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                               sw.acceptGroupInvitationByTicket(to,format(str(ticket)))
                               time.sleep(0.01)
                          

                        elif cmd == ".bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate(msg.to, "Makasih sudah invit\nketemu lain waktu... "+str(G.name))
                                cl.leaveGroup(msg.to)
                                
                        elif cmd == "pulang":
                           if wait["selfbot"] == True:
                            if msg._from in admin:
                               ki.leaveGroup(msg.to)
                               kk.leaveGroup(msg.to)
                               kc.leaveGroup(msg.to)
                               kb.leaveGroup(msg.to)
                               kd.leaveGroup(msg.to)
                               ke.leaveGroup(msg.to)
                               kf.leaveGroup(msg.to)
                               kg.leaveGroup(msg.to)
                               kh.leaveGroup(msg.to)                               

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        sendTextTemplate(i, " Silahkan invite Ownernya ")
                                        cl.leaveGroup(i)
                                        sendTextTemplate(to,"Succes leave group " +h)

                        elif cmd == "timerespon":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                sendTextTemplate3(msg.to, "●Time Respon●\n\n ●Get Profile\n   %.10f\n ●Get Contact\n   %.10f\n ●Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               start = time.time()                               
                               sendTextTemplate(msg.to, "Prosess....")                               
                               elapsed_time = time.time() - start
                               sendTextTemplate(msg.to, "Time:\n{}".format(str(elapsed_time)))
                               
                        elif cmd == "lurk:on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['SKreadPoint'][msg.to] = msg_id
                                 Setmain['SKreadMember'][msg.to] = {}
                                 sendTextTemplate(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurk:off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['SKreadPoint'][msg.to]
                                 del Setmain['SKreadMember'][msg.to]
                                 sendTextTemplate(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['SKreadPoint']:
                                if Setmain['SKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['SKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['SKreadPoint'][msg.to]
                                        del Setmain['SKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['SKreadPoint'][msg.to] = msg.id
                                    Setmain['SKreadMember'][msg.to] = {}
                                else:
                                    sendTextTemplate(msg.to, "User kosong...")
                            else:
                                sendTextTemplate(msg.to, "Ketik lurking on dulu")

                        elif cmd == "sider on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  sendTextTemplate(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "sider off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  sendTextTemplate(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  sendTextTemplate(msg.to, "Sudak tidak aktif")

#===========add img============#                                                                                
                        elif cmd.startswith("addimg"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addimage"]["status"] = True
                                    settings["Addimage"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("image.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(msg.to, "Silahkan kirim fotonya...")
                                else:
                                    sendTextTemplate(to, "Foto itu sudah dalam list")
                        elif cmd.startswith("dellimg "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("image.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate(to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate(msg.to, "Foto itu tidak ada dalam list")

                        elif cmd == "listimage":
                                no = 0
                                ret_ = "Daftar Image\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} Images".format(str(len(images)))
                                sendTextTemplate(to, ret_)
#==============add video==========================================================================
                        elif cmd.startswith("addvideo"):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in images:
                                    settings["Addvideo"]["status"] = True
                                    settings["Addvideo"]["name"] = str(name.lower())
                                    images[str(name.lower())] = ""
                                    f = codecs.open("video.json","w","utf-8")
                                    json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(msg.to, "Silahkan kirim video nya...")
                                else:
                                    sendTextTemplate(to, "video itu sudah dalam list")
                        elif cmd.startswith("dellvideo "):
                               sep = text.split(" ")
                               name = text.replace(sep[0] + " ","")
                               name = name.lower()
                               if name in images:
                                   cl.deleteFile(images[str(name.lower())])
                                   del images[str(name.lower())]
                                   f = codecs.open("video.json","w","utf-8")
                                   json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                   sendTextTemplate(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                               else:
                                   sendTextTemplate(to, "video itu tidak ada dalam list")

                        elif cmd == "listvideo":
                                no = 0
                                ret_ = "Daftar video\n\n"
                                for image in images:
                                    no += 1
                                    ret_ += str(no) + ". " + image.title() + "\n"
                                ret_ += "\nTotal {} video".format(str(len(images)))
                                cl.sendMessage(to, ret_)
#=========== [ Add Audio] ============#
                        elif cmd.startswith("addmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in audios:
                                    settings["Addaudio"]["status"] = True
                                    settings["Addaudio"]["name"] = str(name.lower())
                                    audios[str(name.lower())] = ""
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(msg.to, "Silahkan kirim mp3 nya...") 
                                else:
                                    sendTextTemplate(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in audios:
                                    cl.deleteFile(audios[str(name.lower())])
                                    del audios[str(name.lower())]
                                    f = codecs.open("audio.json","w","utf-8")
                                    json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                                no = 0
                                ret_ = "? Daftar Lagu ?\n\n"
                                for audio in audios:
                                    no += 1
                                    ret_ += str(no) + ". " + audio.title() + "\n"
                                ret_ += "\nTotal {} Lagu".format(str(len(audios)))
                                sendTextTemplate(to, ret_)
 #=========== [ Add sticker] ============#                   
                        elif cmd.startswith("addsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name not in stickers:
                                    settings["Addsticker"]["status"] = True
                                    settings["Addsticker"]["name"] = str(name.lower())
                                    stickers[str(name.lower())] = ""
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(msg.to, "Silahkan kirim stickernya...") 
                                else:
                                    sendTextTemplate(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                name = name.lower()
                                if name in stickers:
                                    del stickers[str(name.lower())]
                                    f = codecs.open("sticker.json","w","utf-8")
                                    json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                    sendTextTemplate(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                                else:
                                    sendTextTemplate(msg.to, "Sticker itu tidak ada dalam list") 
                                                   
                        elif cmd == "liststicker":
                                no = 0
                                ret_ = " Daftar Sticker \n\n"
                                for sticker in stickers:
                                    no += 1
                                    ret_ += str(no) + ". " + sticker.title() + "\n"
                                ret_ += "\nTotal {} Stickers".format(str(len(stickers)))
                                sendTextTemplate(to, ret_)
#=========== [ Hiburan] ============#  
                        elif 'like ' in text.lower():
                                try:
                                    typel = [1001,1002,1003,1004,1005,1006]
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = cl.getContact(u).mid
                                    s = cl.getContact(u).displayName
                                    hasil = cl.getHomeProfile(mid=a)
                                    st = hasil['result']['feeds']
                                    for i in range(len(st)):
                                        test = st[i]
                                        result = test['post']['postInfo']['postId']
                                        cl.likePost(str(sender), str(result), likeType=random.choice(typel))
                                        #cl.createComment(str(sender), str(result), ' ──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-11 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~tetsunaki\nline.me/ti/p/~tetsunaki\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────')
                                    sendTextTemplate(msg.to, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                                except Exception as e:
                                    cl.sendMessage(receiver, str(e))
                                                                                 
                        elif text.lower().startswith("!music "):
                            try:
                                search = text.lower().replace("!musik","")
                                r = requests.get("https://rest.farzain.com/api/joox.php?apikey=rambu&id={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                info = data["info"]
                                audio = data["audio"]
                                hasil = "「 Hasil Musik 」\n"
                                hasil += "\nPenyanyi : {}".format(str(info["penyanyi"]))
                                hasil += "\nJudul : {}".format(str(info["judul"]))
                                hasil += "\nAlbum : {}".format(str(info["album"]))
                                hasil += "\n\nLink : \n1. Image : {}".format(str(data["gambar"]))
                                hasil += "\n\nLink : \n2. MP3 : {}".format(str(audio["mp3"]))
                                cl.sendImageWithURL(msg.to, str(data["gambar"]))
                                cl.sendMessage(msg.to, str(hasil))
                                cl.sendAudioWithURL(msg.to, str(audio["mp3"]))
                                cl.sendMessage(msg.to, "Searching mp3 done..")
                            except Exception as error:
                            	cl.sendMessage(msg.to, "「 Result Error 」\n" + str(error))
                        
                        elif cmd.startswith("profilesmule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                sendTextTemplate(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                sendTextTemplate(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass
                                
                        elif cmd.startswith("meme"):
                          if msg._from in admin:    
                            txt = msg.text.split("@")
                            image = ("http://memegen.link/"+txt[1].replace(" ","_")+"/"+txt[2].replace(" ","_")+"/"+txt[3].replace(" ","_")+".jpg?watermark=none")
                            cl.sendImageWithURL(msg.to, image)
                            
                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                html = requests.get('https://www.instagram.com/' + instagram + '/?')
                                soup = BeautifulSoup(html.text, 'html.parser')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                AR = text1[0].replace("s150x150/","")
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://www.instagram.com/" + instagram
                                detail = "========INSTAGRAM INFO ========\n"
                                details = "\n========INSTAGRAM INFO ========"
                                sendTextTemplate3(msg.to, detail + user + user1 + followers + following + post + link + details)
                                cl.sendImageWithURL(msg.to, AR)
                            except Exception as njer:
                                sendTextTemplate(msg.to, str(njer))
                                                                                    
                        elif cmd.startswith("ytmp4: "):
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\nAuthor : ' + str(vid.author)
                                    durasi = '\nDuration : ' + str(vid.duration)
                                    suka = '\nLikes : ' + str(vid.likes)
                                    rating = '\nRating : ' + str(vid.rating)
                                    deskripsi = '\nDeskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                sendTextTemplate3(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                sendTextTemplate(msg.to,str(e))
                                
                        elif cmd.startswith("img food: "):
                          if msg._from in admin:
                                query = msg.text.replace("img food: ","")
                                r = requests.get("https://cryptic-ridge-9197.herokuapp.com/api/imagesearch/" + query + "?offset=1")
                                data=r.text
                                data=json.loads(r.text)
                                if data != []:
                                    for food in data:
                                        cl.sendImageWithURL(msg.to, str(food["url"]))
                        
                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            sendTextTemplate3(msg.to,"Informasi™\n\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak)

                        elif cmd.startswith("clone "):
                           if msg._from in admin:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    cl.cloneContactProfile(contact)
                                    ryan = cl.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 Clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    cl.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    sendTextTemplate(msg.to, "Gagal clone profile")
                            
                        elif text.lower() == 'restore':
                           if msg._from in admin:
                              try:
                                  lineProfile.displayName = str(myProfile["displayName"])
                                  lineProfile.statusMessage = str(myProfile["statusMessage"])
                                  lineProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                  cl.updateProfile(lineProfile)
                                  sendMention(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  sendTextTemplate(msg.to, "Gagal restore profile")

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"Spamtag change to " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                sendTextTemplate(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(wait["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        sendTextTemplate(msg.to,"Jumlah melebihi 1000")
                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                sendTextTemplate(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                call.acquireGroupCallRoute(to)
                                call.inviteIntoGroupCall(to, contactIds=members)
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in owner:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                sendTextTemplate(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    sendTextTemplate(msg.to,"Jumlah melebihi batas")
                                    
                        elif cmd.startswith("spaminvid"):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    dan = text.split("|")
                                    userid = dan[1]
                                    namagrup = dan[2]
                                    jumlah = int(dan[3])
                                    grups = cl.groups
                                    tgb = cl.findContactsByUserid(userid)
                                    cl.findAndAddContactsByUserid(userid)
                                    if jumlah <= 1000:
                                        for var in range(0,jumlah):
                                            try:
                                                cl.createGroup(str(namagrup), [tgb.mid])
                                                for i in grups:
                                                	grup = cl.getGroup(i)
                                                	if grup.name == namagrup:
                                                	    cl.inviteIntoGroup(grup.id, [tgb.mid])
                                                	    cl.leaveGroup(grup.id)
                                                	    sendTextTemplate(to,"@! sukses spam grup!\n\nkorban: @!\njumlah: {}\nnama grup: {}".format(jumlah, str(namagrup)), [sender, tgb.mid])
                                            except Exception as e:
                                                sendTextTemplate(msg.to,str(e))

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  sendTextTemplate(msg.to, "http://line.me/ti/p/~" + msgs)
                                  sendTextTemplate(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    sendTextTemplate3(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protecturl ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = "Protect url has been active"
                                  else:
                                       protect["pqr"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url telah active\n\ndi group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url deactive\n\nIn Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url has been deactive"
                                    sendTextTemplate3(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in protect["protect"]:
                                       msgs = "Protect has been active"
                                  else:
                                       protect["protect"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect Active\n\nIn group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect has been disable"
                                    sendTextTemplate3(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Proall ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Proall ','')
                              if spl == 'on':
                                  if msg.to in protect["proall"]:
                                       msgs = "Proall has been active"
                                  else:
                                       protect["proall"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect all active\n\nIn group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect all deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect all has been disable"
                                    sendTextTemplate3(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel has been active "
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel active\n\nIn group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel deactive\n\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel has been disable"
                                    sendTextTemplate3(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Protectinvite ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Protectinvite ','')
                              if spl == 'on':
                                  if msg.to in protect["pinv"]:
                                       msgs = "Protect invite has been active"
                                  else:
                                       protect["pinv"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect inv active\n\nIn group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated \n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite deactive\nIn group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protectinvite has been disable"
                                    sendTextTemplate3(msg.to, "Nonactive\n\n" + msgs)

                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protect["antijs"]:
                                       msgs = "Protectjs has been active"
                                  else:
                                       protect["antijs"].append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti kicker \n\naktif di group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "active\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti kicker off\n\ndi group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti kicker off "
                                    sendTextTemplate3(msg.to, "nonactive\n" + msgs)

                        elif 'Semuapro ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Semuapro ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["ghost"]:
                                       msgs = ""
                                  else:
                                       protect["ghost"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                       msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect on \n\ndi group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Succes\nIn group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["ghost"]:
                                         protect["ghost"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Succes Nonactive Allpro\n\nIn group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Allpro has been deactive\nDi Group : " +str(ginfo.name)
                                    sendTextTemplate3(msg.to, "Nonactive\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Status : [ ON ]\nDi Group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "ã Status Protect kick ã\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Status : [ OFF ]\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    sendTextTemplate3(msg.to, "ã Status Protect kick ã\n" + msgs)

                        elif 'Allpro ' in msg.text:
                           if msg._from in owner or msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protect["pqr"]:
                                       msgs = ""
                                  else:
                                       protect["pqr"].append(msg.to)
                                  if msg.to in protect["protect"]:
                                      msgs = ""
                                  else:
                                      protect["protect"].append(msg.to)
                                  if msg.to in protect["pinv"]:
                                      msgs = ""
                                  else:
                                      protect["pinv"].append(msg.to)
                                  if msg.to in protect["antijs"]:
                                      msgs = ""
                                  else:
                                      protect["antijs"].append(msg.to)
                                  if msg.to in protect["proall"]:
                                      msgs = ""
                                  else:
                                      protect["proall"].append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect on \n\ndi group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Succes\nIn group : " +str(ginfo.name)
                                  sendTextTemplate3(msg.to, "Activated\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protect["pqr"]:
                                         protect["pqr"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["protect"]:
                                         protect["protect"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["pinv"]:
                                         protect["pinv"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["antijs"]:
                                         protect["antijs"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protect["proall"]:
                                         protect["proall"].remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Succes Nonactive Allpro\n\nIn group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Allpro has been deactive\nDi Group : " +str(ginfo.name)
                                    sendTextTemplate3(msg.to, "Nonactive\n" + msgs)

#===========KICKOUT============#       
                        elif ("Kicker " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                                           
                        elif ("41413125" in msg.text):
                            if msg._from in admin:
                             if msg.toType == 2:
                                 print ("[ 19 ] KICK ALL MEMBER")
                                 _name = msg.text.replace("Bubar","")                                 
                                 gs = ki.getGroup(msg.to)
                                 gs = kk.getGroup(msg.to)
                                 gs = kc.getGroup(msg.to)
                                 gs = km.getGroup(msg.to)
                                 gs = kb.getGroup(msg.to)
                                 sendTextTemplate(msg.to,"「 Papay Sayang 😚😚😚」")
                                 sendTextTemplate(msg.to,"「 Sorry r̸o̸o̸m̸ n̸y̸a̸ k̸a̸m̸i̸ s̸i̸t̸a̸ s̸e̸e̸ y̸o̸u̸」")
                                 targets = []
                                 for g in gs.members:
                                     if _name in g.displayName:
                                         targets.append(g.mid)
                                 if targets == []:
                                     sendTextTemplate(msg.to,"Limit boss")
                                 else:
                                     for target in targets:
                                       if not target in Bots:
                                          if not target in admin:
                                             if not target in staff:
                                               try:
                                                   dhenza= [ki,kk,kc,km,kb]
                                                   kicker=random.choice(dhenza)
                                                   kicker.kickoutFromGroup(msg.to,[target])
                                                   print (msg.to,[g.mid])
                                               except Exception as error:
                                                   sendTextTemplate(msg.to, str(error))

                        elif text.lower() == 'pasukanpandawa':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                           	if msg.toType == 2:
                                  ginfo = cl.getGroup(msg.to)
                                  sendTextTemplate(msg.to, "Proses Cleanse....")
                                  sendTextTemplate(msg.to, "「 silentkiller 」\nmember : " +str(len(ginfo.members)) + " \nFuck you...")
                                  G = cl.getGroup(msg.to)
                                  G.preventedJoinByTicket = False
                                  cl.updateGroup(G)
                                  Ticket = cl.reissueGroupTicket(msg.to)
                                  ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  km.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                  _name = text.lower().replace('silentkiller','')
                                  gs = ki.getGroup(msg.to)
                                  gs = kk.getGroup(msg.to)
                                  gs = kc.getGroup(msg.to)
                                  gs = km.getGroup(msg.to)
                                  gs = kb.getGroup(msg.to)
                                  gs = sw.getGroup(msg.to)
                                  targets = []
                                  for g in gs.members:
                                  	if _name in g.displayName:
                                  	   targets.append(g.mid)
                                  if targets == []:
                                  	sendTextTemplate(msg.to, "Nothing member")
                                  else:
                                       for target in targets:
                                        if not target in Bots:
                                           if not target in admin:
                                              if not target in staff:
                                                 try:
                                                      random.choice(ABC).kickoutFromGroup(msg.to,[target])
                                                      G = cl.getGroup(msg.to)
                                                      G.preventedJoinByTicket = True
                                                      cl.updateGroup(G)
                                                      G.preventedJoinByTicket(G)
                                                      cl.updateGroup(G)
                                                 except:
                                                      pass
                                                      
                        elif text.lower() == 'killban':
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              gid = cl.getGroupIdsJoined()
                              group = cl.getGroup(to)
                              gMembMids = [contact.mid for contact in group.members]
                              ban_list = []
                              for tag in wait["blacklist"]:
                                    ban_list += filter(lambda str: str == tag, gMembMids)
                              if ban_list == []:
                                    sendTextTemplate(to, "Limit bos")
                                    return
                              else:
                                    for i in gid:
                                    	for jj in ban_list:
                                         if jj in admin:
                                                pass
                                         elif jj in staff:
                                                pass
                                         elif jj in Bots:
                                                pass
                                         else:
                                                cl.kickoutFromGroup(i, [jj])
                                                
                        elif "Mainkan " in msg.text:
                           if msg._from in admin:
                              key = eval(msg.contentMetadata["MENTION"])
                              key["MENTIONEES"][0]["M"]                                                                                                                                
                              targets = []
                              for x in key["MENTIONEES"]:
                                  targets.append(x["M"])
                              for target in targets:                                                                                                                                       
                                  try:
                                      ki.kickoutFromGroup(msg.to,[target])
                                      ki.findAndAddContactsByMid(target)
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                      ki.inviteIntoGroup(msg.to,[target])
                                      ki.cancelGroupInvitation(msg.to,[target])
                                  except:
                                      pass
                                      
                        elif "Invite " in msg.text:
                            if msg._from in admin:                                                                                                                                       
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      cl.findAndAddContactsByMid(target)
                                      cl.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 
                                       
                        elif cmd == "gas":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "ASSALAMUALAIKUM \nHALLOOO!!! SORRY ROOM KALIAN \n\nKEBANYAKAN ANU\nSILENT DATANG\nMAU SAPU ROOM GJ\nNO COMEND \nNO BAPER \nNO BACOT \nNO DESAH \nNO SPONSOR \nNO HATTERS\nROOM OKEP \nROOM JUDI\nROOM GAJELAS\SIAP KAMI BANTAII \n\n\n\n FUCK YOU...\nKENAPE LU PADA DIEM\nTANGKIS SU JANGAN CUMA NYIMAK\n\n\nDASAR ROOM PEA KAGAK JELAS\nSORRY BOS!!!\nGC LU MAU GUA SITA...!!!\n\n\n SALAM DARI KAMI S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜\n\nHADIR DI ROOM ANDA\n\nRATA GAK RATA YANG PENTING KIBAR \nRATA KAMI SENANG\nGAKRATA TUNGGU KEDATANGAN KAMI LAGI\n\n\n  <<<SLAM CIAK S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜>>> \n\n\n>>>>>>GO!!! <<<<<<\n\n\nCREATOR\n\n<<<<<<<<<<S̴̬̦̈͛̈́̇̈́̈́͂͒I̴̡͈͓̖͉̟̲͚̮͚̾͌̂̅̈́̍̀͗̕͝L̴̯̝̣̉͜ͅḚ̵̻͆N̷̡̛͎̗̮̤̩̟̮̏̄́̔̄̀T̵̪̭͇̘̳̚ ̸̲̪̱͒́̂̀ͅK̶̨̟̥͊͑̍̆͌̎Ḯ̸̧̺͖͔̹̞̿͗̚Ļ̶̧̨̫̤͈̖͆͆̈̕̚L̵̖̤͈̜̳̉̽͋͛̈́E̸̡̖̠̦͛͜R̵͖̬̯̞̝̪̳̙̙̋͑̒͊̎̕̚͜>>>>>>>>>>\n\nhttp://line.me/ti/p/~pxj5094s\nhttp://line.me/ti/p/~dhenz415")
                               cl.sendContact(to, mid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)
                               cl.sendContact(to, Amid)
                               cl.sendContact(to, Bmid)                          
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)
                               cl.sendMessage(to, None, contentMetadata={"STKID":"406","STKPKGID":"1","STKVER":"100"}, contentType=7)

                        elif cmd == "respon" or cmd == "pasukan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendMessage(msg.to, "Siap!!")
                                ki.sendMessage(msg.to, "Siap!!")
                                kk.sendMessage(msg.to, "Siap!!")
                                kc.sendMessage(msg.to, "Au ah Males gua..")
                                kb.sendMessage(msg.to, "Siap!!")
                                kd.sendMessage(msg.to, "Siap!!")
                                ke.sendMessage(msg.to, "Siap!!")
                                kf.sendMessage(msg.to, "Siap!!")
                                kg.sendMessage(msg.to, "Siap!!")
                                kh.sendMessage(msg.to, "Siap!!")
                                cl.sendMessage(msg.to, "Seluruh Anak Pandawa Sudah Siap!!\nSiap Untuk mrngamankan Grup!")

                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ki.sendMessage(msg.to, "Salken all "+str(G.name))
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.sendMessage(msg.to, "Salken all "+str(G.name))
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.sendMessage(msg.to, "Salken all "+str(G.name))
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.sendMessage(msg.to, "Salken all "+str(G.name))
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.sendMessage(msg.to, "Salken all "+str(G.name))
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.sendMessage(msg.to, "Salken all "+str(G.name))
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.sendMessage(msg.to, "Salken all "+str(G.name))
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.sendMessage(msg.to, "Salken all "+str(G.name))
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.sendMessage(msg.to, "Salken all "+str(G.name))
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendMessage(msg.to, "Good bye "+str(G.name))
                                ki.leaveGroup(msg.to)
                                #kk.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kk.leaveGroup(msg.to)
                                #kc.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kc.leaveGroup(msg.to)
                                #kb.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kb.leaveGroup(msg.to)
                                #kd.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kd.leaveGroup(msg.to)
                                #ke.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                ke.leaveGroup(msg.to)
                                #kf.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kf.leaveGroup(msg.to)
                                #kg.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kg.leaveGroup(msg.to)
                                #kh.sendTextTemplate(msg.to, "Good bye "+str(G.name))
                                kh.leaveGroup(msg.to)
                                
                        elif cmd == "minggat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sendTextTemplate4(msg.to, "Asalamu.alaikum..wr..wb..! Bye bye "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           sendTextTemplate(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        #elif cmd == "harga":
                          #if wait["selfbot"] == True:
                            #if msg._from in admin:
                               #sendTextTemplate(msg.to, "â­ââââââââââ\nââ«â[     DAFTAR HARGA     ]ââ« \nâSELFBOT ONLY = 75K /BLN\nâ2 ASSIST = 100K /BLN\nâ5 ASSIST = 200K /BLN\nâ10 ASSIST = 300K /BLN\nâ\nâPROTECT ANTIJS\nâ\nâ2 BOT + ANTIJS = 150K /BLN\nâ5 BOT + ANTIJS = 300K /BLN\nâ10 BOT + ANTIJS = 500K /BLN\nâ\nââà¦\âANDA BERMINAT\nâ SILAHKAN ADD CONTACT \nâ DIBAWAH INI   \nâ\nâhttp://line.me/ti/p/~reza.p.i.p\nâ       TERIMA KASIH      \nâ\nâ°ââââââââââââ")
                               #sendTextTemplate(msg.to, "Yuck di Order.... ")
#===========ADMIN ADD============
                        elif ("Staff:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           sendTextTemplate(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Bot:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           sendTextTemplate(msg.to,"Succes Addbot")
                                       except:
                                           pass

                        elif (".Adminexpl:on " in msg.text):
                            if msg._from in owner or msg_from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           sendTextTemplate(msg.to,"Succes expel admin")
                                       except:
                                           pass

                        elif (".Staffexpl:on " in msg.text):
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           sendTextTemplate(msg.to,"Succes expel staff")
                                       except:
                                           pass

                        elif (".Botexpl:on " in msg.text):
                            if msg._from in owner:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           sendTextTemplate(msg.to,"Succes expel Bots")
                                       except:
                                           pass
  #====================================#                                         
                        elif cmd == "autojoin on":
                            if msg._from in owner:
                                settings["autoJoin"] = True
                                sendTextTemplate(to, "Berhasil mengaktifkan auto join")
                        elif cmd == "autojoin off":
                            if msg._from in owner:	
                                settings["autoJoin"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan auto join")
                        elif cmd == "autoblock on":
                           if msg._from in owner:
                                settings["autoBlock"] = True
                                sendTextTemplate(to, "Berhasil mengaktifkan auto Block")
                        elif cmd == "autoblock off":    
                            if msg._from in owner: 	
                                settings["autoBlock"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan auto Block")                        
                        elif cmd == "checkpost on":
                           if msg._from in owner:
                                 settings["checkPost"] = True
                                 sendTextTemplate(to, "Berhasil mengaktifkan check details post")
                        elif cmd == "checkpost off":
                           if msg._from in owner:
                                settings["checkPost"] = False
                                sendTextTemplate(to, "Berhasil menonaktifkan check details post")                        
                        elif cmd == "unsend on":
                       	 if msg._from in owner:
                                 settings["unsendMessage"] = True
                                 sendTextTemplate(to, "Berhasil mengaktifkan unsend message")
                        elif cmd == "unsend off":
                            if msg._from in owner:
                                 settings["unsendMessage"] = False
                                 sendTextTemplate(to, "Berhasil menonaktifkan unsend message")
#==================================#
                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in owner:
                                wait["addadmin"] = True
                                sendTextTemplate(msg.to,"Send Contact")

                        elif cmd == "adminexpl:on" or text.lower() == 'adminexpl:on':
                            if msg._from in owner:
                                wait["delladmin"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addstaff"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "staffexpl:on" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin:
                                wait["dellstaff"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin:
                                wait["addbots"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "botexpl:on" or text.lower() == 'botexpl:on':
                            if msg._from in owner:
                                wait["dellbots"] = True
                                sendTextTemplate(msg.to,"Kirim kontaknya...")

                        elif cmd == "fresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                sendTextTemplate(msg.to,"Clean..")
                                sendTextTemplate(msg.to,"Refresh done 💯")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                     
                        elif cmd == "spaminvite on" or text.lower == 'spaminvite on':
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                sendTextTemplate(msg.to, "Send Contact to spam grup..")
                                
                        elif cmd == "spaminvite off" or text.lower() == 'spaminvite off':
                            if msg._from in admin:
                                settings["Spaminvite"] = False
                                sendTextTemplate(msg.to, "Send Contact to send grup Off..")
                                
#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Mentionkick"] = True
                                sendTextTemplate(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["MentionKick"] = False
                                sendTextTemplate(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = True
                                sendTextTemplate(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["contact"] = False
                                sendTextTemplate(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = True
                                sendTextTemplate(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["detectMention"] = False
                                sendTextTemplate(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = True
                                sendTextTemplate(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoJoin"] = False
                                sendTextTemplate(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                                wait["autoLeave"] = True
                                sendTextTemplate(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["autoLeave"] = False
                                sendTextTemplate(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = True
                                sendTextTemplate(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["autoAdd"] = False
                                sendTextTemplate(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = True
                                sendTextTemplate(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["sticker"] = False
                                sendTextTemplate(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = True
                                sendTextTemplate(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                settings["autoJoinTicket"] = False
                                sendTextTemplate(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif cmd == "ban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    sendTextTemplate(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                         if target not in wait["selfbot"] or target not in Bots:
                                            try:
                                                wait["blacklist"][target] = True
                                                sendTextTemplate(msg.to,"Anda ternoda")
                                            except:
                                                pass
                                                
                        elif cmd == "unban all":
                            if msg.toType == 2:
                                gs = cl.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    sendTextTemplate(msg.to,"gak ada orang")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                sendTextTemplate(msg.to,"Anda ternoda")
                                            except:
                                                pass
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           sendTextTemplate(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           sendTextTemplate(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkwblacklist"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                wait["Talkdblacklist"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["blacklist"][target] = True
                                           sendTextTemplate(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           sendTextTemplate(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["wblacklist"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                wait["dblacklist"] = True
                                sendTextTemplate(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              if wait["blacklist"] == {}:
                                sendTextTemplate(msg.to,"Nothing blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["Talkblacklist"] == {}:
                                sendTextTemplate(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                sendTextTemplate(msg.to," Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'bl':
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                              if wait["blacklist"] == {}:
                                    sendTextTemplate(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "%i" % len(ragets)
                              sendTextTemplate(msg.to,"Succes clearall " +mc)
                        elif text.lower() == 'dz':
                               sendTextTemplate(msg.to, "cie pake sc nya dhenza ya")
#===========COMMAND SET============#
                        elif 'Spesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  sendTextTemplate(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  sendTextTemplate(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  sendTextTemplate(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  sendTextTemplate(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  sendTextTemplate(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  sendTextTemplate(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cpesan":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in admin:
                               sendTextTemplate(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                               
                        elif cmd == "batre":
                            if msg._from in admin or msg._from in owner:
                               try:cl.inviteIntoGroup(to, ["u45882d0ead170385787c60d40e37bec7"]);has = "OK"
                               except:has = "NOT"
                               try:cl.kickoutFromGroup(to, ["u45882d0ead1789855dbc60d40e37bec7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               cl.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                               try:ki.inviteIntoGroup(to, ["u2bf37dc8bb9ac858985395a9e15850f9"]);has = "OK"
                               except:has = "NOT"
                               try:ki.kickoutFromGroup(to, ["u2bf37dc8bb9ac809015395a9e15850f9"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               ki.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kk.inviteIntoGroup(to, ["u0a5ee8d796e3677a59894ff03b6564ec"]);has = "OK"
                               except:has = "NOT"
                               try:kk.kickoutFromGroup(to, ["u0a5ee8d796e36779i9b84ff03b6564ec"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kk.sendMessage(to, "Status:\n\n🔴Kick : {} \n??Invite : {}".format(sil1,sil))
                               try:kc.inviteIntoGroup(to, ["u29b16f0e99cfdf0e7d289170f7cdc1a7"]);has = "OK"
                               except:has = "NOT"
                               try:kc.kickoutFromGroup(to, ["u29b16f0e99cfdf787d7b8170f7cdc1a7"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒. Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low  0%"
                               kc.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                               
                               try:kc.inviteIntoGroup(to, ["udfad8056476f3e76383575513cc8aebe"]);has = "OK"
                               except:has = "NOT"
                               try:km.kickoutFromGroup(to, ["udfad8056476f3346903575513cc8aebe"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               km.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))                              
                               try:kb.inviteIntoGroup(to, ["uea5fe04e39713e6464cf5687bc5ac7aa"]);has = "OK"
                               except:has = "NOT"
                               try:kb.kickoutFromGroup(to, ["uea5fe04e39713e4548cf5687bc5ac7aa"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "🔋██ full 100%"
                               else:sil = "🔌█▒ Low 0%"
                               if has1 == "OK":sil1 = "🔋██ full 100%"
                               else:sil1 = "🔌█▒ Low 0%"
                               kb.sendMessage(to, "Status:\n\n🔴Kick : {} \n🔴Invite : {}".format(sil1,sil))
                                                                                    
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kb.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = kd.findGroupByTicket(ticket_id)
                                     kd.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kd.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group6 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ke.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group7 = kf.findGroupByTicket(ticket_id)
                                     kf.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kf.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group8 = kg.findGroupByTicket(ticket_id)
                                     kg.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kg.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     group9 = kh.findGroupByTicket(ticket_id)
                                     kh.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kh.sendTextTemplate(msg.to, "Masuk : %s" % str(group.name))
                                     
    except Exception as error:
        print (error)


while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                bot(op)
                # Don't remove this line, if you wan't get error soon!
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
