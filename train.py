from deeppavlov import configs
from deeppavlov.core.common.file import read_json
from deeppavlov import configs, train_model

model_config = read_json('train_config.json')

ranker = train_model(model_config)

docs = ranker(['cerebellum'])

print(docs)