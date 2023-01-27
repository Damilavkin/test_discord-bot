token = 'MTA2MjM0NTUxNDcwNTc2MDI4OA.GHGz7F.9QOvEyk8-QbslBBVn1AukGk98C8DfFTDpm55MM'

prefix = "/"

YDL_OPTIONS = {
    'format': 'worstaudio/best',
               'noplaylist': 'True', 'simulate': 'True', 'preferredquality': '192', 'preferredcodec': 'mp3', 'key': 'FFmpegExtractAudio'
               }

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'
                  }