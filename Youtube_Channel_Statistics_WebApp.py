from googleapiclient.discovery import build
import streamlit as st
import requests

api_key = 'AIzaSyAXSesf1gnp1yVRCB5rW0ioTceLT2EB1SE'

def get_channel_id(api_key, channel_name):
    base_url = "https://www.googleapis.com/youtube/v3/search"
    
    # Parameters for the request
    params = {
        'part': 'snippet',
        'q': channel_name,
        'type': 'channel',
        'key': api_key
    }
    
    # Making the API request
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # If channels are found
        if 'items' in data and len(data['items']) > 0:
            # Getting the first channel ID from the search results
            channel_id = data['items'][0]['snippet']['channelId']
            return channel_id
        else:
            st.error('Server is Busy Now! Please try later.')
            return None
    else:
        st.error('Server is Busy Now! Please try later.')
        return None

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
    Joinning_Date = response['items'][0]['snippet']['publishedAt'].split('T')[0])
    
    return data

st.title('Channel Checker: YouTube Analytics at Your Fingertips')
st.header('Enter YouTube Channel Name/ID')

channel_name = st.text_input('Channel Name/ID:', '')

if st.button('Get Channel Info'):
    if channel_name:
        channel_id = get_channel_id(api_key,channel_name)
        channel_info = get_channel_stats(channel_id)
        if channel_info:
            st.subheader('Channel Details')
            st.write(f"**Channel Name:** {channel_info['Channel_name']}")
            st.write(f"**Total Subscribers:** {channel_info['Total_Subscribers']}")
            st.write(f"**Total Videos:** {channel_info['Total_Videos']}")
            st.write(f"**Total Views:** {channel_info['Total_Views']}")
            st.write(f"**Channel Joinning Date :** {channel_info['Joinning_Date']}")
            
        else:
            st.error('No data found for the provided Channel Name. Please check the Name and try again.')
    else:
        st.warning('Please enter a Channel Name 👆')
