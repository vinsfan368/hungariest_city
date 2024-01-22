import wikipedia
import random


def get_hungariest():
    wikipedia.set_lang("en")
    page = wikipedia.page("List of cities and towns of Hungary")
    content = page.content
    str0 = "== Largest cities in Hungary in 1910 =="
    str1 = "== See also =="
    idx0 = content.index(str0)
    idx1 = content.index(str1)
    lines = [l for l in content[idx0:idx1].split("\n") if len(l) > 0]
    return random.choice(lines)
