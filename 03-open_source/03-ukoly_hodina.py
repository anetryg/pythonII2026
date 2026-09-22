# Data k úkolům 2 az 7 jsou stejná jako v kapitole 01-arcpy, tedy liniová vrstva silnic
# a polygonová vrstva chráněných území. Rastrová data k úkolům 8 a 9 dostanete zvlášť.

# Úkol 1
"""
Rozcvička na Shapely, zatím bez dat ze souboru.

Vytvořte polygon o rozměrech 100 krát 50 jednotek a linii, která jím prochází.
Zjistěte plochu polygonu, délku linie a souřadnice těžiště polygonu. Ověřte pomocí
prostorového vztahu, že linie polygon skutečně protíná. Nakonec vytvořte kolem linie
obalovou zónu o šířce 10 jednotek a zjistěte její plochu.
"""


# Úkol 2
"""
Načtěte pomocí GeoPandas obě vrstvy ze složky data. U každé zjistěte a vypište
počet prvků, názvy sloupců a souřadnicový systém. Podívejte se na prvních pět řádků.
"""


# Úkol 3
"""
Souřadnicové systémy v praxi.

Zjistěte, v jakém souřadnicovém systému data jsou, a spočítejte celkovou délku silnic
v kilometrech. Potom vrstvu převeďte do systému WGS84, který má kód 4326 a pracuje
ve stupních, a délku spočítejte znovu.

Porovnejte obě čísla a jednou větou vysvětlete, co znamená to druhé a proč se nedá použít.
Všimněte si, že vás GeoPandas u druhého výpočtu na něco upozorní.
"""


# Úkol 4
"""
Zopakujte úlohu z kapitoly o ArcPy, tentokrát v GeoPandas.

Do vrstvy silnic přidejte sloupec "kategorie". Pokud má linie vyplněný sloupec "JMENO"
a je delší než 1000 metrů, vložte hodnotu "01", jinak vložte "00". Pozor na to, že
délka musí být v metrech, takže pracujte s daty v jejich původním systému, ne v tom
převedeném z úkolu 3.

Spočítejte, kolik linií spadlo do které kategorie.
"""


# Úkol 5
"""
Zjistěte pomocí prostorového spojení, které silnice zasahují do chráněných území.
Vypište jejich počet a názvy prvních deseti.

Rozmyslete si, jaký prostorový vztah je pro tuhle otázku správný, a svou volbu zdůvodněte
v komentáři.
"""


# Úkol 6
"""
Předchozí úkol vám řekl, které silnice se s územími potkávají, ale ne jak dlouhý úsek
uvnitř leží. Použijte překryv, spočítejte délku úseků uvnitř chráněných území a zjistěte,
které území je silnicemi zatížené nejvíc.
"""


# Úkol 7
"""
Ověření napříč nástroji.

Vezměte výsledek úkolu 4 a porovnejte ho s tím, co vám na stejné úloze vyšlo v kapitole
o ArcPy. Napište test, který obě čísla porovná a projde jen tehdy, když se shodují.

Pokud se rozejdou, najděte příčinu. Podezřelá místa jsou souřadnicový systém, zacházení
s prázdnými hodnotami ve sloupci JMENO a hranice podmínky, tedy zda "delší než 1000"
znamená včetně tisícovky nebo bez ní.
"""


# Úkol 8
"""
Otevřete rastr pomocí rasterio a vypište jeho souřadnicový systém, rozměry v pixelech,
počet pásem a rozsah. Načtěte první pásmo jako pole a zjistěte minimum, maximum a průměr.
"""


# Úkol 9
"""
Ořežte rastr podle hranice jednoho chráněného území a výsledek uložte do nového souboru.

Nezapomeňte, že vektorová vrstva a rastr musí být ve stejném souřadnicovém systému.
Po uložení soubor znovu otevřete a ověřte, že má očekávaný rozsah a souřadnicový systém.
"""
