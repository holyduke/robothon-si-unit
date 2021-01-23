from whoosh.index import create_in
from whoosh.fields import *
from whoosh.query import Or, Term
from whoosh import scoring, qparser
import os

def create_index(name):
    schema = Schema(
        name=KEYWORD(stored=True),
        numbers=KEYWORD(stored=True),
        strings=KEYWORD(stored=True),
        id=NUMERIC(stored=True)
    )
    try:
        os.makedirs("index/" + name)
    except FileExistsError:
        pass
    ix = create_in('index/' + name, schema)
    return ix

def add_documents(ix, docs):
    writer = ix.writer()
    for [idx, doc] in enumerate(docs):
        name=" ".join(doc.data['key_name']) if isinstance(doc.data['key_name'], set) else doc.data['key_name']
        numbers=" ".join(doc.data['key_numbers']) if isinstance(doc.data['key_numbers'], set) else doc.data['key_numbers']
        strings=" ".join(doc.data['key_words']) if isinstance(doc.data['key_words'], set) else doc.data['key_words']
        if idx > 0 and idx % 100 == 0:
            print('added ' + str(idx) + ' documents...')
        writer.add_document(
            name=name,
            numbers=numbers,
            strings=strings,
            id=idx
        )
    writer.commit()
    print('added ' + str(len(docs)) + ' documents in total.')

def search(ix, tags, max_results=3, use_what=['name']):      

    matches = []
    with ix.searcher() as searcher:
        all_terms = []
        if 'name' in use_what:
            all_terms.extend([Term('name', n) for n in tags["name"]])
        if 'strings' in use_what:
            all_terms.extend([Term('strings', n) for n in tags["strings"]])
        if 'numbers' in use_what:
            all_terms.extend([Term('numbers', n) for n in tags["numbers"]])

        q = Or(all_terms)
        results = searcher.search(q, terms=True, limit=max_results)
        if(len(results) == 0):
            return []
        #print(results[0].matched_terms())
        #print([[x.score/len(all_terms), x] for x in results])
        for i in range(min(max_results, len(results))):
            matches.append([results[i].score/len(all_terms), results[i]['id'], results[i].matched_terms()]);
    return matches