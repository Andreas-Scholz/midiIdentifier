import difflib

def compare (input, archive):
    matches = dict()
    for key, value in archive.items():
        ratio = difflib.SequenceMatcher(None, input, value).ratio()
        matches[key] = "%.2f" % round(ratio*100,2)
    return matches