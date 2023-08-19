import librosa
import pandas as pd

def extract_mfcc():
    y, sr = librosa.load('downloaded_audio/3.mp3')
    # print(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=20, hop_length=512, n_fft=2048)
    df = pd.DataFrame(mfcc)
    df.to_csv('hi2.csv', index=False)
    print(mfcc.shape)
    # print(mfcc)

extract_mfcc()