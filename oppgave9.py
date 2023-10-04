
def vokaler(ord):
    vokal = 0
    for i in ord:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "y" or i == "æ" or i == "ø" or i == "å":
            vokal += 1
    print(vokal)

vokaler("hei")