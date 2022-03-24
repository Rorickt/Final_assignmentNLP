from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor
editor = Editor()

mann=['quickly','hastily','speedily','hurriedly','immediately','rapidly',
'slowly','swiftly','calmly','casually','gently','lazily', 'nonchalantly', 'gradually']

#### Prep manner capability templates
## BASE [variance test]
template_manner_base = '{first_name} walked to the store last night.'
full_mann_base = editor.template(template_manner_base, meta=True, nsamples=50, remove_duplicates=True)
write_to_file('challenge_sets/manner/full_mann_base.csv', full_mann_base.data, 'ARG0VARGM-DIRARGM-DIRARGM-DIRARGM-TMPARGM-TMPO')

## Manner addition [variance test]
template_manner_mnr = '{first_name} {mann} walked to the store last night.'
full_mann_mnr = editor.template(template_manner_mnr, mann=mann, meta=True, nsamples=50, remove_duplicates=True)
write_to_file('challenge_sets/manner/full_mann_mnr.csv', full_mann_mnr.data, 'ARG0ARGM-MNRVARGM-DIRARGM-DIRARGM-DIRARGM-TMPARGM-TMPO')



files = ['full_mann_base.csv', 'full_mann_mnr.csv']

#### Predict sentences with AllenNLP with BiLSTM and BERT ####
models = ['structured-prediction-srl']#,'structured-prediction-srl-bert']
for model in models:
    for file_ in files:
        if 'MNR' in file_:
            predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/manner/'+file_, model, 0, 0, variance=True )
            j_dumps('predictions/manner/'+file_+'_output'+model[-4:]+'.json', full_preds)
            j_dumps('predictions/manner/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
            output_conf_matr('results/manner/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)
        else:
            predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/manner/'+file_, model, 0, 0, variance=True )
            j_dumps('predictions/manner/'+file_+'_outpuut'+model[-4:]+'.json', full_preds)
            j_dumps('predictions/manner/'+file_+'_output_erut'+model[-4:]+'.json', erred_preds)
            output_conf_matr('results/manner/'+file_+model[-4:]+'_results.txt', gold_labels, predictions) 


