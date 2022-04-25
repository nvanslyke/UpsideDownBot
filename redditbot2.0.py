import praw
import time

reddit = praw.Reddit(
    client_id="Md6VuGCYaoL-V4xxzKVVfA",
    client_secret="3OUZHM0wGI_glIbiiQckPVs5Pg9A4A",
    user_agent="<console:Flipper:1.0>",
    username = "Upside_Down-Bot",
    password = "******"
)



letterdict = {"?":"¿","!":"¡",",":"\'",
"\'":",",".":"˙","A":"∀","B":"𐐒","C":"Ↄ",
"D":"◖","E":"Ǝ","F":"Ⅎ","G":"⅁","H":"H",
"I":"I","J":"ſ","K":"ʞ","L":"⅂","M":"W",
"N":"ᴎ","O":"O","P":"Ԁ","Q":"Ό","R":"ᴚ",
"S":"S","T":"⊥","U":"∩","V":"ᴧ","W":"M",
"X":"X","Y":"⅄","Z":"Z","a":"ɐ","b":"q",
"c":"ɔ","d":"p","e":"ǝ","f":"ɟ","g":"ƃ",
"h":"ɥ","i":"ı","j":"ɾ","k":"ʞ","l":"l",
"m":"ɯ","n":"u","o":"o","p":"d","q":"b", 
"r":"ɹ","s":"s","t":"ʇ","u":"n","v":"ʌ",
"w":"ʍ","x":"x","y":"ʎ","z":"z","\"":"„",
"-":"-","′":",","″":"„","“":"„","’":",",
"”":"„"}

def flipit(words):           
    flipped = ""

    for i in range(len(words)):
        if words[i] in letterdict.keys():
            flipped = letterdict[words[i]] + flipped
        elif words[i] == " ":
            flipped = " " + flipped
        else:
            print("char - " + words[i])
            return ""
    flipped = "„" + flipped + "„"
    return flipped

subreddit = reddit.subreddit("all")
for comment in subreddit.stream.comments(skip_existing=True): 
    if hasattr(comment,"body"):
        lowercaseComment = comment.body.lower()
        if "flip " in lowercaseComment:
            if len(lowercaseComment) < 120:
                print(comment.body)
                if len(flipit(comment.body)) < 1:
                    print("unknown character")
                else:
                    print("******************************************")
                    try:
                        comment.reply(flipit(comment.body))
                        print("Replied - " + flipit(comment.body)) 
                    except:
                        print("Exception")
                  

    


 
