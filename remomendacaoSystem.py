# instalar numpy, scipy e lightfm

import numpy as np 
from lightfm.datasets import fetch_movielens
from lightfm import LightFM

dados = fetch_movielens(min_rating=4.0)

#Listando teste e treino dos dados

print(repr(dados['train']))
print(repr(dados['test']))


#Criando o model

# weighted approximate rank pairwise, ajuda a criar recomendaçõeos
model = LightFM(loss='warp') 

# Treinando os modelos

model.fit(dados['train'], epochs=30, num_threads=2)

#Função de recomendação

def recomendacao(model, dados, user_ids):

    n_users, n_items = dados['train'].shape

    # Gerar recomendação de acordo com cada usuário inserido

    for user_id in user_ids:
        positivos = dados['item_labels'][dados['train'].tocsr()[user_id].indices]

        pontuacao = model.predict(user_id, np.arange(n_items))

        top_itens = dados['item_labels'][np.argsort(-pontuacao)]

        print(u"Usuário %s" % user_id)
        print("  positivos:")

        for x in positivos[:3]:
            print("     %s" % x)
        
        print("     Recomendados:")
        for x in top_itens[:3]:
            print("     %s" % x)


recomendacao(model, dados, [3,25,450])
