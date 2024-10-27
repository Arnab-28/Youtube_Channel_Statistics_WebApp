# YouTube Analyzer: Data-Driven Insights

## Objective

The Channel Checker: YouTube Analytics at Your Fingertips project is designed to provide users with easy access to YouTube channel statistics. Users can simply enter the name of any YouTube channel, and the app will retrieve essential metrics such as:
1. Channel Name
2. Total Subscribers
3. Total Videos
4. Total Views
5. Age

This app leverages the YouTube Data API to fetch real-time data and is built using the Streamlit framework, making it easy for users to interact with and receive instant insights into the performance of their favorite YouTube channels.

## Tech Stack

### Frontend:

Streamlit (for building the user interface)

### Backend: 

YouTube Data API (for retrieving real-time data from YouTube channels)

### API Integration: 

googleapiclient for YouTube API integration and requests for handling HTTP requests

### Python Libraries:
streamlit: To create the user interface.
googleapiclient.discovery: For accessing YouTube API to fetch data.
requests: To send search queries to the YouTube API.

## Project Features

YouTube Channel Search: Users can input the name of a YouTube channel, and the app will search and fetch the corresponding data.
- Real-Time Data Retrieval: The app pulls data directly from the YouTube API, ensuring that users receive the most up-to-date statistics.
- Clean and Simple UI: The Streamlit-based interface makes it easy for users to access data without technical knowledge.
- Error Handling: If a channel is not found, the app will provide relevant error messages guiding the user to input a valid channel name.

