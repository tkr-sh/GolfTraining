# GolfTraining

This repo contains a set of questions to train your golfing skills<br>
You can contribute to this projects by creating any pull requests.<br>

## How to run the program
Just type `python3 main.py`. After that, you can choose the lang in which you want to train and it starts!<br>
_Note: The version of Python should be **3.10** or above_


## How to add a question
Questions are defined in `questions.py` and have many properties:
Parameters are written: `&&&n` with n an integer in [1:9].

### Langs
The language for the question
(Required)
### Question
The question
(Required)
### Response
The expected output
(Required)
### Args
The datatype of the arguments.
- s: string lower
- S: string upper
- $: String upper or lower
- i: an integer
- u: unisgned integer
- f: a float
- d: a digit
(Required)

### Rule
A list of rule. For example: `&&&1 < &&&2`.
(Optionnal)

## How to add a language
If you want to add a new programming language, add at least 3 questions for this programming language