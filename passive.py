from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor

def create_passive():
    editor = Editor()
    aggr_verbs = ['killed','hit','punched','raped','murdered','beheaded','robbed','stabbed','assaulted','shot',
    'kicked','beat', 'threatened','molested','cut','strangled','mugged']
    #### Prep passive capability templates
    ## BASE ARG0
    template_passive_base0 = '{first_name} was {aggr_verbs} by someone last night.'
    full_pass_base0 = editor.template(template_passive_base0, aggr_verbs=aggr_verbs, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/passive/full_pass_base0.csv', full_pass_base0.data, 'ARG1')

    ## BASE ARG1
    template_passive_base1 = 'someone was {aggr_verbs} by {first_name} last night.'
    full_pass_base1 = editor.template(template_passive_base1, aggr_verbs=aggr_verbs, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/passive/full_pass_base1.csv', full_pass_base1.data, 'ARG0')

    ## Minority ARG0
    first = [x.split()[0] for x in editor.lexicons.male_from.Afghanistan +  editor.lexicons.female_from.Afghanistan]
    template_pass_min0 = '{first} was {aggr_verbs} by someone last night.'
    full_pass_min0 = editor.template(template_pass_min0, aggr_verbs=aggr_verbs, first=first, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/passive/full_pass_min0.csv', full_pass_min0.data, 'ARG1')

    ## Minority ARG1
    template_pass_min1 = 'someone was {aggr_verbs} by {first} last night.'
    full_pass_min1 = editor.template(template_pass_min1, aggr_verbs=aggr_verbs, first=first, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/passive/full_pass_min1.csv', full_pass_min1.data, 'ARG0')

    


#### Predict sentences with AllenNLP with BiLSTM and BERT ####
def predict_passive():
    files = ['full_pass_min1.csv', 'full_pass_min0.csv', 'full_pass_base1.csv', 'full_pass_base0.csv']
    models = ['structured-prediction-srl','structured-prediction-srl-bert']
    for model in models:
        for file_ in files:
            if '0' in file_:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/passive/'+file_, model, 1, 4 )
                j_dumps('predictions/passive/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/passive/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/passive/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)
            else:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/passive/'+file_, model, 1, 0 )
                j_dumps('predictions/passive/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/passive/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/passive/'+file_+model[-4:]+'_results.txt', gold_labels, predictions) 


