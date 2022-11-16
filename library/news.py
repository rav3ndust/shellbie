# this is used as a lib to import to mainMenu
import urllib.request as web
import os as sh 
# this is our list of minimal news sources. we can add/remove as needed. 
news_src_list = ["1 - 68k.news", "2 - eink.links"]
# - - - functions - - - 
def sleep(seconds):
    # halts sys ops X seconds
    # usage example: sleep(2)
    sh.system(seconds)
def getNews():
    # getNews() pipes the news in as html which we need to strip out
    # getsNews_links2 might be the better option for now
    print("So, you want to read the news?")
    print("Which of these sources would you prefer?")
    for news in news_src_list:
        print(news)
    ans = "Type the number corresponding to your choice."
    news_src_list[0], news_src_list[1] = 1, 2
    news_src_list[0], news_src_list[1] = str(news_src_list[0]), str(news_src_list[1])
    yn = input(ans)
    if (yn == news_src_list[0]):
        try: 
            with web.urlopen('http://68k.news') as news:
                print(news.read().decode('utf-8'))
        except urllib.error.URLError as err:
            print(err.reason)
    elif (yn == news_src_list[1]):
        try:
            with web.urlopen('https://eink.link') as news:
                print(news.read().decode('utf-8'))
        except urllib.error.URLError as err:
            print(err.reason) 
    else:
        print("Invalid option pressed. Returning.")
        exit()
# getNews_links2 uses a minimal web browser to open the news sites for you to browse.
def getNews_links2():
    print("So, you want to read the news?") 
    print("Which of these sources would you prefer?") 
    for news in news_src_list:
        print(news)
    ch2 = "Type the number corresponding to your choice." 
    news_src_list[0], news_src_list[1] = 1, 2
    news_src_list[0], news_src_list[1] = str(news_src_list[0]), str(news_src_list[1])
    digit = input(ch2) 
    if (digit == news_src_list[0]):
        def browser_display_1():
            opening = "Opening up 68k.news..."
            opening_links = 'links2 -g http://68k.news'  
            print(opening) 
            sleep(2)
            sh.system(opening_links) 
        browser_display_1()
    elif (digit == news_src_list[1]):
        def browser_display_2():
            opening2 = "Opening up eink.link..." 
            opening_links2 = 'links2 -g https://eink.link'  
            print(opening2) 
            sleep(2)
            sh.system(opening_links2)
        browser_display_2()
    else:
        print("Invalid key selected. Exiting.") 
        exit()
# this code ensures the module doesn't run at import time.
if __name__ == '__main__':
    getNews()
    getNews_links2()
