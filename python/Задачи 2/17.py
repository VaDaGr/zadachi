def length(a, b):
    x1 = a["x"]
    y1 = a["y"]
    x2 = b["x"]
    y2 = b["y"]
    ab = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return round(ab, 3)

print(length({"x": 12, "y": 3}, {"x": 45, "y": 6}))