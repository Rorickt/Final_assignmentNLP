from utils import create_challengeset

adjectives = ['round', 'square', 'triangular']
template = 'the woman kicked the {adj} ball.'

create_challengeset('trial_challengeset.csv', template, 'ARG0', input_list=adjectives)

