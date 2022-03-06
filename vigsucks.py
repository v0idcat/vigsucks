import datetime, string, time, langid
from guess_language import guess_language
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

encrypted = "smofzqa jdfv"    # Ciphertext
dictList = "scrabbleList.txt" # Collins Scrabble Words 2019

def crackCipher(cipher, dictList):
    solutionsFound = 0
    decrypted = ""

    print("\nCounting length of dictionary...")
    numLines = sum(1 for line in open(dictList))
    print("Counted %d lines!\n" % numLines)
    now = datetime.datetime.now()
    print("Bruteforce started at:", now.strftime("%Y-%m-%d %H:%M:%S"))
    start = time.time()

    with open(dictList, 'r') as openFile:
        for currentLine in openFile:
            key = currentLine.lower()                  # .lower() for uniformity; key and ciphertext must match case
            decrypted = decipher(cipher, key.rstrip()) # Strips linefeed from key
            if checkLang(decrypted):
                solutionsFound += 1
                with open('solutions.txt', 'a') as solutionOutput:
                    solutionOutput.write("POSSIBLE SOLUTION #%d:\t%s\nKEY:\t\t\t%s" % (solutionsFound, decrypted, currentLine))

    now = datetime.datetime.now()
    print("Bruteforce ended at:", now.strftime("%Y-%m-%d %H:%M:%S"))
    timeElapsed = (time.time() - start) / 60.0
    print('Time taken is approximately %.2f minutes' % timeElapsed)
    print("\nTotal potential solutions found:", solutionsFound)
    print("Percentage of hits: %.3f%%" % (float((solutionsFound / numLines) * 100)))

def decipher(cipher, key): # linefeed must be stripped for key
    index = 0
    plaintext = ""
    for c in cipher:       # Deciphering text loop
        if c in string.ascii_lowercase:
            offset = ord(key[index]) - ord('a')
            posOffset = 26 - offset
            decrypted = chr((ord(c) - ord('a') + posOffset) % 26 + ord('a'))
            plaintext += decrypted
            index = (index + 1) % len(key)
        else:
            plaintext += c
    return plaintext

# Get the script of the episode, use some linux magic to separate each word from 
# every sentence and create a list then use that for language detection AND/OR 
# as keys for the cipher!

def checkLang(deciphered): # Using guess_language-spirit, langid AND langdetect
    checked = langid.classify(deciphered)
    if (guess_language(deciphered) == 'en') and (checked[0] == 'en') and (detect(deciphered) == 'en'): # like staring into your worst nightmares
        return True

crackCipher(encrypted, dictList)
