from data.databases.connectDB import database as bd

def create_material(recordId, name, comment, quantity, unit):
    sql_sentence = f"""
    INSERT INTO material(recordId, name, comment, quantity, unit)
    VALUES ('{recordId}', '{name}', '{comment}', '{quantity}', '{unit}')
    """
    bd.run_sql(sql_sentence)