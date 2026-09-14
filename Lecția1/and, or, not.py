vârsta=26
experiență=6
facultăți_terminate=2
#dacă vărsta este mai mare sau egală cu 24 si are mai mult de 2 luni de experiență, atunci va fi angajat.
print(vârsta>=24 and experiență>=2 and facultăți_terminate>=1)
#dacă are cel puțin 2 luni de experiență sau a terminat cel puțin o facultate, atunci va fi angajat.
print(experiență>=2 or facultăți_terminate>=1)
#dacă a terminat mai mult de o facultate, atunci va fi angajat numaidecât
print(not(not facultăți_terminate>1))
