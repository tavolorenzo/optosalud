from data.databases.conectDB import database as bd

def create_drug(recordId, name, pharmaceuticalForm, quantity, unit):
    sql_sentence = f"""
    INSERT INTO drug(recordId, name, pharmaceuticalForm, quantity, unit)
    VALUES ('{recordId}', '{name}', '{pharmaceuticalForm}', '{quantity}', '{unit}')
    """
    bd.run_sql(sql_sentence)