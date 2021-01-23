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
        id=ID(stored=True)
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
        name=" ".join(doc['name']) if isinstance(doc['name'], list) else doc['name']
        numbers=" ".join(doc['numbers']) if isinstance(doc['numbers'], list) else doc   ['numbers']
        strings=" ".join(doc['strings']) if isinstance(doc['strings'], list) else doc   ['strings']
        if idx > 0 and idx % 10 == 0:
            print('added ' + str(idx) + ' documents...')
        writer.add_document(
            name=name,
            numbers=numbers,
            strings=strings,
                id=doc['id']
        )
    writer.commit()
    print('added ' + str(len(docs)) + ' documents in total.')

def search(ix, tags):       
    match = []
    with ix.searcher() as searcher:
        name_terms = [Term('name', n) for n in tags["name"]]
        string_terms = [Term('strings', n) for n in tags["strings"]]
        number_terms = [Term('numbers', n) for n in tags["numbers"]]
        all_terms = [*name_terms, *string_terms, *number_terms]

        q = Or(all_terms)
        results = searcher.search(q)
        print([[x.score/len(all_terms), x] for x in results])
        match = [results[0].score/len(all_terms), results[0]['id']]
    return match