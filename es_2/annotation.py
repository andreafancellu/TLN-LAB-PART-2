from re import M
from nltk.corpus import framenet as fn
from nltk.corpus import wordnet as wn

def get_synset_from_frames(index):
    frame_name = fn.frame_by_id(index).name
    return wn.synsets(frame_name.split('_')[0])

frameSet = [{'id': 2641, 'name': 'Terrorism'}]


res = {}

# Nome synset - Esempio synset (in alternativa, lemmi, in alternativa iponimi)
# Nome Frame - Nome ricerca (lo split) - definizione del frame
for frame in frameSet:
    f = fn.frame_by_id(frame['id'])
    print(f"Nome Frame: {f.name}")
    print(f"Nome ricercato su wn: {frame['name'].split('_')[0]}")
    print(f"Definizione frame: {f.definition}")

    for synset in wn.synsets(frame['name'].split("_")[0]):
        print(f"Nome Synset: {synset.name()}")
        print(f"Definizione: {synset.definition()}")
        print(f"Esempi: {synset.examples()}")
        print(f"Lemmi: {synset.lemmas()}")
        print('\n')

    print('\n\n\n')
    for fe in f.FE:
        print(f"Nome FE: {f.FE[fe].name}")
        print(f"Nome ricercato FE: {f.FE[fe].name.split('_')[0]}")
        print(f"Definizione FE: {f.FE[fe].definition}\n")
        
        for syn in wn.synsets(f.FE[fe].name.split('_')[0]):
            print(f"Nome Synset: {syn.name()}")
            print(f"Definizione: {syn.definition()}")
            print(f"Esempi: {syn.examples()}")
            print(f"Lemmi: {syn.lemmas()}")
            print('\n')
    print('\n\n\n')
    i = 0
    for lu in f.lexUnit.keys():
        if i<20:
            print(f"Nome LU: {lu}")
            print(f"Nome ricercato LU: {lu.split('.')[0].split(' ')[0]}")
            print(f"Definizione LU: {f.lexUnit[lu].definition}\n")
            for syn in wn.synsets(lu.split(".")[0].split(" ")[0]):
                print(f"Nome Synset: {syn.name()}")
                print(f"Definizione: {syn.definition()}")
                print(f"Esempi: {syn.examples()}")
                print(f"Lemmi: {syn.lemmas()}")
                print('\n')
            i += 1
    print('\n\n\n')

valutation_dict = {
    'Chemical_potency': {
        'Chemical_potency':'chemical.n.01',
        'Chemical_entity':'chemical.n.01',
        'Degree':'',
        'Time':'time.n.03',
        'Circumstances':'circumstance.n.01',
        'Place':'place.n.02',
        'strong.a':'strong.a.01',
        'potent.a':'potent.s.02',
        'stiff.a':'potent.a.03'
    },
    'Fullness': {
        'Fullness': 'fullness.n.03',
        'Container' : 'container.n.01',
        'Contents': 'content.n.01',
        'Degree': 'degree.n.01',
        'Time': 'time.n.03',
        'Frequency': 'frequency.n.01',
        'Duration': 'duration.n.01',
        'full.a': 'full.a.01',
        'empty.a': 'empty.a.01',
        'emptiness.n': 'emptiness.n.01',
        'fullness.n': 'fullness.n.03'
    },
    'Causation': {
        'Causation': 'causing.n.01',
        'Cause': 'cause.n.01',
        'Affected': 'affected.a.01',
        'Effect': 'consequence.n.01',
        'Place': 'place.n.02',#topographic_point.n.01
        'Time': 'time.n.03',
        'Actor': 'actor.n.02',
        'Circumstances': 'context.n.02',
        'Manner': 'manner.n.01',
        'Explanation': 'explanation.n.01',
        'Means': 'means.n.01',
        'Frequency': 'frequency.n.01',
        'Concessive': 'concessive.a.01',
        'cause.v':'cause.v.01',
        'cause.n':'cause.n.01',
        'make.v':'make.v.03',
        'lead (to).v':'lead.v.03',
        'reason.n':'cause.n.02',
        'send.v':'send.v.01',
        'bring about.v':'bring.v.03',
        'precipitate.v':'precipitate.v.01',
        'causative.a':'causative.a.1',
        'render.v':'render.v.01',
        'bring.v':'bring.v.02',
        'bring on.v':'bring.v.02',
        'induce.v':'induce.v.01',
        'wreak.v':'bring.v.03',
        'put.v':'put.v.02',
        'since.c': None,
        'because.c': None,
        'because of.prep': None,
        'raise.v':'raise.v.03',
        'result (in).v':'result.v.01'
    },
    'Disgraceful_situation': {
        'Disgraceful_situation': 'disgraceful.s.01',
        'State_of_affairs': 'state.n.02',
        'Protagonist': 'protagonist.n.02',
        'Degree': 'degree.n.01',
        'Explanation': 'explanation.n.01',
        'Judge:': 'evaluator.n.01',#ha senso?
        'disgraceful.a': 'disgraceful.s.01',#ha senso?
        'shameful.a': 'disgraceful.s.01'#ha senso?
    },
    'Obviousness': {
        'Obviousness': 'obviousness.n.01',
        'Phenomenon': 'phenomenon.n.01',
        'attribute': 'property.n.04',
        'Degree': 'degree.n.01',
        'Time': 'time.n.03',
        'Circumstances': 'circumstance.n.01',
        'Perceiver': 'perceiver.n.01',
        'Evidence': 'evidence.n.02',
        'Group': 'group.n.01',
        'Location_of_protagonist': 'location.n.01',
        'Particular_iteration': 'particular.s.06',
        'Direction': 'direction.n.03',
        'obvious.a': 'obvious.a.01',
        'evident.a': 'apparent.s.01',
        'manifest.a': 'apparent.s.01',
        'visible.a': 'visible.a.01',
        'audible.a': 'audible.a.01',
        'unclear.a': 'unclear.a.02',
        'clear.a': 'clear.a.01',
        'clearly.adv': 'clearly.r.01',
        'obviously.adv': 'obviously.r.01',
        'clarity.n': 'clarity.n.01',
        'show.v': 'show.v.04',
        'show up.v': 'show.v.04',
        'stand out.v': 'stand.v.02',#ha senso?
        'noticeable.a': 'noticeable.a.01'
    },
    'Infrastructure': {
        'Infrastructure':'infrastructure.n.02',
        'Activity':'activity.n.01',
        'Place':'topographic_point.n.01',
        'Possessor':'owner.n.02',
        'Resource':'resource.n.02',
        'User':'user.n.01',
        'Descriptor':'descriptor.n.02',
        'Infrastructure':'infrastructure.n.01',
        'infrastructure.n':'infrastructure.n.01',
        'base.n':'basis.n.02'
    },
    'Product_line': {
        'Product_line': 'merchandise.n.01',
        'Brand' : 'trade_name.n.01',
        'Collection': 'collection.n.01',
        'Products': 'merchandise.n.01',
        'Descriptor': 'descriptor.n.02',
        'Collection_name': 'collection.n.01',
        'Designer': 'couturier.n.01',
        'line.n': 'line.n.22',
        'collection.n': 'collection.n.01'
    },
    'Gusto': {
        'Gusto': 'gusto.n.01',
        'Person': 'person.n.01',
        'Degree': 'degree.n.01',
        'life.n': 'liveliness.n.02',
        'vim.n': 'energy.n.05',
        'spirit.n': 'spirit.n.03'
    },
    'Military': {
        'Military': 'military.n.01',
        'Force': 'force.n.04',
        'Possessor': 'owner.n.02',
        'Descriptor': None,
        'Members': 'member.n.04',
        'Domain:': 'domain.n.02',
        'Goal': 'goal.n.01',
        'Period_of_existence': 'time_period.n.01',
        'military.n': 'military.n.01',
        'force.n': 'force.n.04',
        'navy.n': 'navy.n.01',
        'air force.n': None,
        'army.n': 'army.n.01',
        'naval.a': 'naval.a.01',
        'armed forces.n': None,
        'military.a': 'military.a.01',
        'military forces.n': 'military.n.01',
        'militia.n': 'militia.n.01',
        'national guard.n': None,
        'marines.n': 'marines.n.01',
        'coast guard.n': None
    },
    'Terrorism': {
        'Terrorism': 'terrorism.n.01',
        'Terrorist': 'terrorist.n.01',
        'Act': 'act.n.02',
        'Victim': 'victim.n.01',
        'Organization': 'organization.n.01',
        'Descriptor': 'descriptor.n.02',
        'Manner': 'manner.n.01',
        'Means': 'means.n.01',
        'Time': 'time.n.01',
        'Place': 'topographic_point.n.01',
        'Purpose': 'purpose.n.01',
        'Instrument': 'instrument.n.02',
        'terrorism.n': 'terrorism.n.01',
        'terrorist.n': 'terrorist.n.01',
        'ecoterrorism.n': 'ecoterrorism.n.01',
        'ecoterrorist.n': None,
        'bioterrorism.n': 'bioterrorism.n.01',
        'bioterrorist.n': None,
        'ecoterrorist.n': None,
        'ecoterrorism.n': 'ecoterrorism.n.01',
        'obviously.adv': 'obviously.r.01',
        'terror.n': 'terror.n.04'
    }
}