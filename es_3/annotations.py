import requests
import json
from pprint import pprint

#KEY = '8be6bdbd-78ee-4efb-91a2-3854f79a97e0'
KEY = '5da132f9-c606-4832-9a4f-3c2e3f739cf7'
KEY2 = 'd4bc0872-d933-4516-b456-2063fa7d68ff'
URL = 'https://babelnet.io/v7/getSynset?id={}&key={}&targetLang=IT&searchLang=IT'

## scheda madre: [id, id2, id3]

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
    x = requests.get(URL.format(value,KEY))
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
                    f.write(f"Possibile senso per parola {word}: {get_babel_syn(value)}\n")
                    

    

'''def synset_list(term_list, path):
    skipped = []
    res = {'skipped': skipped}
    with open(path, 'r') as file:
        lines = file.readlines()
        terms_positions = find_term_positions(term_list, lines)
        for term in terms_positions.keys():
            res[term] = {}
            babel_syns_ids = get_babel_syns_ids(term, terms_positions, lines)
            if len(babel_syns_ids) == 0:
                skipped.append(term)
                continue
            #print(term)
            #print(babel_syns_ids)
            for id in babel_syns_ids:
                #print(id)
                res[term][id] = []
                x = requests.get(URL.format(id,KEY))
                if x.status_code == 400:
                    #print("Bad request")
                    continue
                glosses = x.json()['glosses']
                senses = x.json()['senses']
                if len(senses) != 0:
                    res[term][id].append(senses[0]['properties']['fullLemma'])
                #for sense in senses:
                if len(glosses) != 0:
                    res[term][id].append(glosses[0]['gloss'])
            print("Finito ", term)
    return res'''


list_of_words = get_words_list('resources/andrea_fabio_terms.txt')
babel_dict = txt_to_dict('resources/SemEval17_IT_senses2synsets.txt')

print_syn(babel_dict, list_of_words)


'''terms = terms_list('resources/andrea_fabio_terms.txt')
res = synset_list(terms, 'resources/SemEval17_IT_senses2synsets.txt')
'''

print("Finito")
