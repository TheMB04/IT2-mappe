# Presentere data

Med data mener vi all mulig informasjon, det kan for eksempel være temperaturer, tekst, bilder, filmer.

I IT2 lærer vi om to forskjellige måter å presentere data på, nemlig ved tegning av grafer og med nettsider.

## Tegne grafer

For å tegne grafer i Python kan vi bruke biblioteket `matplotlib`.

> Installere matplotlib: `pip install matplotlib`

Tegne enkel graf med egne inputs:

```python
import matplotlib.pyplot as plt #importerer matplotlib

x = [0, 1, 2, 3, 4, 5]
y = [0, 2, 4, 6, 8, 10]

x = []
y = []

def f(x):
    return 3*x+2

for i in range(0, 6):
    x.append(i)
    y2 = f(i)
    y.append(y2)

plt.plot(x, y) # oppretter et plott
plt.scatter(x, y)
plt.show() # viser plottet
```


Vi kan også hente inn data fra csv eller json filer, og tegne en graf ut i fra informasjonen i filene:

```python
import matplotlib.pyplot as plt
fil = open("kolsaas.csv")
data = fil.read()

linjer = data.split("\n")
tur = []
for linje in linjer:
    splittet_linje = linje.split(",")
    tur.append(splittet_linje)
tur[1][0] # gir den første tiden, altså 0

x = []
y = []

for i in tur[1:]:
    x.append(i[0])
    y.append(i[3])

plt.scatter(x, y)
plt.style.use('fivethirtyeight')
plt.show()
```

## Lage nettsider (HTML/Flask)