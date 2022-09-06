import requests
import json
from pprint import pprint

#KEY = '8be6bdbd-78ee-4efb-91a2-3854f79a97e0'
KEY = '4ac4317e-cf96-4222-ba17-753d12dc7a2f'
URL = 'https://babelnet.io/v7/getSynset?id={}&key={}&targetLang=IT&searchLang=IT'

def terms_list(path):
    terms = []

    with open (path, 'r') as f:
        for line in f:
            terms.extend([word.replace('\n','') for word in line.split('\t')])
    
    return terms

def synset_list(term_list, path):
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
    return res

def find_term_positions(term_list, lines):
    res = {'':[]}
    word = ''
    end = 0
    for i in range(len(lines)):
        if lines[i].find('#') == 0:
            res[word].append(end)
            word = ''
        if lines[i][1:-1] in term_list:
            word = lines[i][1:-1]
            end = i+1
            res[word] = [i]
        else:
            end += 1
    del res['']
    return res

def get_babel_syns_ids(term, terms_positions, lines):
    res = []
    start, end = terms_positions[term]
    for line in lines[start+1:end]:
        line = line.replace('\n', '')
        res.append(line)
    return res

def save_to_file(babel_syns_info):
    #url2 = 'results/result_lines_51_100.json'
    url2 = '/home/fazza/Documents/nlp-UniTO-2021-22/Radicioni/es3/results/result_lines_101_150.json'
    with open(url2, 'w') as f:
        json.dump(babel_syns_info, f, indent=4)

#terms = terms_list('term_list.txt')

terms = terms_list('/home/fazza/Documents/nlp-UniTO-2021-22/Radicioni/es3/resource/andrea_fabio_terms.txt')
res = synset_list(terms, '/home/fazza/Documents/nlp-UniTO-2021-22/Radicioni/data/es3_res/SemEval17_IT_senses2synsets.txt')

#res = synset_list(terms, '../data/es3_res/SemEval17_IT_senses2synsets.txt')
save_to_file(res)
#pprint(res)
print("Finito")
