src = r"C:\users\tairk\downloads\staff-broken.csv"
dst = r"C:\users\tairk\downloads\result.csv"

with open(src, "r", encoding="kz1048", newline="") as f:
    text = f.read()

with open(dst, "w", encoding="utf-8-sig", newline="") as f:
    f.write(text)
