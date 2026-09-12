import sys, json
version = sys.argv[1]
with open("pylock.json") as x:
    d = json.load(x)
d["interpreter"] = "https://cdn.jsdelivr.net/pyodide/%s/full/pyodide.mjs" % version
with open("pylock.json", "w") as v:
    json.dump(d, v)
