from googleapiclient.discovery import build
import streamlit as st

api_key = 'AIzaSyBvVHqveFW4FLUuk4lh2kn8NMAF7t0QsY4'

def get_channel_stats(channel_id):
    
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    request = youtube.channels().list(
                part='snippet,contentDetails,statistics',
                id=channel_id)
    
    response = request.execute()
    
    data = dict(Channel_name = response['items'][0]['snippet']['title'],
    Total_Subscribers = response['items'][0]['statistics']['subscriberCount'],
    Total_Views = response['items'][0]['statistics']['viewCount'],
    Total_Videos = response['items'][0]['statistics']['videoCount'],
    Joinning_Date = response['items'][0]['snippet']['publishedAt'].split('T')[0],
    Joinning_Time = response['items'][0]['snippet']['publishedAt'].split('T')[1].replace('Z',''))
    
    return data

st.title('YouTube Channel Information App')
st.header('Enter YouTube Channel ID')

channel_id = st.text_input('Channel ID:', '')

if st.button('Get Channel Info'):
    if channel_id:
        channel_info = get_channel_stats(channel_id)
        if channel_info:
            st.subheader('Channel Details')
            st.write(f"**Channel Name:** {channel_info['Channel_name']}")
            st.write(f"**Total Subscribers:** {channel_info['Total_Subscribers']}")
            st.write(f"**Total Videos:** {channel_info['Total_Videos']}")
            st.write(f"**Total Views:** {channel_info['Total_Views']}")
            st.write(f"**Channel Joinning Date :** {channel_info['Joinning_Date']}")
            st.write(f"**Channel Joinning Time :** {channel_info['Joinning_Time']}")
        else:
            st.error('No data found for the provided Channel ID. Please check the ID and try again.')
    else:
        st.warning('Please enter a Channel ID 👆!')
