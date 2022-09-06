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
    with open(path, 'r')


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





def save_to_file(babel_syns_info):
    #url2 = 'results/result_lines_51_100.json'
    url2 = '/home/fazza/Documents/nlp-UniTO-2021-22/Radicioni/es3/results/result_lines_101_150.json'
    with open(url2, 'w') as f:
        json.dump(babel_syns_info, f, indent=4)

#terms = terms_list('term_list.txt')

terms = terms_list('resources/andrea_fabio_terms.txt')
res = synset_list(terms, '/home/fazza/Documents/nlp-UniTO-2021-22/Radicioni/data/es3_res/SemEval17_IT_senses2synsets.txt')

#res = synset_list(terms, '../data/es3_res/SemEval17_IT_senses2synsets.txt')
save_to_file(res)
#pprint(res)
print("Finito")
