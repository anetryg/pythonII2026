# Data k následujícím úkolům najdete ve složce 01-arcpy/data - jedná se o liniovou vrstvu silnic a polygonovou vrstvu chráněných území

# Úkol 1
""" 
V rámci Python notebooku nejprve do vrstvy SILNICE_DALNICE vložte nový sloupec, který pojmenujete "kategorie" a který bude typu TEXT. Pokud bude mít linie vyplněný sloupec "JMENO" a délka linie bude větší než 1000, vložte do sloupce "kategorie" hodnotu "01", pokud ne, pak vložte hodnotu "00".
"""


# Úkol 2
""" Vytvořte pomocí Python notebooku v ArcGISu Pro histogram z vrstvy SILNICE_DALNICE na základě sloupce SHAPE_Leng, který vyexportujete jako svg. Histogram bude rozdělen na 7 sloupců, vytvořte název grafu, pojmenujte osy x a y a přidejte popis grafu. """


# Úkol 3
""" Vytvořte Python toolbox pro ArcGIS Pro, který bude jako první parametr přijímat vrstvu (v našem případě očekávejme polygonovou vrstvu chráněných území VELKOPLOS_ZVL_CHRAN_UZEMI) a jako druhý parametr bude možné vybrat mezi dvěma hodnotami "min" nebo "max". Na základě toho, jestli uživatel zvolí min nebo max najdete buď rozlohou nejmenší polygon nebo největší a jeho fid_zbg (jedinečný identifikátor) si uložte do proměnné. Následně vytvořte pomocí geoprocessingu ze vstupní polygonové vrstvy bodovou vrstvu (Feature To Point), v této vrstvě najděte podle fid_zbg bod nejmenšího nebo největšího polygonu a vraťte jeho souřadnice a název. 
"""
