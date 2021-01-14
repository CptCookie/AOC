letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
           "n","o","p","q","r","s","t","u","v","w","x","y","z"]

def is_valid(password):
    doubles = 0
    last_double = -1
    adicent = False

    for n, c in enumerate(password):
        if c in ['i', 'o', 'l']:
            return False
        
        if n > 0:
            if c == password[n-1] and n > last_double+1:
                last_double = n
                doubles += 1
            
            if n < len(password) -1:
                letter_index = letters.index(c)
                if letters.index(password[n-1])+1 == letter_index and \
                    letters.index(password[n+1])-1 == letter_index:
                    adicent = True
    return doubles >= 2 and adicent

def increment(start):
    letter_int = [letters.index(n) for n in start][::-1]
    while True:
        for n in range(len(letter_int)):
            if n == 0:
                letter_int[n] += 1
            
            if letter_int[n] / 25 > 1:
                letter_int[n] = 0
                if n < len(letter_int)-1:
                    letter_int[n+1] += 1
                else:
                    letter_int.append(0)

        yield ''.join([letters[n] for n in letter_int[::-1]])

def next_password(old):
    for password in increment(old):
        if is_valid(password):
            return password

def solve(puzzle_input):
    puzzle_input = puzzle_input.split('\n')[0]
    new_password = next_password(puzzle_input)
    print(f"solution 1: {new_password}")
    print(f"solution 2: {next_password(new_password)}")
