#!/usr/bin/env python
INDEX_DIR = "Field.index"
import sys, os, lucene
 
from java.nio.file import Paths
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory, FSDirectory
from org.apache.lucene.search import IndexSearcher
from java.io import File
 
def run(searcher, analyzer):
    while True:
        print ("\nPress enter with no input to quit. \nIf field is blank, there is no data for it.")
        command = input("Query: ")
        if command == '':
            return
        print ("Searching for:", command)
        query = QueryParser("contents", analyzer).parse(command)

        scoreDocs = searcher.search(query, 50).scoreDocs
        print ("%s total matching documents found." % len(scoreDocs))
 
        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            fullpath = os.path.join(doc.get("path")+'/'+doc.get("name"))
            print ('\nLink to file:', fullpath, "\nDocument_ID:", doc.get("doc_id"), "\nFrom:", doc.get("from_"), "\nSubject:", doc.get("subj"))
 
if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = SimpleFSDirectory(Paths.get(os.path.join(base_dir, INDEX_DIR)))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = StandardAnalyzer()
    run(searcher, analyzer)
    del searcher