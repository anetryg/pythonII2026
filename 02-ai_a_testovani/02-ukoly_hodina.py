# Úkol 1
"""
Napište specifikaci funkce dms_na_stupne(stupne, minuty, vteriny), která převede
souřadnici ze stupňů, minut a vteřin na desetinné stupně. Zatím nepište žádný kód,
jen specifikaci jako komentář nebo docstring.

Specifikace musí odpovědět alespoň na tyto otázky:
 - jaké typy mají vstupy a co znamenají,
 - jakého typu je výstup a v jakých jednotkách,
 - jak se zachází se zápornou hodnotou, tedy s jižní a západní polokoulí,
 - co se stane při neplatném vstupu, například když minuty vyjdou mimo rozsah 0 az 59.
"""


# Úkol 2
"""
Podle své specifikace z úkolu 1 napište testy. Kód funkce stále neexistuje.
Vytvořte soubor test_prevody.py a napište do něj nejméně čtyři testy:
 - typickou hodnotu na severní polokouli, například 49 stupňů 12 minut 30 vteřin,
 - hodnotu na jižní polokouli, například -33 stupňů 52 minut 10 vteřin,
 - nulové souřadnice,
 - případ, u kterého podle své specifikace čekáte chybu.

Desetinná čísla porovnávejte s tolerancí, ne na přesnou rovnost.
"""


# Úkol 3
"""
Teprve teď požádejte AI, aby funkci dms_na_stupne napsala. Do promptu vložte svou
specifikaci z úkolu 1. Implementaci uložte do souboru prevody.py a spusťte pytest.

Zapište si, kolik testů prošlo napoprvé a co selhalo. Pokud něco neprošlo, popište AI,
který test selhal a jakou hodnotu vrátil, a nechte kód opravit. Nezačínejte znovu od nuly.
"""


# Úkol 4
"""
Následující funkci vygenerovala AI jako odpověď na dotaz "spočítej vzdálenost dvou GPS
bodů". Vypadá věrohodně a spustí se bez chyby.

Nejdřív napište test, který ověří vzdálenost Brna a Prahy. Skutečná vzdálenost je
přibližně 185 km, tolerance 5 km je rozumná. Teprve pak funkci opravte tak, aby test prošel.
Přidejte ještě test, který ověří, že vzdálenost bodu od sebe samého je nula.
"""

import math


def vzdalenost(lat1, lon1, lat2, lon2):
    R = 6371
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    return 2 * R * math.asin(math.sqrt(a))


# Úkol 5
"""
Požádejte AI, aby napsala funkci plati_souradnice(lat, lon), která vrátí True, pokud
jsou zeměpisné souřadnice platné, a False, pokud nejsou. Nejdřív si ale rozmyslete
a zapište hraniční případy, které budete testovat. Zamyslete se nad tím, jaké hodnoty
zeměpisná šířka a délka vůbec mohou nabývat a co se má stát přesně na hranici rozsahu.

Vygenerovanou funkci proženete svými testy a zapište, na kterém hraničním případu
případně selhala.
"""


# Úkol 6
"""
Vezměte libovolný kus kódu, který vám AI vygenerovala v předchozích úkolech, a projděte
ho podle kontrolního seznamu z této kapitoly:
 - dělá to, co jsem zadala,
 - ošetřuje hraniční případy,
 - nepoužívá zastaralé API,
 - nevymyslelo si funkci nebo knihovnu, která neexistuje,
 - umím vysvětlit každý řádek.

Ke každému bodu napište jednu větu. Pokud u posledního bodu narazíte na řádek, který
vysvětlit neumíte, nechte si ho vysvětlit a teprve pak pokračujte.
"""
