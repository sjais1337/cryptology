from collections import Counter 

text = "JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX"
en_order = "ETAOINSHRDLUCMWFGXPBVKJQYZ"

freqs_l = [[pair[0], pair[1]] for pair in Counter(text).most_common()]
freqs = [pair[0] for pair in Counter(text).most_common()]

cipher_normal = dict(zip(freqs[0:10], en_order[0:10]))
cipher = dict(zip(freqs[0:3], en_order[0:3]))
deciphered = "".join(cipher.get(char, char) for char in text)
print(freqs_l)
print(deciphered)
