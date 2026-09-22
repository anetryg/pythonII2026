## Prostorová data bez ArcGISu

ArcPy z první kapitoly umí hodně, ale má dvě omezení. Potřebuje licenci ArcGIS Pro a běží jen na Windows. 

Existuje druhá cesta, otevřená a zdarma. Naučíme se tři knihovny, které spolu tvoří základ:

* **Shapely** pracuje s geometrií, tedy s body, liniemi a polygony.
* **GeoPandas** přidává atributovou tabulku a souřadnicový systém. Je to tabulka, ve které jeden sloupec obsahuje geometrie ze Shapely.
* **rasterio** čte a zapisuje rastrová data.

Budeme řešit stejné úlohy jako v kapitole o ArcPy a nad stejnými daty. Na konci porovnáte oba výsledky. Když se rozejdou, aspoň jeden z nich je špatně, a vy budete mít z minulé kapitoly nástroj, jak zjistit který.

### Instalace

**Neinstalujte tyhle knihovny do prostředí, které si nese ArcGIS Pro.** Je uzamčené a instalace skončí chybou. Vytvořte si samostatné prostředí úplně mimo ArcGIS.

```
python -m venv geo
geo/Scripts/activate
pip install geopandas rasterio pytest
```

Shapely se nainstaluje samo jako závislost GeoPandas.


## Shapely

Shapely umí geometrii a nic víc. Nezná souřadnicový systém, neví, odkud data pocházejí, a nepracuje s atributy. Počítá s čísly, která mu dáte.

### Vytvoření geometrie

```python
from shapely.geometry import Point, LineString, Polygon

bod = Point(16.61, 49.19)
linie = LineString([(0, 0), (1, 1), (2, 0)])
polygon = Polygon([(0, 0), (0, 2), (2, 2), (2, 0)])
```

### Vlastnosti

```python
print(polygon.area)      # 4.0
print(polygon.bounds)    # (0.0, 0.0, 2.0, 2.0)
print(linie.length)      # 2.8284271247461903
print(polygon.centroid)  # POINT (1 1)
```

### Operace

```python
okoli = bod.buffer(0.01)                  # obalová zóna
prunik = polygon.intersection(okoli)      # průnik
sjednoceni = polygon.union(okoli)         # sjednocení
rozdil = polygon.difference(okoli)        # rozdíl
```

### Prostorové vztahy

Vracejí True nebo False.

```python
print(polygon.contains(Point(1, 1)))    # True
print(linie.intersects(polygon))        # True
print(Point(5, 5).within(polygon))      # False
```

### Pozor na jednotky

Tohle je nejčastější tichá chyba. Shapely neví, v jakém souřadnicovém systému vaše čísla jsou.

```python
# polygon zadaný v zeměpisných souřadnicích
uzemi = Polygon([(16.5, 49.1), (16.6, 49.1), (16.6, 49.2), (16.5, 49.2)])
print(uzemi.area)    # přibližně 0.01
```

Výsledek není v metrech čtverečních ani v hektarech. Je to plocha ve **čtverečních stupních**, což je jednotka, která nedává geografický smysl, protože délka jednoho stupně se mění se zeměpisnou šířkou. Program doběhne, chybu nenahlásí, číslo vypadá jako číslo. Než něco měříte, musíte data převést do systému v metrech. Jak na to, je v další části.


## GeoPandas

GeoPandas je tabulka, která navíc umí geometrii. Vychází z knihovny pandas.

### Načtení dat

```python
import geopandas as gpd

silnice = gpd.read_file("data/SILNICE_DALNICE.shp")
uzemi = gpd.read_file("data/VELKOPLOS_ZVL_CHRAN_UZEMI.shp")

print(silnice.head())        # prvních pět řádků
print(len(silnice))          # počet prvků
print(silnice.columns)       # názvy sloupců
print(silnice.crs)           # souřadnicový systém
```

Načíst umí i GeoPackage, GeoJSON a další formáty. Zápis funguje obdobně:

```python
silnice.to_file("vystup.gpkg", layer="silnice", driver="GPKG")
```

### Souřadnicový systém

Každý GeoDataFrame ví, v jakém systému jeho geometrie je. Převod do jiného systému se dělá metodou `to_crs`.

```python
# 5514 je S-JTSK Krovak East North, český systém v metrech
silnice = silnice.to_crs(5514)
uzemi = uzemi.to_crs(5514)

silnice["delka_m"] = silnice.geometry.length
uzemi["plocha_ha"] = uzemi.geometry.area / 10000
```

Data v tomto kurzu jsou v S-JTSK už při načtení, takže u nich převod nic nezmění. Past je tady opačná: kdybyste je převedli do WGS84, délky a plochy začnou vycházet ve stupních. GeoPandas na to naštěstí upozorní varováním.

**Dvě vrstvy, které spolu mají něco dělat, musí být ve stejném systému.** GeoPandas vás na rozdílný systém upozorní, ale ne u všech operací, takže si to hlídejte sami.

### Výběr a filtrování

Funguje stejně jako v pandas.

```python
dlouhe = silnice[silnice["delka_m"] > 1000]
pojmenovane = silnice[silnice["JMENO"].notna()]
obojí = silnice[(silnice["delka_m"] > 1000) & (silnice["JMENO"].notna())]
```

### Prostorové spojení

Odpoví na otázku, které prvky jedné vrstvy se potkávají s prvky druhé.

```python
v_uzemi = gpd.sjoin(silnice, uzemi, how="inner", predicate="intersects")
print(len(v_uzemi))
```

Parametr `predicate` určuje vztah, nejčastěji `intersects`, `within` nebo `contains`.

### Překryv

Zatímco `sjoin` jen připojí atributy, `overlay` skutečně přepočítá geometrii.

```python
useky = gpd.overlay(silnice, uzemi, how="intersection")
useky["delka_v_uzemi"] = useky.geometry.length
```

### Agregace

```python
soucty = silnice.dissolve(by="kategorie", aggfunc="sum")
```


## rasterio

Zatímco předchozí knihovny pracují s vektorem, rasterio čte a zapisuje rastry. Pixely dostanete jako pole z knihovny numpy.

### Otevření a metadata

```python
import rasterio

with rasterio.open("data/dmr.tif") as src:
    print(src.crs)          # souřadnicový systém
    print(src.width, src.height)
    print(src.count)        # počet pásem
    print(src.bounds)       # rozsah
    print(src.transform)    # převod pixel na souřadnice
    print(src.profile)      # všechno dohromady
```

### Čtení pixelů

```python
with rasterio.open("data/dmr.tif") as src:
    pole = src.read(1)      # první pásmo jako numpy pole

print(pole.shape)
print(pole.min(), pole.max(), pole.mean())
```

### Pásmová matematika

Klasickým příkladem je vegetační index NDVI, který se počítá z červeného a blízkého infračerveného pásma.

```python
import rasterio
import numpy as np

with rasterio.open("data/scena.tif") as src:
    cervena = src.read(3).astype("float32")
    nir = src.read(4).astype("float32")
    profil = src.profile

# where zabrání dělení nulou tam, kde je součet pásem nulový
soucet = nir + cervena
ndvi = np.where(soucet == 0, 0, (nir - cervena) / soucet)
```

### Zápis výsledku

Profil ze vstupního souboru se upraví a použije pro výstup, aby si rastr zachoval umístění a souřadnicový systém.

```python
profil.update(dtype="float32", count=1)

with rasterio.open("ndvi.tif", "w", **profil) as dst:
    dst.write(ndvi.astype("float32"), 1)
```

### Ořez podle polygonu

Tady se vektor a rastr potkávají.

```python
import geopandas as gpd
import rasterio
from rasterio.mask import mask

uzemi = gpd.read_file("data/VELKOPLOS_ZVL_CHRAN_UZEMI.shp")

with rasterio.open("data/dmr.tif") as src:
    uzemi = uzemi.to_crs(src.crs)
    orez, orez_transform = mask(src, uzemi.geometry, crop=True)
```

I tady platí, že vektor a rastr musí být ve stejném souřadnicovém systému. Proto se vrstva převádí podle toho, co má rastr.
