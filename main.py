import re

code = {
        '': '',
        ' ': '',
        '-': '-****-'
        }

matches = []
pattern = r"([\w|/|+|=|.|,|?|(|)|-|'|\"|:|;|$]) {2}([-|*]+)"
with open('morse.txt', 'r') as file:
    data = file.read()
    matches = re.findall(pattern, data)
    for pair in matches:
        code[pair[0]] = pair[1]

code_to_en = {x: y for y, x in code.items()}


def translate_to_morse(sentence):
    n_sentence = []
    for letter in sentence:
        n_sentence.append(code[letter])
    n_sentence = '  '.join(n_sentence)
    print(n_sentence)


def translate_to_english(sentence):
    words = sentence.split('    ')
    print('Words: ', words)
    print(len(words))
    for i in range(1, len(words) + 1, 2):
        print(i)
        words.insert(i, 'n_word')
    print('Words after: ', words)
    n_sentence = []
    for word in words:
        word = word.split(' ')
        for letter in word:
            if letter == 'n_word':
                n_sentence.append('n_word')
            else:
                n_sentence.append(code_to_en[letter])
    print(n_sentence)
    n_sentence = ''.join(n_sentence).replace(' ', '')
    print(n_sentence)
    n_sentence = n_sentence.replace('n_word', ' ')
    print(n_sentence)

q = "Please enter a sentence to translate:\n"
translation_dir = "Write 'm' if you want to translate english to "\
                  "morse or 'e' for translation from morse to english:"\
                  "\n"


def main():
    dir = input(translation_dir)
    if dir == 'm':
        translate_to_morse(input(q).upper())
    elif dir == 'e':
        translate_to_english(input(q).upper())

if __name__ == '__main__':
    main()
