# Lab 5 — Encoding forensics

Pair:   Tair                  Driver first half: Tair
Machine: Personal Machine
Date: 14/11/2026

## What I did

After downloading the original "staff-broken.csv" and extracting the hexdump from it, i deduced by the lack of two-byte letters that it was neither a UTF-8 encoded file nor a UTF-16 encoded one. I then wrote a Python script to read and convert the 'kz1048' encoded file into a readable UTF-8 encoded one.

```
src = r"C:\users\tairk\downloads\staff-broken.csv"
dst = r"C:\users\tairk\downloads\result.csv"

with open(src, "r", encoding="kz1048", newline="") as f:
    text = f.read()

with open(dst, "w", encoding="utf-8-sig", newline="") as f:
    f.write(text)

```

## Result

In the [evidence/](evidence/) folder

## What did not work the first time

I tried to decode using my console to decode the text file but after having a lot of trouble doing that i discovered the the open function in python bears the "encoding" parameter that, in my opinion was the cleanest and most efficient way to go around the problem i was having

## Evidence

- [evidence/](evidence/) — one line per file on what it proves
