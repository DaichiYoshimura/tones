# Tones
!NOTICE! This repository is demonstration.

## Features
- Based on music theory.
- Treat music note as The following classes, Tonality,Time, and Note.
- You handle the relationship of Note,Tonality and Time easily.

## Usage
For example.

```python
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
``` 

### Tonality
At first, You set 'tonal' value by selecting 'Major' or 'minor'.

Second, You set 'key' value by selecting below.
If the 'tonal' value you selected is 'Major',Select in 'Major key list',
Or 'minor',select in 'minor key list'.
(+ means sharp,- means flat)
- Major list : C,D-,D,E-,E,F,G-,G,A-,A,B-,B,C+,F+,C-
- minor list : C,C+,D,D+,E,F,F+,G,G+,A,A+,B,E-,A-,B-

### Time
Third, 'beats' and 'beat_type' value is allowed to set a natural number.

### Note
Next, You set 'pitch','octave' and 'duration' by following the rules.

- pitch : string value that means pitch symbol. (ex: 'C','D-','F+')
- octave : natural value (the lowest value is 1)
- duration : string value in the following list.

  'whole': 1,
  'half': 1/2,
  'quarter': 1/4,
  'eighth': 1/8,
  'sixteenth': 1/16,
  'thirty-second': 1/32,
  'dotted-half': 3/8,
  'dotted-quarter': 3/16,
  'dotted-eight': 3/32,
  'dotted-sixteenth': 3/64,
  'dotted-thirty-second': 3/128

