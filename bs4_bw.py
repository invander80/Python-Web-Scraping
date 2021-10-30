# Web-Scraping, Anzeige mit pyplot, Bundeswahlleiter

from bs4 import BeautifulSoup       # pip install bs4 / pip install beautifulsoup4
import requests                     # pip install requests
import ast                          # ast um strings in ein dict um zu wandeln (standart lib)
import matplotlib.pyplot as plt
# für den Parser: pip install html.parser // ansonsten -> lxml (version abhängig, aber schneller)

source_code = requests.get("https://www.bundeswahlleiter.de/bundestagswahlen/2021/ergebnisse/bund-99.html").text

data = BeautifulSoup(source_code, "html.parser")


# // Zweitstimmen // ------------------------------------------------------------------------------------------------ //

matches_zweitstimmen = data.find("div", class_="chart chart-perfect-fourth u-hidden u-visible-for-svg js-d3chart")["data-chartdata"]
matches_zweitstimmen = ast.literal_eval(matches_zweitstimmen)

parteien = []
prozente = []
colors = []

for x in range(len(matches_zweitstimmen["data"])):
    parteien.append(matches_zweitstimmen["data"][x]["label"])
    prozente.append(matches_zweitstimmen["data"][x]["value"])
    colors.append(matches_zweitstimmen["data"][x]["color"])

print(parteien)
print(prozente)
print(colors)

# // Sitzplätze // -------------------------------------------------------------------------------------------------- //
matches_sitze = data.find("div", class_="chart chart-golden-section u-hidden u-visible-for-svg js-d3chart")["data-chartdata"]
matches_sitze = ast.literal_eval(matches_sitze)

parteien_sitze = []
prozente_sitze = []
colors_sitze = []

for x in range(len(matches_sitze["data"])):
    parteien_sitze.append(matches_sitze["data"][x]["label"])
    prozente_sitze.append(matches_sitze["data"][x]["value"])
    colors_sitze.append(matches_zweitstimmen["data"][x]["color"])

print(parteien_sitze)
print(prozente_sitze)


# // Pyplots - Zweitstimmen // -------------------------------------------------------------------------------------- //
# Bar-Chart
pos = [i for i, _ in enumerate(parteien)]
plt.bar(pos, prozente, color=colors)
plt.xlabel("Parteien")
plt.ylabel("Prozente")

plt.xticks(pos, parteien)
plt.show()

# # // Pyplots - Sitze // ------------------------------------------------------------------------------------------- //
# Pie-Chart
"""fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(1,1,1)
ax.pie(prozente_sitze, labels=parteien_sitze, colors=colors_sitze)
ax.add_artist(plt.Circle((0,0), 0.1, color="white"))
plt.show()
"""
