# YouTubeDownloader-Video

PyTube now version 12.1.2 have problem with atribute "span"

how fix this use next instruction

```
go to
C:.../appdata/local/programs/python*/python*/Lib/pytube/chiper.py

in this file search row 411

transform_plan_raw = find_object_from_startpoint(raw_code, match.span()[1] - 1)

and do

transform_plan_raw = js
```
And PyTube be working
