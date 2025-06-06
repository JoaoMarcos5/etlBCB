import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv, salvarSQLite, salvarMySql

dadosBcb = requestApiBcb('20191')

#salvarCsv(dadosBcb, "etlBCB/src/datasets/meiosPagamentosTri.csv", ";", ".")

salvarSQLite(dadosBcb, "etlBCB/src/datasets/ETLbcb.db", "meios_pagamentos_tri")

#salvarMySql(dadosBcb, "root", "teste", "localhost", "etlbcb", "meios_pagamentos_tri")

# Gerar conexão com banco de dados db em um jupyter