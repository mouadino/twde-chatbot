# Documentation

## Machine learning and natural language processing
* [Deep Learning Book](http://www.deeplearningbook.org/)
* [Deep learning for natural language processing - CS Course at Stanford](http://cs224d.stanford.edu/syllabus.html)
* [Introduction to natural language understanding](https://www.oreilly.com/ideas/three-tips-for-getting-started-with-nlu)
* [NLP Papers from Google](https://research.google.com/pubs/NaturalLanguageProcessing.html)
* [NLP Papers from Facebook](https://research.fb.com/publications/?cat=8)

## Technical Approach
* [Contextual chatbots with Tensorflow](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077)
* [Part1: Trained neural net for Tensorflow and natural language understanding](https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html)
* [Part2: Trained neural net for Tensorflow and natural language understanding](https://research.googleblog.com/2017/03/an-upgrade-to-syntaxnet-new-models-and.html)
* [Small comparison between frameworks and their purpose](https://stackshare.io/stackups/rasa-nlu-vs-tensorflow-vs-walkme)
* [Discussion around frameworks](https://stackoverflow.com/questions/47379785/can-api-ai-rasa-nlu-be-integrated-with-tensorflow-to-make-a-chatbot?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa)
* [Simple workflow guide on how to train a chatbot model](https://nativemsg.com/blog/101-on-data-training-smart-chatbots)
* [Google NLU Division](https://research.google.com/teams/nlu/)
* [Google Hangouts bots](https://developers.google.com/hangouts/chat/how-tos/bots-develop)
* [Slack bots](https://api.slack.com/bot-users)

## Frameworks
* [Rasa Github](https://github.com/rasahq)
* [Rasa](http://rasa.com/)
* [Tensorflow Github](https://www.tensorflow.org/)
* [Tensorflow](https://github.com/tensorflow)
* [Amazon Lex](https://aws.amazon.com/de/lex/)
* [Chatbase - Chatbot analytics](https://chatbase.com)

## NLP datasets
[Collection of datasets](https://github.com/niderhoff/nlp-datasets)
[UCI Text datasets](http://archive.ics.uci.edu/ml/datasets.html?format=&task=cla&att=&area=&numAtt=&numIns=&type=text&sort=nameUp&view=table)
https://research.google.com/research-outreach.html#/research-outreach/research-datasets
freebase
https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus
https://www.clips.uantwerpen.be/conll2003/ner/

## theoretical problems
### intent classification
find correct intent for sentence, train classification deep neural net

how to vectorize sentence input? -> embedding
https://www.tensorflow.org/programmers_guide/embedding
https://research.fb.com/publications/advances-in-pre-training-distributed-word-representations/
https://www.tensorflow.org/tutorials/text_classification_with_tf_hub
https://research.fb.com/publications/enriching-word-vectors-with-subword-information-2/
https://www.tensorflow.org/hub/modules/google/universal-sentence-encoder/1
https://research.google.com/pubs/pub46808.html
https://research.googleblog.com/2017/11/sling-natural-language-frame-semantic.html
https://research.fb.com/publications/bag-of-tricks-for-efficient-text-classification/

### name entity recognition
automatically tag entities in sentence -> location, person, ...

entities can be bound to intention: order_food_intent, entities: food, quantity

charwnn neural net architecture, word2vec (tags need to be named)

[https://www.tensorflow.org/tutorials/word2vec](https://www.tensorflow.org/tutorials/word2vec)

[https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)

[https://arxiv.org/pdf/1505.05008.pdf](https://arxiv.org/pdf/1505.05008.pdf)

[http://proceedings.mlr.press/v32/santos14.pdf](http://proceedings.mlr.press/v32/santos14.pdf)

[https://www.aclweb.org/anthology/N16-1030](https://www.aclweb.org/anthology/N16-1030)

### context
e.g.:

> you can buy a, b, c
>
> i take the second one

-> with context b is chosen

reinforcement learning, q learning, but what are actions and what state?

[https://arxiv.org/pdf/1606.01541.pdf](https://arxiv.org/pdf/1606.01541.pdf)

### answering in natural language
