# Lethiea

A prototype cipher application intended to demonstrate the basics of a non-formula based encoding methodology that
should represent highly difficult to functionally impossible to crack text message encoding. The weakness of this
approach is the total encoded message size, however the size before a message could be reliably decoded is so large
that the actual weakness is in the passing of the key table.

## Concept

First, for each word in the supplied dictionary, a number of pseudo-random hex-characters is generated as a key that
will be used in substitution of the word in the encoded message. By using more than one code per word, the complexity
of decoding without the key requires a significantly larger set of communicated messages. 

The point of using the hex codes for the key does not increase the difficulty of isolating a code. What it does is break
the linear sequencing of codes, which allows injecting fake codes in with valid codes. The randon length of the codes
means that the total encoded message size cannot be used as an indicator of the decosed message length. If the encoded
message is able to avoid using a deliminator, then the encoded message will be a sequence of un-broken hex digits.

## Discionary Source

We are using the 10,000 most common words in english as represented in
`https://github.com/first20hours/google-10000-english.git`.

## Usage (In Progress)

* `lethiea -init <name>` generates a code-book with the name provided.
* `lethiea <code-book-name> -f <message-file-name>` reads the text in the indicated message file and encodes it with the indicated code-book
* `lethiea <code-book-name> -m "content"` encode the inline message using the indicated code-book
* `lethiea <code-book-name> -d <file-name>` decodes the indicated file using the indicated code-book
