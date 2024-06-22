import emoji
import pandas as pd
from collections import Counter
from wordcloud import WordCloud
from urlextract import URLExtract

def fetch_stats(user, df):
    extracter = URLExtract()
    if user != 'Overall':
        df = df[df['users'] == user]

    # 1. fetch number of messages 
    num_messages = df.shape[0]   

    # 2. number of words
    words = []
    for message in df['message']:
        words.extend(message.split()) 

    # 3. Fetch Total number of Media messages
    number_media_msg = df[df['message'] == '<Media omitted>'].shape[0]

    # # 4. Fetch total number of Links messages
    count = 0
    for msg in df['message']:
        if 'https' in msg:
            count += 1

    return num_messages, words, number_media_msg, count


def fetch_most_busy_user(df):
    x = df['users'].value_counts().head()
    df = round((df['users'].value_counts()/df.shape[0])*100, 2).reset_index().rename(columns={'users': 'Name', 'count': 'Percent(%)'})
    return x, df
    
def create_wordcloud(selected_user, df):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    temp = df[df['users'] != 'System_notification']
    temp = temp[temp['message'] != r'<Media omitted>']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_word(selected_user, df):

    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    temp = df[df['users'] != 'System_notification']
    temp = temp[temp['message'] != r'<Media omitted>']


    words = []
    for message in temp['message']:
        for word in message.split():
            if word.lower() not in stop_words and not emoji.is_emoji(word.lower()):
                words.append(word.lower())

    most_common_word_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_word_df


def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    emojis=[]
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])
    
    emoji_df = pd.DataFrame(Counter(emojis).most_common(20), columns=['Emoji', 'Count'])
    return emoji_df


def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    
    timeline['time'] = time
    return timeline


def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    daily_timeline = df.groupby('date_timeline').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['users'] == selected_user]
    
    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap

