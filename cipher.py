import random;

DICTIONARY_FILE_NAME = 'dictionary.txt';
KEY_FILE_NAME = 'key.txt';
LOOKUP_TABLE_FILE_NAME = 'lookup.tbl';

KEY_FILE_SIZE = 2048;
KEY_SIZE_MAX = 128;
KEY_SIZE_MIN = 32;


# def encode_message(message, lookup_table):
    

def generate_key_file():
    key_file = open(KEY_FILE_NAME, 'w')
    code = ''.join([random.choice('0123456789ABCDEF') for x in range(KEY_FILE_SIZE)]);
    key_file.write(code);
    key_file.close();
    
def generate_lookup_table(word_set, key_file):
    lookup_table_file = open(LOOKUP_TABLE_FILE_NAME, 'w');
    for index in range(len(word_set)):
        key_start = random.randrange(0, (KEY_FILE_SIZE - KEY_SIZE_MAX));
        key_size = random.randrange(KEY_SIZE_MIN, KEY_SIZE_MAX);
        code_value = key_file[key_start:(key_start + key_size)];
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

def read_key_file():
    key_file = open(KEY_FILE_NAME, 'r');
    output = key_file.read();
    key_file.close();
    return output;


generate_key_file();
word_set = read_dictionary();
generate_lookup_table(word_set, read_key_file());
