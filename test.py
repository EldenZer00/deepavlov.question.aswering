from deeppavlov import configs
from deeppavlov.core.commands.infer import build_model

odqa = build_model('model_config.json', download = False)

# for testing
a = odqa(["what is tuberculosis?"])

print(a)
