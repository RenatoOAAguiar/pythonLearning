from sklearn import tree

#altura, peso e tamanho do pé

X = [[181, 80, 40], [170, 95, 41], [160, 60, 38], [158, 58, 37], [190, 105, 47]]

Y = ['homem', 'homem', 'mulher', 'mulher', 'homem']


decisoes = tree.DecisionTreeClassifier()
decisoes = tree.fit(X, Y)

predicao = decisoes.predict([190,90,46])

print(predicao)