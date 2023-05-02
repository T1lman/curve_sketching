from sympy import *
import numpy as np
from matplotlib import pyplot as plt


init_printing(use_unicode=True, pretty_print=True)

plt.rcParams["figure.autolayout"] = True
ax = plt.gca()
ax.set_xlim([-5, 5])
ax.set_ylim([-10, 10])


x = symbols('x', real=True)

input = input("Enter your Function: ")

funktion = eval(input)


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
Nullstellen_x = solve(funktion, x)
Nullstellen = []


# Nullstellen printen
for count, value in enumerate(Nullstellen_x):
    Nullstellen.append((value, 0))
    print(f"{count+1} Nullstelle: ({value}|0)")


# Sattelpunkte falls vorhanden
Sattelpunkte = []

# Extrempunkte finden
Extrempunkte_x = solve(ableitung1, x)
Extrempunkte_y = []
Extrempunkte = []


# Y werte der Extrempunkte finden
for i in Extrempunkte_x:
    Extrempunkte_y.append(funktion.subs(x, i))


# Extrempunkte in 2 Ableitung einsetzen
überprüfung_extrempunkte = []
for i in Extrempunkte_x:
    überprüfung_extrempunkte.append(ableitung2.subs(x, i))


# Extrempunkte mithilfe 2 Ableitung überprüfen,zuordnen und gegebnenfalls asudrucken
for count, value in enumerate(Extrempunkte_x):
    if überprüfung_extrempunkte[count] > 0:
        Extrempunkte.append((float(value), float(Extrempunkte_y[count])))
        print(
            f"Der Extrempunkt {count+1} ist ein lokales Minimum und liegt bei ({float(value)}|{float(Extrempunkte_y[count])})")
    elif überprüfung_extrempunkte[count] < 0:
        Extrempunkte.append((float(value), float(Extrempunkte_y[count])))
        print(
            f"Der Extrempunkt {count+1} ist ein lokales Maximum und liegt bei ({float(value)}|{float(Extrempunkte_y[count])})")
    else:
        Sattelpunkte.append((float(value), float(Extrempunkte_y[count])))
        print(
            f"Der Extrempunkt {count+1} ist ein Sattelpunkt und liegt bei ({float(value)}|{float(Extrempunkte_y[count])})")


# Wendepunkte finden
Wendepunkte_x = solve(ableitung2, x)
Wendepunkte_y = []
Wendepunkte = []

for i in Wendepunkte_x:
    Wendepunkte_y.append(funktion.subs(x, i))


# Wendepunkte in 3 Ableitung einsetzen
überprüfung_wendepunkte = []
for i in Wendepunkte_x:
    überprüfung_wendepunkte.append(ableitung3.subs(x, i))


# Wendepunkte mithilfe 3 Ableitung überprüfen,zuordnen und gegebnenfalls asudrucken
for count, value in enumerate(Wendepunkte_x):
    if überprüfung_wendepunkte[count] > 0:
        Wendepunkte.append((float(value), float(Wendepunkte_y[count])))
        print(
            f"Der Wendepunkt {count+1} beschreibt eine links-rechts Kurve und liegt bei ({float(value)}|{float(Wendepunkte_y[count])})")
    elif überprüfung_wendepunkte[count] < 0:
        Wendepunkte.append((float(value), float(Wendepunkte_y[count])))
        print(
            f"Der Wendepunkt {count+1} beschreibt eine rechts-links Kurve und liegt bei ({float(value)}|{float(Wendepunkte_y[count])})")


def f(x):
    return eval(input)


# deffinitionsbereich funktiongraph erstellen
x = np.linspace(-100, 100, 10000)

# funktion plotten
plt.plot(x, f(x), color='red')


for i in Nullstellen:
    plt.plot(i[0], i[1], marker="o", color="red")

for i in Extrempunkte:
    plt.plot(i[0], i[1], marker="o", color="green")

for i in Wendepunkte:
    plt.plot(i[0], i[1], marker="o", color="blue")


for i in Sattelpunkte:
    plt.plot(i[0], i[1], marker="o", color="pink")

plt.show()
