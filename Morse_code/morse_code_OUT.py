# řetězec, který chceme dekódovat
sifrovana_zprava = ".-.. . --- -. .- .-. -.. ---"
print(f"Původní zpráva: {sifrovana_zprava}")
# řetězec s dekódovanou zprávou
zprava = ""

# vzorové seznamy
abecedni_znaky = "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

# rozbití řetězce na znaky morzeovky
znaky = sifrovana_zprava.split(" ")

# iterace znaky morzeovky
for morseuv_znak in znaky:
    abecedni_znak = "?"
    try:
        index = morseovy_znaky.index(morseuv_znak)
        abecedni_znak = abecedni_znaky[index]
        zprava += abecedni_znak
    except ValueError: # znak nenalezen
        zprava += abecedni_znak

print(f"Dekódovaná zpráva je: {zprava}")