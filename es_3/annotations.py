import requests
import json
from pprint import pprint

#KEY = '8be6bdbd-78ee-4efb-91a2-3854f79a97e0'
KEY = '5da132f9-c606-4832-9a4f-3c2e3f739cf7'
KEY2 = 'd4bc0872-d933-4516-b456-2063fa7d68ff'
URL = 'https://babelnet.io/v7/getSynset?id={}&key={}&targetLang=IT&searchLang=IT'

def txt_to_dict(path):
    res = {}
    with open(path, 'r') as file:
        for line in file.readlines():
            if line.find('#') == 0:
                word = line[1:].split('\n')[0]
                res[word] = []
            else:
                res[word].append(line)
    
    return res

def get_words_list(path):
    res = []
    with open(path, 'r') as file:
        for line in file.readlines():
            res = res + line.split('    ')
    return res


def get_babel_syn(value):
    s,g = None, None
    x = requests.get(URL.format(value,KEY2))
    if x.status_code == 400:
        print(f"Bad request con babelId: {value}")   
    else:
        s = x.json()['senses']
        if len(s) != 0:
            s = s[0]['properties']['fullLemma'] 
        
        g = x.json()['glosses']
        if len(g) != 0: 
            g = g[0]['gloss']
    return s,g
    


def print_syn(babel_dict, words):
    url2 = 'resources/result_lines_101_150.txt'
    with open(url2, 'w') as f:
        for word in words:
            word = word.split('\n')[0]
            if word in babel_dict.keys():
                for value in babel_dict[word]:
                    f.write(f"Parola {word} con id: {value}: {get_babel_syn(value)}\n")
            
            


list_of_words = get_words_list('resources/andrea_fabio_terms.txt')
babel_dict = txt_to_dict('resources/SemEval17_IT_senses2synsets.txt')

print_syn(babel_dict, list_of_words)
