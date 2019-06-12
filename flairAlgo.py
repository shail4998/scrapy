from flair.data import Sentence
from flair.models import SequenceTagger

def tagIt(title, noOfTags):
    # make a sentence
    sentence = Sentence(title)
    # load the NER tagger
    tagger = SequenceTagger.load('ner') #ner-fast for cpu, in case youy are poor

    # run NER over sentence
    tagger.predict(sentence)

    # iterate over entities and print
    for entity in sentence.get_spans('ner'):
            noOfTags.append(entity.text)