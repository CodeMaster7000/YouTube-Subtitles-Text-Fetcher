def get_subtitle_text(subtitleUrl):
    # Access API
    url = "https://youtube-media-downloader.p.rapidapi.com/v1/subtitles"
    headers = {
        'x-rapidapi-host': "youtube-media-downloader.p.rapidapi.com",
        'x-rapidapi-key': "<<PASTE API KEY>>" # Enter your API key here
    }
    querystring = {"subtitleUrl": subtitleUrl}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
