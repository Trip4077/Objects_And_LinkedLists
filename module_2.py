a = {"x": 2, "y": 3}

print(a)
print(a["x"], a["y"])

point = {"x_coord": 5, "y_coord": 10}

print(point["x_coord"], point["y_coord"])

print("x" in a)
print("y_coord" in point)
print("z_coord" in point)

point["z_coord"] = 15

print("z_coord" in point)
print(point)
