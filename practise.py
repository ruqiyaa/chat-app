# buffer = b"hi\nthere\nsup"
# line, buffer = buffer.split(b"\n", 2)
# print(line)
# print(buffer)

line = "/msg Ben "
parts = line.split(" ", 2)
#print(parts)
if len(parts) < 3:
    print("use: /msg name text")
else:
    print("to:", parts[1])
    print("text:", parts[2])
# print("/msg ben".split(" ", 2))
# print("heiinn".split(" ", 2))