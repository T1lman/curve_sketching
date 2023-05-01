from sympy import *

init_printing(use_unicode=True, pretty_print=True)


x = symbols('x', real=True)

funktion = x**3+x**2

# Ersten 3 Ableitungen erstellen
ableitung1 = diff(funktion, x)
ableitung2 = diff(ableitung1, x)
ableitung3 = diff(ableitung2, x)

# Funktion sowie Ableitung printen
print(f"Funktionsuntersuchung der Funktion  : {funktion}")
print(f"Erste Ableitung  : {ableitung1}")
print(f"Zweite Ableitung : {ableitung2}")
print(f"Dritte Ableitung : {ableitung3}")


# Nullstellen finden
Nullstellen = solve(funktion, x)

# Nullstellen printen
for count, value in enumerate(Nullstellen):
    print(f"{count+1} Nullstelle: {value}")


# Extrempunkte finden
Extrempunkte_x = solve(ableitung1, x)
Extrempunkte_y = []

for i in Extrempunkte_x:
    Extrempunkte_y.append(funktion.subs(x, i))


# Extrempunkte in 2 Ableitung einsetzen
überprüfung_extrempunkte = []
for i in Extrempunkte_x:
    überprüfung_extrempunkte.append(ableitung2.subs(x, i))

# Extrempunkte mithilfe 2 Ableitung überprüfen,zuordnen und gegebnenfalls asudrucken
for count, value in enumerate(Extrempunkte_x):
    if überprüfung_extrempunkte[count] > 0:
        print(
            f"Der Extrempunkt {count+1} ist ein lokales Minimum und liegt bei ({float(value)}|{float(Extrempunkte_y[count])})")
    elif überprüfung_extrempunkte[count] < 0:
        print(
            f"Der Extrempunkt {count+1} ist ein lokales Maximum und liegt bei ({float(value)}|{float(Extrempunkte_y[count])})")


# Wendepunkte finden
Wendepunkte_x = solve(ableitung2, x)
Wendepunkte_y = []

for i in Wendepunkte_x:
    Wendepunkte_y.append(funktion.subs(x, i))


# Wendepunkte in 3 Ableitung einsetzen
überprüfung_wendepunkte = []
for i in Wendepunkte_x:
    überprüfung_wendepunkte.append(ableitung3.subs(x, i))


# Wendepunkte mithilfe 3 Ableitung überprüfen,zuordnen und gegebnenfalls asudrucken
for count, value in enumerate(Wendepunkte_x):
    if überprüfung_wendepunkte[count] > 0:
        print(
            f"Der Wendepunkt {count+1} beschreibt eine links-rechts Kurve und liegt bei ({float(value)}|{float(Wendepunkte_y[count])})")
    elif überprüfung_wendepunkte[count] < 0:
        print(
            f"Der Wendepunkt {count+1} beschreibt eine rechts-links Kurve und liegt bei ({float(value)}|{float(Wendepunkte_y[count])})")
