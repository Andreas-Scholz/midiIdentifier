import difflib

def compare (input, archive):
    matches = dict()
    count = 1
    for key, value in archive.items():
        if count%100 == 0:
            print(count)
        ratio = difflib.SequenceMatcher(None, input, value).ratio()
        matches[key] = "%.2f" % round(ratio*100,2)
        count += 1
    return matches