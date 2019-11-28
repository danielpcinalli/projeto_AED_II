
def bencode(x):
    if type(x) is int:
        return f"i{str(x)}e"
    if type(x) is str:
        return f"{len(x)}:{x}"
    if type(x) is list:
        bencoding = "l"
        for item in x:
            bencoding = f"{bencoding}{bencode(item)}"
        return f"{bencoding}e"
    if type(x) is dict:
        bencoding = "d"
        for key, value in x.items():
            bencoding = f"{bencoding}{bencode(key)}{bencode(value)}"
        return f"{bencoding}e"
        
        
