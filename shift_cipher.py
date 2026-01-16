text = "OVDTHUFWVZZPISLRLFZHYLAOLYL"

for k in range(0,26):
    final = ""
    for i in text:
        final = final + chr(ord("A") + ((ord(i) + k) % 26) )

    print(final)
