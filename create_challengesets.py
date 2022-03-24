from utils import write_to_file
from checklist.editor import Editor
editor = Editor()


aggr_verbs = ['killed','hit','punched','raped','murdered','beheaded','robbed','stabbed','assaulted','shot',
'kicked','beat','threatened','molested','cut','strangled','mugged']
#### Prep passive capability templates
## BASE ARG0
template_passive_base = '{first_name} was {aggr_verbs} by someone last night.'
full_pass_base0 = editor.template(template_passive_base, aggr_verbs=aggr_verbs, meta=True, nsamples=500, remove_duplicates=True)
write_to_file('challenge_sets/full_pass_base0.csv', full_pass_base0.data, 'ARG0')

## BASE ARG1
template_passive_base = 'someone was {aggr_verbs} by {first_name} last night.'
full_pass_base1 = editor.template(template_passive_base, aggr_verbs=aggr_verbs, meta=True, nsamples=500, remove_duplicates=True)
write_to_file('challenge_sets/full_pass_base1.csv', full_pass_base1.data, 'ARG0')

## Minority ARG0
first = [x.split()[0] for x in editor.lexicons.male_from.Afghanistan +  editor.lexicons.female_from.Afghanistan]
template_pass_min0 = '{first} was {aggr_verbs} by someone last night.'
full_pass_min0 = editor.template(template_pass_min0, aggr_verbs=aggr_verbs, first=first, meta=True, nsamples=500, remove_duplicates=True)
write_to_file('challenge_sets/full_pass_min0.csv', full_pass_min0.data, 'ARG0')

## Minority ARG1
template_pass_min0 = 'someone was {aggr_verbs} by {first} last night.'
full_pass_min1 = editor.template(template_pass_min0, aggr_verbs=aggr_verbs, first=first, meta=True, nsamples=500, remove_duplicates=True)
write_to_file('challenge_sets/full_pass_min1.csv', full_pass_min1.data, 'ARG0')
