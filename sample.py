import tones as t

tonality = t.Tonality('C', 'Major')
print(tonality.display())
time = t.Time(4, 4)
print(time.display())
note = t.Note('C', 1, 'quarter', tonality, time)
print(note.display())
print(note.pitch + ' degree is ' + str(note.degree()))
tonality.transpose_key(+0.5)
print(note.pitch + ' degree is ' + str(note.degree()))
