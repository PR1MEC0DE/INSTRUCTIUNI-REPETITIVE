#Cele trei variabile semnifica cantitatea de bani(S), procentajul de dobanda(p)
#Variabila(k) reprezinta numarul de luni
S = float(input("Ce cantitate de bani doriti sa depuneti in banca : "))
p = float(input("Ce procentaj va fi dobanda : "))
k = int(input("Cate luni vei tine aceasta cantitate de bani in banca : "))
print("Dupa ", k, "luni vei detine", ((S/100*p*k)+S), "de bani")

