import pandas as pd
import numpy as np
# from sdv.metadata import MultiTableMetadata
# from sdv.multi_table import HMASynthesizer

parent = pd.DataFrame(data={
    'id': ['id_' + str(i) for i in range(10)],
    'A': list(np.random.uniform(low=0, high=10, size=10)),
    'B': list(np.random.choice(['value_0', 'value_1', 'value_2'], size=10))
})

child = pd.DataFrame(data={
    'id': ['id_' + str(i) for i in range(100)],
    'parent_id': ['id_' + str(i) for i in list(np.random.randint(low=0, high=10, size=100))],
    'C': list(np.random.uniform(low=0, high=10, size=100))
})

# metadata = MultiTableMetadata.load_from_dict({
#     'tables': {
#         'parent': {
#             'primary_key': 'id',
#             'columns': {
#                 'id': { 'sdtype': 'id', 'regex_format': 'id_\d{2}' },
#                 'A': { 'sdtype': 'numerical' },
#                 'B': { 'sdtype': 'categorical' }
#             }
#         },
#         'child': {
#             'primary_key': 'id',
#             'columns': {
#                 'id': { 'sdtype': 'id', 'regex_format': '\d{3}' },
#                 'parent_id': { 'sdtype': 'id', 'regex_format': 'id_\d{2}' },
#                 'C': { 'sdtype': 'numerical' }
#             }
#         }
#     },
#     'relationships': [{
#         'parent_table_name': 'parent',
#         'parent_primary_key': 'id',
#         'child_table_name': 'child',
#         'child_foreign_key': 'parent_id'
#     }]
# })

# synth = HMASynthesizer(metadata)
# synth.fit({
#     'parent': parent,
#     'child': child
# })
# synth.sample(scale=1)