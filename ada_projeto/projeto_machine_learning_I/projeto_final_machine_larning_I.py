# ============================================================
# PROJETO FINAL - MACHINE LEARNING I
# Dataset: Titanic (Kaggle)
# Problema de Negócio:
# Prever se um passageiro sobreviveria ao Titanic
# Tipo: Classificação Binária
# ============================================================

# =========================
# 1) IMPORTAÇÃO DE BIBLIOTECAS
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    roc_auc_score,
    classification_report,
    roc_curve
)

# =========================
# 2) CARREGAR DATASET
# =========================
df = pd.read_csv("train.csv")

# =========================
# 3) DEFINIÇÃO DO PROBLEMA
# Prever a variável "Survived"
# =========================

# =========================
# 4) TRATAMENTO DOS DADOS COM PANDAS
# =========================

# Remover colunas irrelevantes
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Preencher valores nulos
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Feature Engineering
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# =========================
# 5) SEPARAÇÃO DE VARIÁVEIS
# =========================
X = df.drop("Survived", axis=1)
y = df["Survived"]

# =========================
# 6) DEFINIR COLUNAS
# =========================
num_cols = ["Age", "SibSp", "Parch", "Fare", "FamilySize"]
cat_cols = ["Pclass", "Sex", "Embarked"]

# =========================
# 7) PIPELINE DE PRÉ-PROCESSAMENTO
# =========================
numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, num_cols),
        ("cat", categorical_transformer, cat_cols)
    ]
)

# =========================
# 8) DIVISÃO TREINO / TESTE
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# 9) MÉTRICA ESCOLHIDA
# ROC-AUC (classificação binária)
# =========================

# =========================
# 10) MODELO 1 - Logistic Regression
# =========================
pipe_lr = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

pipe_lr.fit(X_train, y_train)

y_prob_lr = pipe_lr.predict_proba(X_test)[:, 1]

roc_lr = roc_auc_score(y_test, y_prob_lr)

print("ROC-AUC Logistic Regression:", roc_lr)

# =========================
# 11) MODELO 2 - Random Forest
# =========================
pipe_rf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

pipe_rf.fit(X_train, y_train)

y_prob_rf = pipe_rf.predict_proba(X_test)[:, 1]

roc_rf = roc_auc_score(y_test, y_prob_rf)

print("ROC-AUC Random Forest:", roc_rf)

# =========================
# 12) OTIMIZAÇÃO DE HIPERPARÂMETROS - Random Forest
# =========================
param_grid_rf = {
    "classifier__n_estimators": [100, 200],
    "classifier__max_depth": [None, 5, 10]
}

grid_rf = GridSearchCV(pipe_rf, param_grid_rf, cv=5, scoring="roc_auc")
grid_rf.fit(X_train, y_train)

best_rf = grid_rf.best_estimator_
y_prob_best_rf = best_rf.predict_proba(X_test)[:, 1]

roc_best_rf = roc_auc_score(y_test, y_prob_best_rf)

print("ROC-AUC Random Forest Otimizado:", roc_best_rf)

# =========================
# 13) GRÁFICO CURVA ROC (Matplotlib)
# =========================

# Calcular curvas
fpr_lr, tpr_lr, _ = roc_curve(y_test, y_prob_lr)
fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_best_rf)

# Plot
plt.figure()
plt.plot(fpr_lr, tpr_lr, label="Logistic Regression")
plt.plot(fpr_rf, tpr_rf, label="Random Forest Otimizado")
plt.plot([0, 1], [0, 1], linestyle="--")  # linha aleatória

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("Curva ROC - Comparação de Modelos")
plt.legend()
plt.show()

# =========================
# 14) CONCLUSÃO
# =========================

# O modelo resolve o problema?
# Sim, pois o ROC-AUC indica boa capacidade de separação entre classes.

# Pode ir para produção?
# Sim, com monitoramento de performance e re-treinamento periódico.