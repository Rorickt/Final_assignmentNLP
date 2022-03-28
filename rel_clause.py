from utils import write_to_file
from utils import predict_sents, output_conf_matr, j_dumps
from checklist.editor import Editor


def create_elips():

    editor = Editor()

    object_ = ['bird','ball','stick','plane','girl','guy','cat','dog','car', 'bike', 'rabbit',
    'tree', 'sign']
    ## predicate ellipsis
    template_rel_clause_who = '{first_name} kicked a {object_} and {first_name1} a {object_1}'
    pred_elips_ = editor.template(template_rel_clause_who, object_=object_, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/ellipsis/pred_elips.csv', pred_elips_.data, 'ARG0')

    ## arg ellipsis
    template_rel_clause_who = '{first_name} walked home and saw a {object_}'
    pred_elips_ = editor.template(template_rel_clause_who, object_=object_, meta=True, nsamples=100, remove_duplicates=True)
    write_to_file('challenge_sets/ellipsis/arg_elips.csv', pred_elips_.data, 'ARG0')


def predict_elips():
    files = ['pred_elips.csv', 'arg_elips.csv']

    #### Predict sentences with AllenNLP with BiLSTM and BERT ####
    models = ['structured-prediction-srl','structured-prediction-srl-bert']
    for model in models:
        for file_ in files:
            if 'arg' in file_:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/ellipsis/'+file_, model, 1, 0 )
                j_dumps('predictions/ellipsis/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/ellipsis/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/ellipsis/'+file_+model[-4:]+'_results.txt', gold_labels, predictions)
            else:
                predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/ellipsis/'+file_, model, 0, 5 )
                j_dumps('predictions/ellipsis/'+file_+'_output'+model[-4:]+'.json', full_preds)
                j_dumps('predictions/ellipsis/'+file_+'_output_err'+model[-4:]+'.json', erred_preds)
                output_conf_matr('results/ellipsis/'+file_+model[-4:]+'_results.txt', gold_labels, predictions) 



