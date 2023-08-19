import pandas
import yt_dlp
import os

# downloaded_audio_folder = os.getcwd() + "/downloaded_audio"
downloaded_audio_folder = "downloaded_audio"

ydl_opts = {
	'format': 'bestaudio/best',
	'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192',
	}],
}


def download_audio_from_youtube_id():
    df = pandas.read_csv('data/salami_youtube_pairings.csv')
    all_pairings_df = pandas.read_csv('data/all_pairings.csv')
    for index, row in df.iterrows():
        print(row['salami_id'])
        ydl_opts['outtmpl'] = downloaded_audio_folder + "/" + str(row['salami_id']) + ".%(ext)s"
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                x = ydl.download(['http://www.youtube.com/watch?v='+row['youtube_id']])
                all_pairings_df.loc[row['salami_id']] = row
                all_pairings_df.to_csv('all_pairings.csv', index=False)
        except (KeyboardInterrupt):
            raise
        except:
            print("Error downloading youtube id: " + row['youtube_id'])
            continue

download_audio_from_youtube_id()