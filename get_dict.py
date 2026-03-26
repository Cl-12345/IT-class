def get() -> dict:
    dicts = dict()
    with open('dict.txt', 'r', encoding='utf-8') as f:
        s = f.readlines()
        for i in s:
            dicts[i.split()[0].lower()] = i.split()[1:]
    return dicts