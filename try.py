from utils import predict_sents, output_conf_matr, j_dumps

#### Predict sentences with AllenNLP with BiLSTM ####
model = 'structured-prediction-srl'
predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/f_aggressor.csv', model, 0, 0 )
output_conf_matr('results/conf_matr_f_bilstm', gold_labels, predictions)