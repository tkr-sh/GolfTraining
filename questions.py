# sourcery skip: for-index-underscore
from random import*

*alphabet_low, = map(chr,range(97,123))

#############
# Arguments #
#############
# s: string lower
# S: string upper
# $: String upper or lower
# i: an integer
# u: unisgned integer
# f: a float
# d: a digit

questions = {
    'q1' : {
        'lang': 'python',
        'question':'Define 3 variables &&&1, &&&2, &&&3 as "&&&4","&&&5" and "&&&6" in this order',
        'response':'&&&1,&&&2,&&&3="&&&4&&&5&&&6"',
        'args': "sssddd"
    },
    'q2': {
        'lang': 'python',
        'question':'Write the condition (and only the condition) for a while loop that should run while &&&1 - 1 < &&&2',
        'response':'~-&&&1<&&&2',
        'args': "ss"
    },
    'q3': {
        'lang': 'python',
        'question':'Write the condition (and only the condition) for a while loop that should run while &&&1 + 1 > &&&2',
        'response':'-~&&&1>&&&2',
        'args': "ss"
    },
    'q4': {
        'lang': 'python',
        'question':'Declare a list/tuple &&&1 that contains numbers in the range [&&&2, &&&3[',
        'response': ['*&&&1,=range(&&&2,&&&3)', '&&&1=*range(&&&2,&&&3),'],
        'args': "sii",
        'rule': ["&&&2+9<&&&3"]
    },
    'q5': {
        'lang': 'python',
        'question':'You have a list &&&1. Declare a variable &&&2 which should be the last value of &&&1',
        'response':'*_,&&&2=&&&1',
        'args': "ss"
    },
    'q6': {
        'lang': 'python',
        'question':'Write a list/tuple &&&1 that contains all the letters of the alphabet in UPPERCASE',
        'response':['*&&&1,=map(chr,range(65,91))', '&&&1=*map(chr,range(65,91)),'],
        'args': "s"
    },
    'q7': {
        'lang': 'python',
        'question':'Write a list/tuple &&&1 that contains all the letters of the alphabet in lowercase',
        'response': ['*&&&1,=map(chr,range(97,123))', '&&&1=*map(chr,range(97,123)),'],
        'args': "s"
    },
    'q8': {
        'lang': 'python',
        'question':'You have a list &&&1 and an int &&&2. Get the (len(&&&1)-&&&2-1)th element of &&&1 ',
        'response':'&&&1[~&&&2]',
        'args': "ss"
    },
    'q9': {
        'lang': 'python',
        'question':'You have a list &&&1 and an int &&&2. Get the (len(&&&1)-&&&2)th element of &&&1 ',
        'response':'&&&1[-&&&2]',
        'args': "ss"
    },
    'q10': {
        'lang': 'python',
        'question':'You have a boolean &&&1. If &&&1 if true return "ON" else "OFF"',
        'response':'"OOFNF"[&&&1::2]',
        'args': "s"
    },
    'q11': {
        'lang': 'python',
        'question':'You have a list &&&1. Remove the last element of &&&1',
        'response':'*&&&1,_=&&&1',
        'args': "s"
    },
    'q12': {
        'lang': 'python',
        'question':'You have a set &&&1 and an element &&&2. Check if &&&2 is in &&&1',
        'response':['{&&&2}&&&&1', '&&&1&{&&&2}'],
        'args': "ss"
    },
    'q13': {
        'lang': 'python',
        'question':'You have a list &&&1 and an element &&&2. Add &&&2 to &&&1',
        'response': "&&&1+=&&&2,",
        'args': "s"
    },
    'q13': {
        'lang': 'python',
        'question':'You have a float &&&1. Return &&&1 floored',
        'response': '&&&1//1',
        'args': "s"
    },
    'q14': {
        'lang': 'python',
        'question':'You have a float &&&1. Return &&&1 ceilled',
        'response': '-(-&&&1//1)',
        'args': "s"
    },
    'q15': {
        'lang': 'python',
        'question':'You have a boolean &&&1 and an integer &&&2. If &&&1, return ~&&&2, else -&&&2',
        'response': ['-&&&2-&&&1','-&&&1-&&&2'],
        'args': "ss"
    },
    'q16': {
        'lang': 'python',
        'question':'You have a boolean &&&1 and an integer &&&2. If &&&1, return ~x, else x',
        'response': ['&&&2^-&&&1', '-&&&1^&&&2'],
        'args': "ss"
    },
    'q17': {
        'lang': 'python',
        'question':'You have a boolean &&&1 and an integer &&&2. If &&&1, return &&&2, else 1',
        'response': '&&&2**&&&1',
        'args': "ss"
    },
    'q18': {
        'lang': 'python',
        'question':'You have a boolean &&&1 and an integer &&&2. If &&&1, return &&&2, else 0',
        'response': ['&&&2*&&&1', '&&&1*&&&2'],
        'args': "ss"
    },
    'q19': {
        'lang': 'python',
        'question':'Read all STDIN as bytes',
        'response': 'open(0,"rb")',
        'args': ""
    },
    'q20': {
        'lang': 'python',
        'question':'Call the function &&&1 with the the char \'&&&2\' and \'&&&3\'',
        'response': '&&&1(*"&&&2&&&3")',
        'args': "sss"
    },
    'q21': {
        'lang': 'python',
        'question':'You have a list &&&1 and an element &&&2. Write the condition to check if &&&2 isn\'t in &&&1',
        'response': ['1^(&&&2 in &&&1)','(&&&2 in &&&1)^1','1-(&&&2 in &&&1)'],
        'args': "ss"
    },
    'q22': {
        'lang': 'ruby',
        'question':'You have a list &&&1. Join each element in &&&1 by \'&&&2\'',
        'response': "&&&1*?&&&2",
        'args': "ss"
    },
    'q23': {
        'lang': 'ruby',
        'question':'You have a 3 integers: &&&1, &&&2, &&&3. Return the sum of &&&1 and &&&2, times &&&3',
        'response': "&&&3.*&&&1+&&&2",
        'args': "sss"
    },
    'q24': {
        'lang': 'ruby',
        'question':'You have a list &&&1. Return &&&1 with unique elements',
        'response': "&&&1&&&&1",
        'args': "s"
    },
    'q25': {
        'lang': 'ruby',
        'question':'Define a list &&&1 with the first element being &&&2',
        'response': "*&&&1=&&&2",
        'args': "sd"
    },
    'q26': {
        'lang': 'ruby',
        'question':'Print "&&&1&&&2&&&3" with or without a newline at the end and without \"',
        'response': ["puts:&&&1&&&2&&&3", "$><<:&&&1&&&2&&&3"],
        'args': "$$$"
    },
    'q27': {
        'lang': 'ruby',
        'question':'You have a list &&&1 and a variable &&&2. Add &&&2 to &&&1',
        'response': "&&&1<<&&&2",
        'args': "ss"
    },
    'q28': {
        'lang': 'ruby',
        'question':'You have a list &&&1 of string that contains numbers. Return the sum of &&&1',
        'response': "eval &&&1*?+",
        'args': "s"
    },
    'q29': {
        'lang': 'ruby',
        'question':'You have a list &&&1. Remove the last element of &&&1.',
        'response': "*&&&1,_=&&&1",
        'args': "s"
    },
    'q30': {
        'lang': 'ruby',
        'question':'You have a function &&&1. Execute this function 9 times.',
        'response': ['eval"&&&1();"*9',"9.times{&&&1()}",'eval"&&&1[];"*9',"9.times{&&&1[]}"],
        'args': "s"
    },
    'q31': {
        'lang': 'ruby',
        'question':'You have a function &&&1. Execute this function 3 times.',
        'response': ['&&&1();&&&1();&&&1()','&&&1[];&&&1[];&&&1[]'],
        'args': "s"
    },
}