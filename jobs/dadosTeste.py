# Imports
from pyspark.sql import SparkSession
import os
# Cria uma sessão Spark
spark = SparkSession.builder \
    .appName("Ingestão de Dados para teste de Log") \
    .getOrCreate()

# Configura o nível de log
spark.sparkContext.setLogLevel('ERROR')

# Carrega o conjunto de dados no formato CSV
dfTeste = spark.read.option("delimiter", ";").csv('./data/dadosTeste.csv', header = True, inferSchema = True)

# Mostra as primeiras linhas do DataFrame
dfTeste.show()

dfTeste.count()


# dfSize = SizeEstimator.estimate(someDF)
# print(f"Estimated size of the dataFrame weatherDF = {dfSize/1000000} mb")
# Salvar o resultado em um arquivo CSV
dfTeste.write.format("parquet")\
                .mode("overwrite")\
                .save("dataTeste.parquet")

file_stats = os.stat("dataTeste.parquet")
print(file_stats.st_size)
# Encerrar a sessão Spark
spark.stop()
