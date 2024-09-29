
import pandas as pd
#look at https://github.com/mlomb/chat-analytics?tab=readme-ov-file
#        https://github.com/Tyrrrz/DiscordChatExporter?tab=readme-ov-file


def get_col_info(dataframe):
    for idx, col in enumerate(dataframe.columns):
        flag = ""
        if idx in (4, 7, 11):
            flag = "*"
        print(f"Column {idx}{flag}: {col}")

def main():
    
    # df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # dataframe = pd.read_csv('../personal_messages_etc/5messages_testing.csv')
    dataframe = pd.read_csv('../personal_messages_etc/1305messages.csv')

    # Filter for sent and received messages
    dataframe['Message Date'] = pd.to_datetime(dataframe['Message Date'])

    sent_messages = dataframe[dataframe['Type'] == 'Outgoing']  # Messages you sent
    received_messages = dataframe[dataframe['Type'] == 'Incoming']  # Messages you received
    
    #find most recent message
    most_recent_message = dataframe['Message Date'].max()
    least_recent_message = dataframe['Message Date'].min()
    days_between_first_and_last_message = (most_recent_message - least_recent_message).days
    messages_per_day = len(dataframe)/days_between_first_and_last_message
    
    
    #find who you text the most
    chat_session_counts = dataframe['Chat Session'].value_counts()
    top_20_chat_sessions = chat_session_counts.head(200)  # Get the top 20 chat sessions
    
    
    for idx, (chat_session, count) in enumerate(top_20_chat_sessions.items(), start=1):
        print(f"{idx}. {chat_session} {count}")
    
    # Find the person you have received the most messages from
    most_received_from = received_messages['Sender Name'].value_counts().idxmax()
    most_received_count = received_messages['Sender Name'].value_counts().max()

    
        
    print("=========================================")
    print(f"oldest message: {least_recent_message}, most recent message: {most_recent_message}")
    print(f"days between first and last message: {days_between_first_and_last_message}")
    print(f"that averages to {messages_per_day} messages per day")
    print(f"In total, you've sent {len(sent_messages)} messages and received {len(received_messages)} messages. That's {len(sent_messages) + len(received_messages)} messages!")
    
    print(f"Most received from: {most_received_from} with {most_received_count} messages")
    
    # person you text the most (outside of gcs)
    # how many messages you've sent to them/received from them
    
    # person you've texted for the most days in a row
    # how many days in a row you've texted them
    
    # person you've texted the most in a single day
    # how many messages you've sent to them
    
    # person you've texted the most in a single month
    # how many messages you've sent to them
    
    # person you've texted the most in a single year
    # how many messages you've sent to them
    
    # person you've texted the most in a single hour
    # how many messages you've sent to them
    
    # person you've texted the most in a single minute
    # how many messages you've sent to them
    
    # highest imbalance of sent vs received messages where you have over 100 messages with that person
    
    # time stats

if __name__ == '__main__':
    main()