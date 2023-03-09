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

