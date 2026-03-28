import collections

def solve_substitution(ciphertext):
    # Mapping derived from the crib "Multi-factor authentication" and "Third-party"
    # Cipher char -> Plain char
    key_map = {
        '%': ' ', ':': 't', 'B': 'h', 'V': 'e', ')': 'o',
        'u': 'a', 'G':'n', 'o':'i', '9':'c','u':'a','s':'u',
        '"': 's', 'F': 'r', '3':'m','@':'l','U':'-','M':'f',
        'T':'b','X':'w',']':'y','8':'g',"'":'d','Q':'k',
        '~':'p','*':'v','J':'I','!':'.', '|':'q','H':'M','R':'S',
        'b':'G','?':'F','6':'z','v':',','C':'j','&':'D','\\':'P',
        'N':'A','>':'W','f':'2','#':'0','r':'8','d':'R','l':'T','{':'E',
        '(':'x','.':'K','+':'U','a':'[','w':'6','_':'C','P':'1','e':'3',
        '<':'4','j':'L', 'x':'(','A':',','}':'5','m':'9','i':'7','`':')',
        '/':'H','D':'O','W':']','L':'&',';':'B','4':"'",'p':'V','k':'N',
        'q':'"', " ": ':', 'k':'N','0':'j'
    }

    plaintext = []
    for char in ciphertext:
        if char in key_map:
            plaintext.append(key_map[char])
        elif char == '\n':
            plaintext.append('\n')
        else:
            # Keep unknown characters as is to spot them
            plaintext.append(f"[{char}]") 

    text = "".join(plaintext)            

    print(text)



ciphertext = r"""""" # inserted ciphertext here

print("Decrypting with Substitution Map")
solve_substitution(ciphertext)
