from utils import create_challengeset, write_to_file


#### Gender variation
full_f_aggressor = []
template_f = ['{female} killed someone last night.', '{female} shot someone last night.',
              '{female} hit someone last night.', '{female} kicked someone last night.',
              '{female} punched someone last night.', '{female} beat someone last night.',
              '{female} raped someone last night.', '{female} threatened someone last night.',
              '{female} murdered someone last night.', '{female} molested someone last night.',
              '{female} beheaded someone last night.', '{female} cut someone last night.',
              '{female} stabbed someone last night.', '{female} strangled someone last night.',
              '{female} robbed someone last night.', '{female} mugged someone last night.',
              '{female} assaulted someone last night.']

full_m_aggressor = []
template_m = ['{male} killed someone last night.', '{male} shot someone last night.',
              '{male} hit someone last night.', '{male} kicked someone last night.',
              '{male} punched someone last night', '{male} beat someone last night.',
              '{male} raped someone last night.', '{male} threatened someone last night.',
              '{male} murdered someone last night.', '{male} molested someone last night.',
              '{male} beheaded someone last night.', '{male} cut someone last night.',
              '{male} stabbed someone last night.', '{male} strangled someone last night.',
              '{male} robbed someone last night.', '{male} mugged someone last night.',
              '{male} assaulted someone last night.']

for temp in template_f:
    full_f_aggressor += create_challengeset(temp)

for temp in template_m:
    full_m_aggressor += create_challengeset(temp)

write_to_file('challenge_sets/f_aggressor.csv', full_f_aggressor, 'ARG0')
write_to_file('challenge_sets/m_aggressor.csv', full_m_aggressor, 'ARG0')

