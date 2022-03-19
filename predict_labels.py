from utils import predict_sents, output_conf_matr

#### Predict sentences with AllenNLP with BiLSTM ####
model = 'structured-prediction-srl'
full_preds, predictions, gold_labels = predict_sents('challenge_sets/f_aggressor_bilstm.csv', model, 0, 0 )
output_conf_matr('results/conf_matr_f_bilstm', gold_labels, predictions)


#### Predict sentences with AllenNLP with BiLSTM ####
model = 'structured-prediction-srl-bert'
full_preds, predictions, gold_labels = predict_sents('challenge_sets/f_aggressor_bert.csv', model, 0, 0 )
output_conf_matr('results/conf_matr_f_bert', gold_labels, predictions)
