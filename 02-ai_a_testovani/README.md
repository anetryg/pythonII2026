## Programování s AI

Značnou část kódu, se kterým budete v praxi pracovat, nenapíšete vy. Napíše ho AI a vaše role bude jiná: zadat úlohu, výsledek přečíst, ověřit a opravit. Odpovědnost za to, co program spočítá, ale nikam nezmizí a zůstává na vás.

Tahle kapitola je o tom, jak s AI pracovat tak, abyste byli vy ten, kdo rozhoduje, a ona ten, kdo píše.

### Čtyři způsoby, jak AI generuje kód

Nejde jen o to, který nástroj používáte. Podstatné je, kolik kódu vznikne najednou a kolik z něj stihnete zkontrolovat.

| Způsob | Jak to vypadá | Co zbývá na vás |
|---|---|---|
| Našeptávač v editoru | Dopisuje řádek nebo pár řádků, jak píšete | Přečtete každý návrh, než ho přijmete |
| Chat | Popíšete úlohu, dostanete blok kódu | Přečtete celý blok, spustíte, otestujete |
| Agent | Sám edituje soubory a spouští příkazy | Kontrolujete výsledek, ne jednotlivé řádky |
| AI jako recenzent | Dáte jí svůj kód a ptáte se na chyby | Posoudíte, jestli má pravdu |

Z tabulky plyne hlavní myšlenka celé kapitoly. **Čím víc práce AI udělá najednou, tím míň stíháte číst řádky a tím víc musí odvést zadání a testy.** U našeptávače si vystačíte s pozorností. U agenta, který vám přepíše deset souborů, už ne.

### Kde AI selhává

* **Vymyslí si funkci nebo knihovnu.** Název zní věrohodně, dokumentace k němu neexistuje.
* **Použije zastaralé API.** Kód pochází z verze knihovny, která už se takhle nechová.
* **Udělá logickou chybu a napíše k ní sebevědomý komentář.** Tohle je nejnebezpečnější, protože komentář vypadá jako důkaz, že autor věděl, co dělá.
* **Vyřeší jinou úlohu.** Zadání si vyloží po svém a vy dostanete funkční kód na něco jiného.
* **Souhlasí s vámi.** Když se zeptáte "tady mají být metry, že?", nejspíš přikývne. Když se zeptáte opačně, přikývne taky.

#### Příklad, který v geoinformatice potkáte

Požádáte AI: *"spočítej rozlohu těch polygonů"*. Dostanete kód, který se spustí a vrátí čísla. Jenže ze zadání nebylo poznat:

* v jakém souřadnicovém systému se má počítat,
* jestli chcete metry čtvereční, hektary nebo kilometry čtvereční,
* co se má stát s vícedílnou geometrií,
* co s prázdnou nebo neplatnou geometrií.

AI si to za vás dosadila. Možná dobře, možná ne. Číslo, které vám vrátila, vypadá v obou případech stejně věrohodně.

### Prompt je specifikace

Většina špatných odpovědí nevzniká proto, že by AI byla hloupá, ale proto, že zadání připouštělo víc výkladů. Porovnejte:

> Napiš funkci, která spočítá vzdálenost dvou bodů.

> Napiš funkci `vzdalenost(lat1, lon1, lat2, lon2)`, která vrátí vzdálenost dvou bodů na Zemi v kilometrech jako float. Vstupem jsou zeměpisné souřadnice v desetinných stupních, kladné na severní a východní polokouli, záporné na jižní a západní. Použij haversinovu formuli a poloměr Země 6371 km. Pro dva shodné body vrať 0.0.

Druhé zadání má jednu správnou odpověď. První jich má desítky.

### Jak napsat dobré zadání

Než začnete psát prompt, projděte si tenhle seznam:

1. **Vstupy.** Co funkce dostane, jakého typu a v jakých jednotkách.
2. **Výstup.** Co vrátí, jakého typu a v jakých jednotkách.
3. **Jednotky a souřadnicový systém.** V geoinformatice nejčastější zdroj tichých chyb.
4. **Hraniční případy.** Nula, záporné číslo, prázdný vstup, jižní polokoule, přelom roku.
5. **Chybějící a neplatné hodnoty.** Co se má stát, když data nejsou v pořádku.
6. **Chování při chybě.** Vrátit `None`, vyhodit výjimku, nebo přeskočit?

### Dejte AI kontext

AI nevidí vaši obrazovku ani vaše data. Užitečné je jí dát:

* **celou chybovou hlášku**, ne jen poslední řádek,
* **ukázku dat**, klidně tři řádky tabulky nebo výpis názvů sloupců,
* **kód kolem**, aby věděla, na co navazuje,
* **verzi knihovny**, se kterou pracujete.

### Co dělat s vygenerovaným kódem

Vždy stejné čtyři kroky, v tomhle pořadí:

1. **Přečtěte ho celý.** Ne jen první řádky a ne jen do chvíle, kdy to vypadá povědomě.
2. **Spusťte ho.**
3. **Vyzkoušejte hranice.** Nula, záporná hodnota, prázdný vstup, jižní polokoule.
4. **Ověřte si, že umíte vysvětlit každý řádek.** Co nedokážete vysvětlit, to neodevzdávejte.

### Iterace

Když kód nefunguje, nezačínejte znovu od nuly. Popište, **co jste čekali**, **co se stalo** a **co už jste zkusili**. Tím z AI uděláte ladicího partnera místo generátoru náhodných pokusů.


## Testování

Předchozí část skončila u toho, že vygenerovaný kód musíte ověřit. Dělat to pokaždé ručně nejde. Od toho jsou testy.

### Proč testy dávají s AI ještě větší smysl

Test napsaný **předem** je zároveň specifikace. Nutí vás rozmyslet si, co má kód dělat, dřív než o něj požádáte. A když vám AI vrátí padesát řádků, nemusíte je číst všechny, aby vás napadlo, kde je chyba. Stačí spustit testy.

### assert

Nejjednodušší test je jedna řádka. Když podmínka platí, nestane se nic. Když neplatí, program spadne.

```python
assert dms_na_stupne(49, 12, 30) == 49.208333
```

U desetinných čísel na přesnou rovnost nespoléhejte, porovnávejte s tolerancí:

```python
assert abs(dms_na_stupne(49, 12, 30) - 49.208333) < 0.000001
```

### pytest

Na víc testů se hodí knihovna pytest. Nainstalujete ji příkazem

```
pip install pytest
```

Testy dáte do souboru, jehož název začíná na `test_`, a každý test je funkce, jejíž název taky začíná na `test_`.

```python
# test_prevody.py
from prevody import dms_na_stupne


def test_severni_polokoule():
    assert abs(dms_na_stupne(49, 12, 30) - 49.208333) < 0.000001


def test_jizni_polokoule():
    assert abs(dms_na_stupne(-33, 52, 10) + 33.869444) < 0.000001


def test_nulove_souradnice():
    assert dms_na_stupne(0, 0, 0) == 0.0
```

Spustíte je příkazem

```
pytest
```

Pytest sám najde všechny soubory s testy a spustí je. Když je všechno v pořádku, vypíše za každý test tečku:

```
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\student\geo
collected 3 items

test_prevody.py ...                                                      [100%]

============================== 3 passed in 0.02s ==============================
```

Užitečnější je ale výstup ve chvíli, kdy něco neprojde. Tady implementace zapomněla, že na jižní polokouli se minuty a vteřiny od stupňů odečítají, ne přičítají:

```
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\student\geo
collected 3 items

test_prevody.py .F.                                                      [100%]

================================== FAILURES ===================================
____________________________ test_jizni_polokoule _____________________________

    def test_jizni_polokoule():
>       assert abs(dms_na_stupne(-33, 52, 10) + 33.869444) < 0.000001
E       assert 1.7388884444444486 < 1e-06
E        +  where 1.7388884444444486 = abs((-32.13055555555555 + 33.869444))
E        +    where -32.13055555555555 = dms_na_stupne(-33, 52, 10)

test_prevody.py:9: AssertionError
=========================== short test summary info ===========================
FAILED test_prevody.py::test_jizni_polokoule - assert 1.7388884444444486 < 1e-06
========================= 1 failed, 2 passed in 0.04s =========================
```

Číst se to dá ve třech krocích. Na řádku `test_prevody.py .F.` vidíte, že prostřední test selhal, protože tečka znamená úspěch a `F` neúspěch. V bloku FAILURES pytest rozepíše, jak k výsledku došel. A na posledním řádku rozpisu je vidět jádro věci: funkce vrátila -32.13 místo očekávaných -33.87, tedy minuty a vteřiny přičetla k zápornému číslu.

### Co testovat

Ke každé funkci alespoň tři případy:

* **typický vstup**, u kterého znáte správnou odpověď,
* **hraniční případ**, tedy nula, záporné číslo, prázdný vstup,
* **případ, u kterého čekáte chybu**, abyste ověřili, že se kód zachová, jak má.

### Druhy testů

Testům, které píšeme v této kapitole, se říká **jednotkové**, anglicky unit testy. Ověřují jednu funkci samostatně, nesahají na disk ani na síť a proběhnou v řádu milisekund.

Kromě nich se v praxi rozlišují ještě dvě úrovně:

* **Integrační test** ověří, že spolu několik částí funguje dohromady. U nás by to byla funkce, která načte shapefile a vrátí přefiltrovanou tabulku. Potřebuje skutečný soubor na disku, takže už není izolovaná.
* **End to end test** spustí celou úlohu tak, jak ji spustí uživatel, a zkontroluje výsledek na konci. U geoinformatického skriptu to znamená pustit celý výpočet a ověřit, že výstupní soubor vznikl, má správný souřadnicový systém a očekávaný počet prvků. Protože se výsledek porovnává s tím, o kterém víte, že je správný, mluví se často také o regresním testu.

Nejde o nic specifického pro Python, stejné tři úrovně najdete v jakémkoli jazyce. Liší se jen rozsahem toho, co test pokrývá.

My zůstaneme u jednotkových testů. Píšou se nejsnáz, běží nejrychleji a u kódu od AI odhalí většinu chyb. Zbylé dvě úrovně vám zatím stačí znát jménem.

### Vývoj řízený specifikací

Dosud jsme se na specifikaci i na testy dívali odděleně. Dohromady tvoří přístup, kterému se říká spec-driven development.

Myšlenka je jednoduchá. Dřív se psal kód a testy se k němu případně dopsaly potom. Když ale kód píše AI, těžiště se přesouvá dopředu, na to, co napíšete **před** ním. Specifikace a testy se stávají tím cenným, co v projektu zůstává, zatímco vygenerovaný kód je levný a kdykoli nahraditelný.

Z toho plyne návyk, který se vyplatí si osvojit hned. **Když je kód špatně, neopravujte ho ručně po řádcích. Nejdřív se ptejte, jestli chyba nebyla už v zadání.** Ve většině případů tam byla, protože jste zapomněli na jednotky, na hraniční případ nebo na chybějící hodnoty. Doplníte specifikaci, doplníte test a necháte kód vygenerovat znovu.

Postup má šest kroků:

1. Napište specifikaci.
2. Podle ní napište testy. **Ještě před tím, než existuje kód.**
3. Nechte AI napsat implementaci.
4. Spusťte testy.
5. Když něco neprojde, popište AI, co selhalo, a nechte to opravit.
6. Opakujte, dokud testy neprojdou.

Testy z druhého kroku vám zůstanou. Až kód za měsíc změníte, řeknou vám, jestli jste něco nerozbili.

Specifikace může být obyčejný docstring nad funkcí, komentář na začátku souboru nebo samostatný soubor s popisem úlohy. Podstatné není kam ji napíšete, ale že existuje dřív než kód.
