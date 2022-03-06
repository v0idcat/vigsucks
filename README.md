## *vigsucks.py*: "Bruteforcing" Vigenère cipher using python language detection modules.

I wrote this super quick script to bruteforce potential keys for a Vigenère cipher that I found in Gravity Falls (Season 2, Ep. 1, if you're curious). 
I think the creators of that show expected you to go through the entire episode and guess what the key might be, but I'm taking another approach. 


The script first sets `langdetect` module seed as `0` to have consistent results, then calls `crackCipher`, which is the main function that does the following:
1. Count length of dictionary + time of script start for stats
2. Iterate through dictionary, calling `decipher` function each time with a new line
3. Call `checkLang` function, which checks deciphered text for legibility using 3 different modules to reduce false positives.
4. If `checkLang` returns `True`, it'll save the resulting deciphered text + key used to a file called `solutions.txt`

**NOTE: This script is extremely inaccurate when it comes to long ciphertext;** it's primarily useful for very short ciphertext with simple keys as this is its purpose, after all. 

I've ran a total of 2 tests on this: one with a custom and relatively long ciphered text, and another that's the ciphertext found in Gravity Falls. 
I used "Collins Scrabble Words 2019" as the dictionary for both tests. 
Here's the custom cipher text (Ciphertext was `this is my encrypted text i hope nobody can crack it` and key was `therealcipher`):

![image](https://user-images.githubusercontent.com/40967439/156947218-fb135e7f-0c33-4ef8-b146-94c30aa4b3f9.png)

Here's the ciphertext from Gravity Falls that I managed to successfully and accurately crack:

![image](https://user-images.githubusercontent.com/40967439/156947305-99e7f638-7ef4-49cd-9fd0-e38d95fe3092.png)
![image](https://user-images.githubusercontent.com/40967439/156947316-8c378eee-2827-47af-a5d3-dfa2746655e6.png)


As you can see, the results can be iffy. 
