# -*- coding: utf-8 -*-
"""Média de uma variável.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wSQU_HCkhUD_NekB9XzZ50dDs5trl9MY
"""

import pandas as pd
dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})
dataset.Idade.mean()

#Agrupado por Sexo
dataset.groupby(['Sexo'])['Idade'].mean()

#Usando loc para média de idade dos homens
dataset.groupby('Sexo').mean().loc['H']

