# Presentere data

Med data mener vi al mulig informasjon, det kan for esempel være temperaturer, tekst, bilder, filmer.

I IT2 lærer vi om to forskjellige måter å presentere data på, benlig ved tegning av grafer og med nettsider.

## Tegne grafer

For å tegne grafer i Python kan vi bruke biblioteket `matplotlib`.

> Installere matplotlib: `pip install matplotlib`
> Importere matplotlib: `import matplotlib.pyplot as plt`

Tegne enkel graf med egne inputs:

```python
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

## Lage nettsider (HTML/Flask)