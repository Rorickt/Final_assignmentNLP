from utils import predict_sents, output_conf_matr, j_dumps

#### Predict sentences with AllenNLP with BiLSTM ####
model = 'structured-prediction-srl'
predictions, gold_labels, full_preds, erred_preds= predict_sents('challenge_sets/f_aggressor_bilstm.csv', model, 0, 0 )
j_dumps('predictions/f_aggressor_output.json', full_preds)
j_dumps('predictions/f_aggressor_output_err.json', erred_preds)
output_conf_matr('results/conf_matr_f_bilstm', gold_labels, predictions)

#### Predict sentences with AllenNLP with BiLSTM ####
model = 'structured-prediction-srl-bert'
predictions, gold_labels, full_preds, erred_preds = predict_sents('challenge_sets/f_aggressor_bert.csv', model, 0, 0 )
j_dumps('predictions/m_aggressor_output.json', full_preds)
j_dumps('predictions/m_aggressor_output_err.json', erred_preds)
output_conf_matr('results/conf_matr_f_bert', gold_labels, predictions)
