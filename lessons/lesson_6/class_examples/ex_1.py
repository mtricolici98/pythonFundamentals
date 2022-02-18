nested_dict_exemple = [
    {
        'dict': {
            'name': 'Marius'
        }
    }
]


inner_dicts = [out_dict['dict'] for out_dict in nested_dict_exemple]

print(inner_dicts)
print(nested_dict_exemple)

inner_dicts[0]['name'] = 'Andrei'

print(inner_dicts)
print(nested_dict_exemple)
