from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor

def create_manner():
    editor = Editor()
    mann=['quickly','hastily','hurriedly','rapidly',
    'slowly','swiftly','calmly','casually','gently','lazily']

    ###### BASE [variance test] ######
    template_manner_base1 = '{first_name} walked to the store.'
    # the gold label for the challengeset is a string of all combined SR labels (stripping 'B/I-')
    full_mann_base = editor.template(template_manner_base1, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/manner/full_mann_base.csv', full_mann_base.data, 'ARG0VARGM-DIRARGM-DIRARGM-DIRO')


    ###### Manner addition [variance test] ######
    template_manner_mnr1 = '{first_name} {mann} walked to the store.'
    # the gold label for the challengeset is a string of all combined SR labels (stripping 'B/I-')
    full_mann_mnr = editor.template(template_manner_mnr1, mann=mann, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/manner/full_mann_mnr.csv', full_mann_mnr.data, 'ARG0ARGM-MNRVARGM-DIRARGM-DIRARGM-DIRO')

    ###### Manner addition [ARGdir test] ######
    template_manner_mnr1 = '{first_name} {mann} walked to the store last night.'
    # the gold label for the challengeset is a string of the first argument ('ARG-DIR')
    full_mann_mnr = editor.template(template_manner_mnr1, mann=mann, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/manner/temp_mann_mnr.csv', full_mann_mnr.data, 'ARG0ARGM-MNRVARGM-DIRARGM-DIRARGM-DIRARGM-TMPARGM-TMPO')



#### Predict sentences with AllenNLP with BiLSTM and BERT ####
def predict_manner():
    files = ['full_mann_base.csv', 'full_mann_mnr.csv', 'temp_mann_mnr.csv']
    models = ['structured-prediction-srl', 'structured-prediction-srl-bert']
    for model in models:
        for file_ in files:
            predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/manner/'+file_, model, 0, -2, variance=True )
            j_dumps('predictions/manner/'+file_+'_output'+model[-4:]+'.json', full_preds)
            j_dumps('predictions/manner/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
            output_conf_matr('results/manner/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)
