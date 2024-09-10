import tiktoken


encoding = tiktoken.get_encoding("cl100k_base")

enc = encoding.encode(" Conveyor")
print(enc)
