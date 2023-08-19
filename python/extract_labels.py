import os
import pandas as pd
import numpy as np

from utils import assign_label_group

annotations_path = 'data/salami-data-public/annotations/'
salami_metadata = pd.read_csv('data/salami-data-public/metadata/metadata.csv')

def clear_df(df_loc='data/labels.csv', both=False):
    if both:
        pd.DataFrame(columns=['song_id', 'timestamp', 'label']).to_csv('data/labels.csv', index=False)
        pd.DataFrame(columns=['song_id', 'timestamp', 'label']).to_csv('data/downloaded_audio_labels.csv', index=False)
    else:
        pd.DataFrame(columns=['song_id', 'timestamp', 'label']).to_csv(df_loc, index=False)

def get_segment_times(audio_file, annotation_folder=annotations_path, df_loc='data/labels.csv'):
    print(audio_file)
    df = pd.read_csv(df_loc)
    file_name = os.path.splitext(os.path.basename(audio_file))[0]
    # for some tracks, only one annotation is available, take first one as default
    # if there is no annotation available, store -1 as error code

    try:
        label_file = os.path.join(annotation_folder, file_name, 'parsed', 'textfile1_functions.txt')
        t = pd.read_table(label_file, header=None)
        print('annotation 1')
    except IOError:
        try:
            label_file = os.path.join(annotation_folder, file_name, 'parsed', 'textfile2_functions.txt')
            t = pd.read_table(label_file, header=None)
            print('annotation 2')
        except IOError:
            print('no annotation available')
            return -1

    segment_times = t.iloc[:, 0].values
    segment_labels = t.iloc[:, 1].values
    # print(t)
    for i, r in t.iterrows():
        new_row = {'song_id': file_name, 'timestamp': r[0], 'label': r[1]}
        df = df.append(new_row, ignore_index=True)
        # print(r)
    print(df)
    df.to_csv(df_loc, index=False)
    # print(segment_labels)
    return segment_times

# clear_df(both=True)
# song_ids = salami_metadata['SONG_ID'].values.tolist()
# for song_id in song_ids:
#     get_segment_times(f'{song_id}.mp3', annotations_path)

def map_labels(df_loc='data/labels.csv'):
    df = pd.read_csv(df_loc)
    df['mapped_label'] = df['label'].apply(assign_label_group)
    df.to_csv(df_loc, index=False)

# directory = os.fsencode('downloaded_audio')
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     print(filename)
#     if filename.endswith(".mp3"):
#         get_segment_times(filename, annotations_path, 'data/downloaded_audio_labels.csv')

# df = pd.read_csv('data/labels.csv')
# print(df.groupby('label').size().sort_values(ascending=False))

# directory = os.fsencode('internet_archives_audio')
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     print(filename)
#     if filename.endswith(".mp3"):
#         get_segment_times(filename, annotations_path, 'data/internet_archives_audio_labels.csv')

# map_labels('data/internet_archives_audio_labels.csv')

# def get_duration(audio_file, df_loc='data/start_and_end.csv'):
#     df = pd.read_csv(df_loc)
#     file_name = int(os.path.splitext(os.path.basename(audio_file))[0])
#     print(f"Processing file: {file_name}")

#     matching_rows = df[df['song_id'] == file_name]
#     print(f"Number of matching rows: {len(matching_rows)}")

#     try:
#         song_duration = salami_metadata.loc[salami_metadata['SONG_ID'] == file_name, 'SONG_DURATION'].values[0]
#         print(f"Song duration: {song_duration}")

#         df.loc[df['song_id'] == file_name, 'song_duration'] = song_duration
#         updated_rows = df[df['song_id'] == file_name]
#         print(updated_rows)
#         # print(df)
#         df['song_duration'] = np.where(df['song_id'] == file_name, song_duration, df['song_duration'])
#         df.to_csv(df_loc, index=False)
#     except Exception as e:
#         print(f"Error processing file {filename}: {e}")

# directory = os.fsencode('downloaded_audio')
# for file in os.listdir(directory):
#     filename = os.fsdecode(file)
#     # print(filename)
#     if filename.endswith(".mp3"):
#         get_duration(filename)
