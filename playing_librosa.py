import librosa
import matplotlib.pyplot as plt
import librosa.display

"""
y, sr = librosa.load('test_chords/Grand Piano - Fazioli - major A# middle.wav')
chm = librosa.feature.chroma_cqt(y, sr)
print(chm)

plt.figure()
librosa.display.specshow(chm, y_axis='chroma', x_axis='time')
plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()
plt.show()
"""

y, sr = librosa.load('Hotel California - The Eagles [FLAC Lossless].flac')
# chm = librosa.feature.chroma_cqt(y, sr)
# print(chm)

tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
beats_timed = librosa.frames_to_time(beats, sr=sr)
print(tempo)
print(beats_timed)

"""
plt.figure()
librosa.display.specshow(chm, y_axis='chroma', x_axis='time')
plt.title('chroma_cqt')
plt.colorbar()
plt.tight_layout()
plt.show()
"""
