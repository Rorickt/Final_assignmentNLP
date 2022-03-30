# NLP Technologies - Final Assignment

## General Info
A paper on Semantic Role Labeling focused challenge sets. The final assignment was to create challenge sets  that help to give insight into the (in)ability of an SRL system for five linguistic phenomena. \
The accompanied code gives the user the ability to create challenge sets for each test and retrieve the accuracy of semantic role labeling on these sets by two systems. Both of these systems are featured in the AllenNLP package. The package is also used to load the models and use them to predict the semantic roles.


## How to run
 
In the main folder one can find two coded files 'A_...' and 'B_...'.\
The User should first run *A_create_challengesets.py* to create the challenge data sets.\
Following this, the user can run *B_predict_challenge_sets.py* with any of the following commandline additions:\
`1`: to predict the passive sentence challenge tests\
`2`: to predict the manner influence challenge tests\
`3`: to predict the ellipsis challenge tests\
`4`: to predict the role set variation challenge tests\
`5`: to predict the theme-goal order variation challenge tests\
`6`: to predict the xx challenge tests

\
\
----CONTACT---- \
Rorick Terlou: m.r.terlou@student.vu.nl 

\
**Needed modules and packages**

- From sklearn.metrics: 
	- accuracy_score
	- load_predictor
- From checklist.editor
	- Editor
- allennlp_models.pretrained
	- load_predictor
- json
- sys
- torch
- csv