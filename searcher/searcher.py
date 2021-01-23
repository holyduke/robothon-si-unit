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
    for doc in docs:
        writer.add_document(
            name=doc['name'],
            numbers=doc['numbers'],
            strings=doc['strings'],
            id=doc['id']
        )
    writer.commit()

def search(ix, tags):
    with ix.searcher() as searcher:
        name_terms = [Term('name', n) for n in tags["name"]]
        string_terms = [Term('strings', n) for n in tags["strings"]]
        number_terms = [Term('numbers', n) for n in tags["numbers"]]

        q = Or([*name_terms, *string_terms, *number_terms])
        results = searcher.search(q)
        print([[x.score, x] for x in results])

