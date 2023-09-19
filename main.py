silvias_age = 26

olegs_age = silvias_age + 1

daniels_age = silvias_age - 1

# in Python kann man mit # Kommetare machen
# in Python kann man die vier Grundrechenarten +, -, *, / verwenden

# Eine Variable wird in Python als snake-Schreibweise benannt.
# Wird eine variable zuerst erwähnt, heißt das Deklaration.
# Wird einer Varianblen zum ersten mal ein Wert zugewiesen heißt das Initialisierung.

silvias_age_halbe = silvias_age / 2
silvias_age_doppelte = silvias_age_halbe * 4

print (olegs_age)
print (daniels_age)
print (silvias_age_halbe)
print (silvias_age_doppelte)

#Will man in Python einen Text (mehrere Buchstaben) ausgeben, setzt man das in "".

if silvias_age >= 18:
    print ("Du bist erwachsen, kümmer dich selbst!")
elif silvias_age == 35:
    print ("Hey, genau so alt wie ich!")
else: 
    print ("Geh und frag Mutti!")

# if elif else nimmt immer die erste Ausfahrt und guckt dann nicht weiter.

bank_account_balances = [5322.0, 577.41, -100.0]

for balance in bank_account_balances:
    print (balance)

schooling_horses = ["Fee", "Mirco", "Puschkin"]

for horse in schooling_horses:
    print (horse)

nordic_animals = ("raindeer", "polar bear", "whale")
for animal in nordic_animals:
    print (animal)