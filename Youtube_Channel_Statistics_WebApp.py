from googleapiclient.discovery import build
import streamlit as st
import requests
import os

# Use the YouTube API key
api_key = st.secrets["api_key"]

# Function to get channel ID by channel name, if ID is unknown
@st.cache_data(show_spinner=False)
def get_channel_id(api_key, channel_name):
    """Fetch the YouTube channel ID for the given channel name."""
    try:
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
                return data['items'][0]['snippet']['channelId']
            else:
                return None
        elif response.status_code == 429:
                st.error("Server is Busy Now! Please try again later!")
                return None
        else:
            return None
    except Exception:
        return None
# Function to fetch and cache YouTube channel stats for a given channel ID
@st.cache_data(show_spinner=False)
def get_channel_stats(api_key,channel_id):
    """Fetch channel statistics given a channel ID."""
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.channels().list(
                    part='snippet,statistics',
                    id=channel_id)
        response = request.execute()
        
        if 'items' in response and response['items']:
            channel = response['items'][0]
            return {
                'Channel_name' : channel['snippet']['title'],
                'Total_Subscribers' : channel['statistics'].get('subscriberCount', 'N/A'),
                'Total_Views' : channel['statistics'].get('viewCount', 'N/A'),
                'Total_Videos' : channel['statistics'].get('viewCount', 'N/A'),
                'Joinning_Date' : channel['snippet']['publishedAt'].split('T')[0]
            }
        else:
            return None
    except Exception as e:
        st.error("Failed to fetch channel statistics! Please try again later!")
        return None
        
st.title('YouTube Analyzer: Data-Driven Insights')
st.header('Enter YouTube Channel Name/ID')

channel_name_or_id = st.text_input('Channel Name/ID:', '')

if st.button('Get Channel Info'):
    if channel_name_or_id:
        channel_id = (channel_name_or_id if len(channel_name_or_id) == 24 else get_channel_id(api_key, channel_name_or_id))
        if channel_id:
            channel_info = get_channel_stats(api_key, channel_id)
            if channel_info:
                st.subheader('Channel Details')
                st.write(f"**Channel Name:** {channel_info['Channel_name']}")
                st.write(f"**Total Subscribers:** {channel_info['Total_Subscribers']}")
                st.write(f"**Total Videos:** {channel_info['Total_Videos']}")
                st.write(f"**Total Views:** {channel_info['Total_Views']}")
                st.write(f"**Channel Joinning Date :** {channel_info['Joinning_Date']}")
            else:
                st.error('Failed to retrieve channel statistics. Server is Busy Now! Please try again later.')
        else:
            st.error('Channel not found or Server is Busy Now! Please try again later.')
    else:
        st.warning('Please enter a Channel Name/ID 👆')
