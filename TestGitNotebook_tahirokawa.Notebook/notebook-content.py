# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "742d72d5-d442-4688-b842-9616721518fc",
# META       "default_lakehouse_name": "TestGitLakehouse_tahirokawa",
# META       "default_lakehouse_workspace_id": "48f23139-67df-4dfa-a8c8-b903a708847c",
# META       "known_lakehouses": [
# META         {
# META           "id": "742d72d5-d442-4688-b842-9616721518fc"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

print("Hello World")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM TestGitLakehouse_tahirokawa.factory_equipment_12months LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
