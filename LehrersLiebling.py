#
# TODO: Durch Eingabe von RP und GP p automatisch ermitteln!
#

p = int(input('?'))
if p > 100:
    n = 'Error: Not in Range'
elif p >= 95:
    n = 15
elif p >= 90:
    n = 14
elif p >= 85:
    n = 13
elif p >= 80:
    n = 12
elif p >= 75:
    n = 11
elif p >= 70:
    n = 10
elif p >= 65:
    n = 9
elif p >= 60:
    n = 8
elif p >= 55:
    n = 7
elif p >= 50:
    n = 6
elif p >= 45:
    n = 5
elif p >= 39:
    n = 4
elif p >= 33:
    n = 3
elif p >= 27:
    n = 2
elif p >= 20:
    n = 1
elif p < 20 and p >= 0:
    n = 0
else:
    n = 'ungültig'

print(n)
