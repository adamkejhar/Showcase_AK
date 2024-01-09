# řetězec, který chceme zakódovat
print("Zadejte zprávu k zakódování: ")
sifrovana_zprava = input().lower()
# řetězec se zakódovanou zprávou
zprava = ""

# vzorové seznamy
abecedni_znaky = "abcdefghijklmnopqrstuvwxyz"
morseovy_znaky = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
"..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-",
"...-", ".--", "-..-", "-.--", "--.."]

znaky = sifrovana_zprava

# iterace znaky morzeovky
for abecedni_znak in znaky:
    morseuv_znak = "?"
    try:
        index = abecedni_znaky.index(abecedni_znak)
        morseuv_znak = morseovy_znaky[index]
        zprava += morseuv_znak +' '
    except ValueError: # znak nenalezen
        zprava += morseuv_znak

print(f"Zakódovaná zpráva je: {zprava}")