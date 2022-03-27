from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor

def create_manner():
    
    editor = Editor()
    mann=['quickly','hastily','speedily','hurriedly','immediately','rapidly',
    'slowly','swiftly','calmly','casually','gently','lazily', 'nonchalantly', 'gradually']

    ###### BASE [variance test] ######
    template_manner_base = '{first_name} walked to the store last night.'
    full_mann_base = editor.template(template_manner_base, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/manner/full_mann_base.csv', full_mann_base.data, 'ARG0VARGM-DIRARGM-DIRARGM-DIRARGM-TMPARGM-TMPO')

    ###### Manner addition [variance test] ######
    template_manner_mnr1 = '{first_name} {mann} walked to the store last night.'
    template_manner_mnr2= '{first_name} {mann} ran to the house last night'
    template_manner_mnr3= '{first_name} {mann} flew to the country last night.'
    template_manner_mnr4= '{first_name} {mann} rode to the park last night.'
    # the gold label for the challengeset is a string of all combined SR labels (stripping 'B/I-')
    full_mann_mnr = editor.template(template_manner_mnr1, mann=mann, meta=True, nsamples=25, remove_duplicates=True)
    full_mann_mnr + editor.template(template_manner_mnr2, mann=mann, meta=True, nsamples=25, remove_duplicates=True)
    full_mann_mnr + editor.template(template_manner_mnr3, mann=mann, meta=True, nsamples=25, remove_duplicates=True)
    full_mann_mnr + editor.template(template_manner_mnr4, mann=mann, meta=True, nsamples=25, remove_duplicates=True)
    write_to_file('challenge_sets/manner/full_mann_mnr.csv', full_mann_mnr.data, 'ARG0ARGM-MNRVARGM-DIRARGM-DIRARGM-DIRARGM-TMPARGM-TMPO')



#### Predict sentences with AllenNLP with BiLSTM and BERT ####
def predict_manner():
    files = ['full_mann_base.csv', 'full_mann_mnr.csv']
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
                j_dumps('predictions/manner/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/manner/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/manner/'+file_+model[-4:]+'_results.txt', gold_labels, predictions) 


