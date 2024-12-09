
def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')
def number_to_letter(number):
    return chr((number % 26) + ord('A'))

def matrix_determinant(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    raise ValueError("No modular inverse exists")

def matrix_inverse(matrix):
    det = matrix_determinant(matrix)
    det_inv = mod_inverse(det % 26, 26)


    inv_matrix = [
        [(matrix[1][1] * det_inv) % 26, (-matrix[0][1] * det_inv) % 26],
        [(-matrix[1][0] * det_inv) % 26, (matrix[0][0] * det_inv) % 26]
    ]
    return inv_matrix

def matrix_multiply(matrix, vector):
    result = [(matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % 26,
              (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % 26]
    return result


def hill_encrypt(message, key_matrix):
    message = message.upper().replace(" ", "")

    if len(message) % 2 != 0:
        message += 'X'

    encrypted_message = ''
    for i in range(0, len(message), 2):
        letter_pair = [letter_to_number(message[i]), letter_to_number(message[i+1])]
        encrypted_pair = matrix_multiply(key_matrix, letter_pair)
        encrypted_message += number_to_letter(encrypted_pair[0]) + number_to_letter(encrypted_pair[1])

    return encrypted_message


def hill_decrypt(ciphertext, key_matrix):
    ciphertext = ciphertext.upper().replace(" ", "")
    decrypted_message = ''
    key_matrix_inv = matrix_inverse(key_matrix)

    for i in range(0, len(ciphertext), 2):
        letter_pair = [letter_to_number(ciphertext[i]), letter_to_number(ciphertext[i+1])]
        decrypted_pair = matrix_multiply(key_matrix_inv, letter_pair)
        decrypted_message += number_to_letter(decrypted_pair[0]) + number_to_letter(decrypted_pair[1])

    return decrypted_message

print("Enter 2x2 key matrix (space-separated values):")
key_matrix = []
for i in range(2):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    key_matrix.append(row)
plaintext = input("Enter the message to encrypt: ")
ciphertext = hill_encrypt(plaintext, key_matrix)
print(f"Encrypted message: {ciphertext}")
decrypted_message = hill_decrypt(ciphertext, key_matrix)
print(f"Decrypted message: {decrypted_message}")


