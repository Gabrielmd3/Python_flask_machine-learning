import numpy as np
from matplotlib import pyplot as plt

from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier

def machine_learning(cl,p1, p2, rs):
    # Coleta e Preparação de Dados.
    iris = load_iris()
    X = iris.data # caracteristica
    y = iris.target # rotulos

    # Divisão dos Dados em Treinamento e Teste.
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=int(rs))

    # Escolha do Algoritmo de Machine Learning.
    if cl == "mlp":
        clf = MLPClassifier(hidden_layer_sizes=(int(p1),), activation=(p2))
    elif cl == "rf":
        clf = RandomForestClassifier(n_estimators=int(p1), max_depth=int(p2))
    elif cl == "knn":
        clf = KNeighborsClassifier(n_neighbors=int(p1))
    elif cl == "dt":
        clf = DecisionTreeClassifier(criterion=(p1), max_depth=int(p2))



    # Treinamento do Modelo.
    clf.fit(X_train, y_train)

    # Teste / Previsão do Modelo.
    y_pred = clf.predict(X_test)

    f1 = f1_score(y_test, y_pred, average='weighted')
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred, average='weighted')
    precision = precision_score(y_test, y_pred, average='weighted')
    # Análise dos Resultados.
    cm = confusion_matrix(y_test, y_pred)

    classes = iris.target_names.tolist()
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)

    disp.plot()
    plt.savefig("static/displayimg")

    return accuracy, precision, recall, f1