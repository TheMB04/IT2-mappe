assert 10> 5 #10 er strre enn 5, derfor gjør denne ingenting

try:
    assert 10 > 20 #10 er ikke større enn 20, derfor gir denne en feilmelding 
except:
    print("Hei på deg!")

# Oppgave: Definer en funksjon med navn areal, som tar inn en høyde og en bredde og returnerer arealet av en 
# rektangel med tilsvarende høyde og bredde

def areal(høyde, bredde):
    areal = høyde * bredde
    return areal

def omkrets(høyde, bredde):
    omkrets = høyde*2 + bredde*2
    return omkrets

#Oppgave: Test funksjonen areal på tre forskjellige rektangler

assert areal(3, 2) == 6
assert areal(3, 3) == 9
assert areal(3, 4) == 12
assert omkrets(3, 2) == 10
assert omkrets(3, 3) == 12
assert omkrets(3, 4) == 14


print(f"koden er ferdig")

