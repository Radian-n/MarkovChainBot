import pandas as pd

df = pd.read_csv("goodnewseveryone-v1.0/gne-release-v1.0.tsv", sep="\t", encoding="utf-8")
headlines = list(df["headline"])


def clean(hdln):
    hdln = hdln.replace("'", "")
    hdln = hdln.replace('"', "")
    hdln = hdln.replace("…", "")
    hdln = hdln.replace("”", "")
    hdln = hdln.replace("`", "")
    hdln = hdln.replace("’", "")
    hdln = hdln.replace("“", "")
    hdln = hdln.replace("(", "")
    hdln = hdln.replace(")", "")
    hdln = hdln.replace("#", "")
    return hdln


headlines = [e.strip() for e in headlines]
headlines = [e.split("|")[0] for e in headlines]
headlines = [clean(e) for e in headlines]
headlines = "\n".join(headlines)


with open("headlines.txt", 'a',encoding='utf-8') as outfile:
    outfile.write(headlines)


    