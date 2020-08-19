import pyfiglet
import termcolor
import wikipedia
import gtts
import playsound
import os
import datetime
import newsapi

icon_text = pyfiglet.figlet_format('WikiTalk')
welcome_screen = termcolor.colored(icon_text, color='blue')
print(welcome_screen)


def raw_audio(greating_text):
    try:

        audio = gtts.gTTS(text=greating_text, lang='en', slow=False)
        audio.save('greatings.mp3')
        playsound.playsound('greatings.mp3')
        os.remove('greatings.mp3')
    except BaseException:
        return False


def greatings(text):
    x = raw_audio(text)
    while True:
        if x != False:
            break
        else:
            x = raw_audio(text)
    return x


current = datetime.datetime.now()


# check if it is the first time of the user


try:
    with open('welcome.txt', 'r') as f:
        name = f.readlines()
except BaseException:
    with open('welcome.txt', 'w') as f2:
        welcome_text = "Hi there.welcome to WikiTalk.I am Wiki,your personal voice assistant.It seems we've met for the first time.That's amazing!!Ummm!!What should I call you?"
        greatings(welcome_text)
        name = input('Your name:')
        f2.write(name)
        thanks_text = f'Humm...{name}..sounds cool.So,{name},let me officially greet you.'
        greatings(thanks_text)
with open('welcome.txt', 'r') as f2:
    name = f2.readlines()


if int(current.hour) <= 12:
    text = f'Hi {name}.Good morning.How can I help you?I can tell you todays breaking news.Or if you want,I can search for any information on web..'
    greatings(text)

elif int(current.hour) <= 15:
    text = f'Hi {name}.Good noon.How can I help you?I can tell you todays breaking news.Or if you want,I can search for any information on web..'
    greatings(text)

elif int(current.hour) <= 17:
    text = f'Hi {name}.Good afternoon.How can I help you?I can tell you todays breaking news.Or if you want,I can search for any information on web..'
    greatings(text)
else:
    text = f'Hi {name}.Good evening.How can I help you?I can tell you todays breaking news.Or if you want,I can search for any information on web..'
    greatings(text)

while True:

    def wikisearch():
        try:
            ask_for_search_type = input('News/Information: ')

            if ask_for_search_type[0].lower(
            ) == 'n' or 'news' in ask_for_search_type.lower():
                welcome_to_newsworld = "Okay.Please let me know what kinds of news you are looking for."
                greatings(welcome_to_newsworld)

                my_api_key = '38df851456f641ea9df315b23bc19ffa'
                news_client = newsapi.NewsApiClient(api_key=my_api_key)
                user_input = input('News topic: ')

                news = news_client.get_everything(
                    q=user_input, language='en', page_size=100)['articles']

                news_ammount = len(news)
                news_find_time = "Give me few seconds.I am searching through more than 30 world's famous newspapers about your news topic"
                greatings(news_find_time)

                if news_ammount == 0:
                    text = f"Umm!It seems there is no news today about your topic.Make sure you enter a right topic.And just enter the topic name and nothing else."
                    greatings(text)
                elif news_ammount <= 5:
                    greatings('Yep.I am done.Here it is')
                    j = 1
                    for x in news:
                        title = x['title']
                        description = x['description']
                        final_news = title + description
                        n_count = f'News:{j}'
                        greatings(n_count)
                        greatings(final_news)
                        j += 1
                else:
                    user_demand = f"Yeo.I am done.i have found {news_ammount} news about your topic.How many news you want to listen?"
                    greatings(user_demand)
                    news_number = input('Amount of news: ')
                    i = 0
                    j = 1
                    for x in news:
                        if i < int(news_number):

                            title = x['title']
                            description = x['description']
                            final_news = title + description
                            n_count = f"News{j}"
                            greatings(n_count)
                            greatings(final_news)
                            i += 1
                            j += 1
            else:
                greatings('Okay.What kind of information you are looking for?')

                search = input('Search:')
                search_result = wikipedia.search(search)
                greatings(
                    'Give me few seconds.I am colllecting information on your topic.')
                search_summary = wikipedia.summary(search_result)
                x = f"Yep.I am done.Here it is.{search_summary}"
                greatings(x)

        except BaseException:
            return False
    while True:
        s_res = wikisearch()
        if s_res != False:
            break

        else:
            text = "Umm!...I'm sorry.I couldn't get you.Can you please try again??"
            greatings(text)

    greatings('Do you wanna search something else?')
    search_again = input('Yes/No:')
    if search_again[0].lower() == 'n':
        greatings('Thanks for using me.See you later.')
        break
    else:
        greatings('Sure.What I will search now?')
