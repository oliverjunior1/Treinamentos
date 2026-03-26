# ============================================================
# PROJETO FINAL - MACHINE LEARNING I (VERSÃO AVANÇADA)
# Dataset: Titanic (Kaggle)
# Problema: Prever sobrevivência de passageiros
# Tipo: Classificação Binária
# Métrica principal: ROC-AUC
# ============================================================

# =========================
# 1) IMPORTAÇÃO DE BIBLIOTECAS
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    classification_report,
    roc_curve,
    confusion_matrix
)

# =========================
# 2) CARREGAMENTO DOS DADOS
# =========================
df = pd.read_csv("train.csv")

# =========================
# 3) PROBLEMA DE NEGÓCIO
# Prever a probabilidade de sobrevivência
# =========================

# =========================
# 4) TRATAMENTO E FEATURE ENGINEERING
# =========================

# Remover colunas irrelevantes
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Preencher valores nulos
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Feature Engineering avançado
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# =========================
# 5) SEPARAÇÃO DE VARIÁVEIS
# =========================
X = df.drop("Survived", axis=1)
y = df["Survived"]

# =========================
# 6) DEFINIÇÃO DAS COLUNAS
# =========================
num_cols = ["Age", "SibSp", "Parch", "Fare", "FamilySize"]
cat_cols = ["Pclass", "Sex", "Embarked", "IsAlone"]

# =========================
# 7) PIPELINE DE PRÉ-PROCESSAMENTO
# =========================
numeric_transformer = Pipeline([
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, num_cols),
    ("cat", categorical_transformer, cat_cols)
])

# =========================
# 8) DIVISÃO TREINO / TESTE
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 9) MODELO 1 - Logistic Regression
# =========================
pipe_lr = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

# Validação cruzada
cv_lr = cross_val_score(pipe_lr, X_train, y_train, cv=5, scoring="roc_auc")
print("ROC-AUC CV Logistic Regression:", cv_lr.mean())

# Treinamento final
pipe_lr.fit(X_train, y_train)
y_prob_lr = pipe_lr.predict_proba(X_test)[:, 1]

# =========================
# 10) MODELO 2 - Random Forest
# =========================
pipe_rf = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

# Validação cruzada
cv_rf = cross_val_score(pipe_rf, X_train, y_train, cv=5, scoring="roc_auc")
print("ROC-AUC CV Random Forest:", cv_rf.mean())

# =========================
# 11) OTIMIZAÇÃO DE HIPERPARÂMETROS
# =========================
param_grid_rf = {
    "classifier__n_estimators": [100, 200],
    "classifier__max_depth": [None, 5, 10],
    "classifier__min_samples_split": [2, 5]
}

grid_rf = GridSearchCV(pipe_rf, param_grid_rf, cv=5, scoring="roc_auc")
grid_rf.fit(X_train, y_train)

best_rf = grid_rf.best_estimator_

# =========================
# 12) AVALIAÇÃO FINAL
# =========================
y_pred = best_rf.predict(X_test)
y_prob = best_rf.predict_proba(X_test)[:, 1]

print("=== MODELO FINAL ===")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))
print(classification_report(y_test, y_pred))

# =========================
# 13) MATRIZ DE CONFUSÃO (VISUAL)
# =========================
cm = confusion_matrix(y_test, y_pred)

plt.figure()
plt.imshow(cm)
plt.title("Matriz de Confusão")
plt.xlabel("Predito")
plt.ylabel("Real")

for i in range(len(cm)):
    for j in range(len(cm)):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.show()

# =========================
# 14) CURVA ROC (GRÁFICO PRINCIPAL)
# =========================
fpr, tpr, _ = roc_curve(y_test, y_prob)

plt.figure()
plt.plot(fpr, tpr, label="Random Forest (Final)")
plt.plot([0, 1], [0, 1], linestyle="--")

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Curva ROC")
plt.legend()
plt.show()

# =========================
# 15) IMPORTÂNCIA DAS VARIÁVEIS
# =========================
feature_names = (
    num_cols +
    list(best_rf.named_steps["preprocessor"]
         .named_transformers_["cat"]
         .named_steps["encoder"]
         .get_feature_names_out(cat_cols))
)

importances = best_rf.named_steps["classifier"].feature_importances_

# Ordenar
indices = np.argsort(importances)[-10:]

plt.figure()
plt.barh(range(len(indices)), importances[indices])
plt.yticks(range(len(indices)), [feature_names[i] for i in indices])
plt.title("Top 10 Features Mais Importantes")
plt.show()

# =========================
# 16) CONCLUSÕES (RESPONDER PROFESSOR)
# =========================

# O modelo resolve o problema?
# Sim. O modelo apresenta boa performance (ROC-AUC alto),
# indicando boa capacidade de distinguir sobreviventes.

# Pode ir para produção?
# Sim, porém:
# - Necessário monitoramento contínuo (data drift)
# - Re-treinamento periódico
# - Deploy via API (FastAPI ou Flask)
# - Monitoramento de métricas em produção

# Diferencial do projeto:
# - Uso de Pipeline
# - Feature Engineering
# - Validação cruzada
# - Otimização de hiperparâmetros
# - Análise visual (ROC + Matriz de Confusão)