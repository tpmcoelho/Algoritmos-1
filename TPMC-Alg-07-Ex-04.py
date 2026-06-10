def morse(a, tabela_morse):
    tradução = []
    y = a.upper()
    for i in y:
        if i in tabela_morse:
            tradução.append(tabela_morse[i])
    return " ".join(tradução)

def main():
    morse_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", 
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", 
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", 
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", 
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", 
        "Z": "--..",
        "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-", 
        "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
    }
    
    x = input("Digite a mensagem para traduzir: ")
    resultado = morse(x, morse_dict)
    print(resultado)

main()