import pandas as pd
from src.extrectTransform import requestApiBcb
from src.load import salvarCsv, salvarSqlite, salvarMySql

dadosBcb = requestApiBcb("20191")
# salvarCsv(dadosBcb,'src/datasets/meiospagamentostri.csv', ";", ".")
# salvarSqlite(dadosBcb,"src/datasets/ETLBCB.db","meios_pagamentos_tri")

salvarMySql(dadosBcb, "root", "root", "localrost", "etlBCB", "meios_pagamentos_tri")
