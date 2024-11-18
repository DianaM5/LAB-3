table = [
    ['Р', 'Е', 'С', 'П', 'У', 'Б'],
    ['Л', 'И', 'К', 'А', 'В', 'Г'],
    ['Д', 'Ж', 'З', 'М', 'Н', 'О'],
    ['Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш'],
    ['Щ', 'Ь', 'Ы', 'Э', 'Ю', 'Я']
]

def find_position(char):
    for i, row in enumerate(table):
        if char in row:
            return (i, row.index(char))
    return None


def encrypt_letter(char):
    pos = find_position(char)
    if pos is None:
        return char 

    new_row = (pos[0] + 1) % 5 
    new_char = table[new_row][pos[1]]
    return new_char

def encrypt_message(message):
    message = message.replace(" ", "")  
    encrypted_message = ""
    for char in message:
        encrypted_message += encrypt_letter(char)

    return encrypted_message


message = "ПРИВЕТ"  
encrypted_message = encrypt_message(message)
print(f"Зашифрованное сообщение: {encrypted_message}")
