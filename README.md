# Encryptor

## Description
Python console script that encrypts/decrypts messages

## Basic working principle
This cipher works in a similar fashion to a caesar cipher, but each substitution is not simply replacing a character with a letter three 'steps backward' in the alphabet. For given keys (3 keys) and for each position in the given message this program generates a 'random step' in the alphabet. Each letter is then replaced following this formula, where x is the position in the alphabet of the plain character and '%' is the modulo operator:<br>
##### (x + 'random step') % (number of symbols in a given alphabet) = new position in the alphabet<br>
Random step is never 0, therefore it is always going to replace a character with a different one<br>
Given alphabet is always specifed on top of the script and can be modifed freely. The alphabet I used has 96 characters, therefore has a maximum theoretical number of brute iterations equal to 96^(message length).

## Notes
- Script performs encryption "iterations" (code variable) times, default is 5 (more can be slow).<br>
- Program can be easily quit of out by typing 'exit'.





