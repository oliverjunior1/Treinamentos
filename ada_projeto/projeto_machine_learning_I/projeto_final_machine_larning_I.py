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

from  sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, roc_auc_score, classification_report

# =========================
# 2) CARREGAR DATASET (mínimo 1000 linhas considerando treino + teste Kaggle)
# =========================
df = pd.read_csv("train.csv")

# =========================
# 3) DEFINIÇÃO DO PROBLEMA
# Quero prever a variável "Survived"
# =========================

# =========================
# 4) TRATAMENTO DOS DADOS COM PANDAS
# =========================

# Remover colunas irrelevantes para o modelo
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

# Preencher valores nulos numéricos com mediana
df["Age"] = df["Age"].fillna(df["Age"].median())

# Preencher valores nulos categóricos com moda
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Criar Feature Engineering (tamanho da família)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# =========================
# 5) SEPARAÇÃO DE VARIÁVEIS
# =========================
X = df.drop("Survived", axis=1)
y = df["Survived"]

# =========================
# 6) DEFINIR COLUNAS NUMÉRICAS E CATEGÓRICAS
# =========================
num_cols = ["Age", "SibSp", "Parch", "Fare", "FamilySize"]
cat_cols = ["Pclass", "Sex", "Embarked"]

# =========================
# 7) PIPELINE DE PRÉ-PROCESSAMENTO
# =========================
numeric_transformer = Pipeline(steps=[
    ("scaler", StandardScaler())  # Normalização
])

categorical_transformer = Pipeline(steps=[
    ("encoder", OneHotEncoder(handle_unknown="ignore"))  # One-hot encoding
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
# 9) MÉTRICA DE AVALIAÇÃO
# Escolhida: ROC-AUC (boa para classificação binária)
# =========================

# =========================
# 10) MODELO 1 - Logistic Regression
# =========================
pipe_lr = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=1000))
])

pipe_lr.fit(X_train, y_train)

y_pred_lr = pipe_lr.predict(X_test)
y_prob_lr = pipe_lr.predict_proba(X_test)[:, 1]

print("=== Logistic Regression ===")
print("Accuracy:", accuracy_score(y_test, y_pred_lr))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_lr))
print(classification_report(y_test, y_pred_lr))

# =========================
# 11) OTIMIZAÇÃO DE HIPERPARÂMETROS - Logistic Regression
# =========================
param_grid_lr = {
    "classifier__C": [0.01, 0.1, 1, 10],
    "classifier__solver": ["lbfgs"]
}

grid_lr = GridSearchCV(pipe_lr, param_grid_lr, cv=5, scoring="roc_auc")
grid_lr.fit(X_train, y_train)

print("Melhores parâmetros LR:", grid_lr.best_params_)

# =========================
# 12) MODELO 2 - Random Forest
# =========================
pipe_rf = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])

pipe_rf.fit(X_train, y_train)

y_pred_rf = pipe_rf.predict(X_test)
y_prob_rf = pipe_rf.predict_proba(X_test)[:, 1]

print("=== Random Forest ===")
print("Accuracy:", accuracy_score(y_test, y_pred_rf))
print("ROC-AUC:", roc_auc_score(y_test, y_prob_rf))
print(classification_report(y_test, y_pred_rf))

# =========================
# 13) OTIMIZAÇÃO DE HIPERPARÂMETROS - Random Forest
# =========================
param_grid_rf = {
    "classifier__n_estimators": [100, 200],
    "classifier__max_depth": [None, 5, 10],
    "classifier__min_samples_split": [2, 5]
}

grid_rf = GridSearchCV(pipe_rf, param_grid_rf, cv=5, scoring="roc_auc")
grid_rf.fit(X_train, y_train)

print("Melhores parâmetros RF:", grid_rf.best_params_)

# =========================
# 14) COMPARAÇÃO FINAL DOS MODELOS
# =========================
best_lr = grid_lr.best_estimator_
best_rf = grid_rf.best_estimator_

y_prob_best_lr = best_lr.predict_proba(X_test)[:, 1]
y_prob_best_rf = best_rf.predict_proba(X_test)[:, 1]

roc_lr = roc_auc_score(y_test, y_prob_best_lr)
roc_rf = roc_auc_score(y_test, y_prob_best_rf)

print("ROC-AUC Final LR:", roc_lr)
print("ROC-AUC Final RF:", roc_rf)

# Escolher o melhor modelo
if roc_rf > roc_lr:
    print("Melhor modelo: Random Forest")
    best_model = best_rf
else:
    print("Melhor modelo: Logistic Regression")
    best_model = best_lr

# =========================
# 15) RESPOSTAS FINAIS
# =========================

# O modelo resolve o problema?
# Sim, pois apresenta boa capacidade preditiva medida pelo ROC-AUC.

# Pode ser colocado em produção?
# Sim, porém:
# - Deve haver monitoramento de performance
# - Re-treinamento periódico
# - Monitoramento de data drift
# - Deploy via API (Flask ou FastAPI)