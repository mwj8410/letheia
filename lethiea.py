import random;
import sys;

DICTIONARY_FILE_NAME = 'dictionary.txt';
KEY_FILE_NAME = 'key.txt';
KEY_SIZE_MAX = 128;
KEY_SIZE_MIN = 32;
KEY_WORD_RATIO = 2;

CODE_CHARACTER_SET = '0123456789ABCDEF';

def generate_lookup_table(word_set, codebook_name):
    lookup_table_file = open(codebook_name, 'w');
    for index in range(len(word_set)):
        for code_index in range(KEY_WORD_RATIO):
            key_size = random.randrange(KEY_SIZE_MIN, KEY_SIZE_MAX);
            code_value = ''.join([random.choice(CODE_CHARACTER_SET) for x in range(key_size)]);
            lookup_table_file.write(str(index) + ':' + code_value + '\n');
    lookup_table_file.close();

def read_dictionary():
    dictionary_file = open(DICTIONARY_FILE_NAME, 'r');
    words = dictionary_file.readlines();
    output = [];
    for i in words:
        j = i.replace('\n','');
        output.append(j);
    return output;

# lethiea
if (len(sys.argv) < 3):
    print('Invalid number of arguments supplied.');
    sys.exit(0); # Incorrect error code
# lethiea -init <name> 
if (len(sys.argv) == 3 and sys.argv[1] == '-init'):
    generate_lookup_table(read_dictionary(), sys.argv[2] + '.tbl');
    print('New Codebook generated.');
    sys.exit(0);
# lethiea <code-book-name> -f <message-file-name>
if (len(sys.argv) == 4 and sys.argv[2] == '-f'):
    print('Encode indicated file');
    sys.exit(0);
# lethiea <code-book-name> -m "content"
if (len(sys.argv) == 4 and sys.argv[2] == '-m'):
    print('Encode inline message');
    sys.exit(0);
# lethiea <code-book-name> -d <file-name>
if (len(sys.argv) == 4 and sys.argv[2] == '-d'):
    print('decode indicated file');
    sys.exit(0);

print(sys.argv);