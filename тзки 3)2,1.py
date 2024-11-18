def transpose_cipher(message, rows, cols):
    # Мәтінді кеңістіксіз алып, кестеге орналастырамыз
    message = message.replace(' ', '').upper()  # кеңістіктерді алып тастау
    # Егер мәтін ұяшықтарға толық сыймаса, соңына 'X' таңбасы қосамыз
    message = message.ljust(rows * cols, 'X')
    
    matrix = ['' for _ in range(rows)]
    
    # Кестеге бағандар бойынша жазу
    index = 0
    for col in range(cols):
        for row in range(rows):
            if index < len(message):
                matrix[row] += message[index]
                index += 1
    
    # Жолдар бойынша оқу
    encrypted_message = ''.join(matrix)
    
    # 5 әріптен тұратын топтарға бөлеміз
    encrypted_message_grouped = [encrypted_message[i:i+5] for i in range(0, len(encrypted_message), 5)]
    
    return ' '.join(encrypted_message_grouped)

# Тест
message = "СРЕДНИЙ РЕЗУЛЬТАТ ОКАЗАЛСЯ ВЫШЕ ОЖИДАНИЙ"
rows = 5
cols = 7

encrypted_message = transpose_cipher(message, rows, cols)
print(f"Шифрланған хабарлама: {encrypted_message}")
  
