buffer = b"hi\nthere\nsup"
line, buffer = buffer.split(b"\n", 2)
print(line)
print(buffer)