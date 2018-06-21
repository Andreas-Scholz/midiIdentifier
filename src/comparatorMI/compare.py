import difflib
import operator
import json

def getArchive():
    with open('../../files/songs.json') as json_data:
        archive = json.load(json_data)
    smallArchive = {}
    for song in archive:
        smallArchive[song['name']] = song['short_midi']
    return smallArchive


def compare(inp, archive):
    matches = dict()
    count = 1
    for key, value in archive.items():
        if count % 100 == 0:
            print(count)
        print(inp + " - " + value + " - ")
        ratio = difflib.SequenceMatcher(None, inp, value).ratio()
        matches[key] = "%.2f" % round(ratio * 100, 2)
        count += 1
    return matches


def levenshtein(inp, archive):
    ''' From Wikipedia article; Iterative with two matrix rows. '''
    matches = dict()
    for key, value in archive.items():
        if inp == value:
            return 0
        elif len(inp) == 0:
            return len(value)
        elif len(value) == 0:
            return len(inp)
        v0 = [None] * (len(value) + 1)
        v1 = [None] * (len(value) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(inp)):
            v1[0] = i + 1
            for j in range(len(value)):
                cost = 0 if inp[i] == value[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]

        matches[key] = v1[len(value)]
    return matches


def main():
    self_played = {}
    self_played["Alle meine Entchen (falsch): "] = "n60n62n64n65n67n67n65n69n69n69"
    self_played["Alle meine Entchen (richtig): "] = "n60n62n64n65n67n67n69n69n69n6"
    self_played["Alle meine Entchen (länger): "] = "n60n62n64n65n67n67n69n69n69n69n67n69n69n69n69n67n65"
    self_played["Für Elise (last note Wrong): "] = "n64n63n64n63n64n59n62n60n57n48"
    self_played["Für Elise (too high): "] = "n71n70n71n70n71n65n69n67n64n60"
    self_played["Für Elise (too low): "] = "n57n56n57n56n57n52n55n53n50n48"

    library = {}
    library[
        "alle_meine_entchen--heilpaedagogik-info-de.mp3.mid: "] = "n60n79n88n91n94n96n98n102n38n38n44n74n81n90n93n61n62n45n95n40"
    library["Alle_Meine_Entchen.mid: "] = "n48n50n52n53n55n55n57n57n57n57n55n57n57n57n57n55n53n53n53n53"
    library["for_elise_by_beethoven.mid: "] = "n76n75n76n75n76n71n74n72n69n45n52n57n60n64n69n71n40n52n56n64"
    library["for_elise_by_beethoven_shortened.mid: "] = "n76n75n76n75n76n71n74n72"
    library["StarWarsMainTheme.mid: "] = "n82n94n106n82n70n82n70n58n46n34n62n70n74n82n77n58n58n34n46n46"

    for song in self_played.keys():
        # matches = compare(self_played[song], library)
        matches = levenshtein(self_played[song], library)
        sorted_matches = sorted(matches.items(), key=operator.itemgetter(1), reverse=True)[:20]
        print(song)
        print(sorted_matches)


if __name__ == "__main__":
    main()
