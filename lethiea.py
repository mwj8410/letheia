import random
import re
import sys

DECODE_FILE_NAME = 'decoded.txt'
DICTIONARY_FILE_NAME = 'dictionary.txt'
ENCODED_FILE_NAME = 'encoded.txt'
KEY_FILE_NAME = 'key.txt'
KEY_SIZE_MAX = 128
KEY_SIZE_MIN = 32
KEY_WORD_RATIO = 2

CODE_CHARACTER_SET = '0123456789ABCDEF'

def decode_message(code, key, dictionary):
    decode_partial = code
    for i in key:
        decode_partial = decode_partial.replace(i[1], '[' + get_word_by_index(int(i[0]), dictionary) + ']')
    word = re.compile('\[[a-z\s]*.\]')
    return normalize_message(' '.join(word.findall(decode_partial)))

def encode_message(message, key, dictionary):
    message_parts = str.split(message, ' ')
    output = []
    for i in message_parts:
        index = dictionary.index(i) # get the index/id of the word
        output.append(extract_code(index, key))
    return pad_codes(output)

def extract_code(index, key):
    index_str = str(index)
    choices = filter(lambda (i): i[0] == index_str, key)
    return choices[random.randrange(0, len(choices))][1]

def generate_lookup_table(word_set, codebook_name):
    lookup_table_file = open(codebook_name, 'w')
    for index in range(len(word_set)):
        for code_index in range(KEY_WORD_RATIO):
            key_size = random.randrange(KEY_SIZE_MIN, KEY_SIZE_MAX)
            code_value = ''.join([random.choice(CODE_CHARACTER_SET) for x in range(key_size)])
            lookup_table_file.write(str(index) + ':' + code_value + '\n')
    lookup_table_file.close()

def get_word_by_index(index, dictionary):
    return dictionary[index]

def normalize_message(message):
    charset = 'abcdefghijklmnopqrstuvwxyz '
    output = ''.join([c for c in message.lower() if c in charset])
    return output

def pad_codes(codes):
    output = []
    for i in codes:
        junk_size = random.randrange(1, KEY_SIZE_MIN)
        junk_value = ''.join([random.choice(CODE_CHARACTER_SET) for x in range(junk_size)])
        output.append(junk_value)
        output.append(i)
    return output

def read_dictionary():
    dictionary_file = open(DICTIONARY_FILE_NAME, 'r')
    words = dictionary_file.readlines()
    output = []
    for i in words:
        j = i.replace('\n','')
        output.append(j)
    return output

def read_encoded_file(file_name):
    dictionary_file = open(file_name, 'r')
    content = dictionary_file.readlines()[0]
    dictionary_file.close()
    return content

def read_lookup_table(filename):
    file_contents = open(filename + '.tbl', 'r').readlines()
    output = []
    for i in file_contents:
        j = i.replace('\n','')
        output.append(str.split(j, ':'))
    return output

def save_decoded_message(message_content):
    message_file = open(DECODE_FILE_NAME, 'w')
    message_file.write(message_content)
    message_file.close()

def save_encoded_message(codes):
    message_file = open(ENCODED_FILE_NAME, 'w')
    message_file.write(''.join(codes))
    message_file.close()

def trin_junk(content):
    content
    
# lethiea
if (len(sys.argv) < 3):
    print('Invalid number of arguments supplied.')
    sys.exit(0) # Incorrect error code

# lethiea -init <name> 
if (len(sys.argv) == 3 and sys.argv[1] == '-init'):
    generate_lookup_table(read_dictionary(), sys.argv[2] + '.tbl')
    print('New Codebook generated.')
    sys.exit(0)

# lethiea <code-book-name> -f <message-file-name>
if (len(sys.argv) == 4 and sys.argv[2] == '-f'):
    print('Encode indicated file')
    lookup_table_file_name = sys.argv[1]
    file_name = sys.argv[3]
    save_encoded_message(
        encode_message(
            read_encoded_file(file_name),
            read_lookup_table(lookup_table_file_name),
            read_dictionary()
        )
    )
    sys.exit(0)

# lethiea <code-book-name> -m "content"
if (len(sys.argv) == 4 and sys.argv[2] == '-m'):
    print('Encode inline message')
    lookup_table_file_name = sys.argv[1]
    message_content = normalize_message(sys.argv[3])
    save_encoded_message(
        encode_message(
            message_content,
            read_lookup_table(lookup_table_file_name),
            read_dictionary()
        )
    )
    sys.exit(0)

# lethiea <code-book-name> -d <file-name>
if (len(sys.argv) == 4 and sys.argv[2] == '-d'):
    print('decode indicated file')
    lookup_table_file_name = sys.argv[1]
    file_name = sys.argv[3]
    save_decoded_message(
        decode_message(
            read_encoded_file(file_name),
            read_lookup_table(lookup_table_file_name), read_dictionary()
        )
    )
    sys.exit(0)

print(sys.argv)