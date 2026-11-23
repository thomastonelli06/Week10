from model.model import Model
#vedi come mai non va
model = Model()
luoghi = model.get_luoghi()
for luogo in luoghi:
    print(luogo)


