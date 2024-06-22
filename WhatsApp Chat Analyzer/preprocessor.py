import re
import pandas as pd

# It will Preprcess the data
def preprocess(data):
    # Message Extracting
    pattern = r'\s-\s'
    results = [re.split(pattern, line)[1] if re.split(pattern, line)[1:] else line for line in data.split('\n')]

    # Date and time Extracting

    if 'AM' in data or 'PM' in data or 'am' in data or 'pm' in data:
        date_pattern = r'^(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s[apAP][mM]\s-)\s'
        dates = [re.findall(date_pattern, line)[0] if re.findall(date_pattern, line) else '' for line in data.split('\n')]
        if dates[0] == '':
            date_pattern = r'^(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-)\s'
            dates = [re.findall(date_pattern, line)[0] if re.findall(date_pattern, line) else '' for line in data.split('\n')]

    for i in range(len(dates)):
        dates[i] = dates[i].replace(' -', '')
        dates[i] = dates[i].replace(' -', '')

    df = pd.DataFrame({'user_message': results, 'message_date': dates})
    
    # Mixed is used to convert the string date format intp the date-time format
    df['message_date'] = pd.to_datetime(df['message_date'], format='mixed')
    df.rename(columns={'message_date': 'date'}, inplace=True)

    # Separate users and messages

    users = []
    messages = []
    for message in df['user_message']:
        entry = message.split(': ')
        if entry[1:]:
            users.append(entry[0])
            messages.append(entry[1])
        else:
            users.append('System_notification')
            messages.append(entry[0])

    df['users'] = users
    df['message'] = messages
    df.drop(columns='user_message', axis='columns', inplace=True)
    df.head()

    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['date_timeline'] = df['date'].dt.date

    period = []
    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))

    df['period'] = period

    df_new = df.dropna()

    return df_new