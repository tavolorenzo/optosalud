import sqlite3

FK_ON='PRAGMA foreing_keys=ON'

create_role_table='''
  CREATE TABLE role (
    roleId INTEGER PRIMARY KEY AUTOINCREMENT,
    description varchar(20) NOT NULL,
    access varchar(50) NOT NULL
    )'''
create_task_table='''
CREATE TABLE task (
    taskId INTEGER PRIMARY KEY AUTOINCREMENT,
    description varchar(20) NOT NULL
)'''

create_user_table='''
CREATE TABLE user (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    document varchar(20) UNIQUE NOT NULL,
    name varchar(20) NOT NULL,
    lastname varchar(20) NOT NULL,
    photoURI varchar(255),
    phone varchar(10) NOT NULL,
    jobPosition varchar(20)NOT NULL ,
    email varchar(50) NOT NULL,
    password varchar(255) NOT NULL ,
    status boolean DEFAULT TRUE
)'''

create_sector_table='''
CREATE TABLE sector (
    sectorId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(20) NOT NULL,
    photoURI varchar(255)
)'''

create_room_table='''
CREATE TABLE room (
    roomId INTEGER PRIMARY KEY AUTOINCREMENT,
    sectorId INTEGER NOT NULL REFERENCES sector(sectorId),
    name varchar(20) NOT NULL,
    UNIQUE(sectorId, name)
)'''
create_dailyRecord_table='''
CREATE TABLE dialyRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    bed varchar(5) NOT NULL,
    pacientDocument varchar(20) NOT NULL,
    pacientName varchar(20) NOT NULL,
    pacientLastName varchar(20) NOT NULL,
    comment varchar(500) NOT NULL
)'''
create_pharmacRecord_table='''
CREATE TABLE pharmacRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    isPrevision boolean DEFAULT FALSE
)'''

create_drug_table='''
CREATE TABLE drug (
    drugId INTEGER PRIMARY KEY AUTOINCREMENT,
    recordId INTEGER NOT NULL REFERENCES pharmacRecord(recordId),
    name varchar(50) NOT NULL,
    pharmaceuticalForm varchar(50) NOT NULL,
    quantity INTEGRER NOT NULL,
    unit varchar(10) NOT NULL,
    UNIQUE(recordId, name, pharmaceuticalForm)
)'''

create_materialRecord_table='''
CREATE TABLE materialRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    createdDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    isPrevision boolean DEFAULT FALSE
)'''

create_material_table='''
CREATE TABLE material (
    materialId INTEGER PRIMARY KEY AUTOINCREMENT,
    recordId INTEGER NOT NULL REFERENCES materialRecord(recordId),
    name varchar(50) NOT NULL,
    comment varchar(50) NOT NULL,
    quantity INTEGRER NOT NULL,
    units varchar(10) NOT NULL,
    UNIQUE(recordId, name, comment)
)'''


FK_user_role='''
ALTER TABLE user ADD roleId INTEGER NOT NULL REFERENCES role(roleId)'''

FK_role_task='''
ALTER TABLE task ADD roleId INTEGER NOT NULL REFERENCES role(roleId)'''

FK_pharmacRecord_user='''
  ALTER TABLE pharmacRecord ADD nurseId INTEGER NOT NULL REFERENCES user(userId)'''

FK2_pharmacRecord_user='''
  ALTER TABLE pharmacRecord ADD auxNurseId INTEGER NOT NULL REFERENCES user(userId)'''

FK_pharmacRecord_sector='''
  ALTER TABLE pharmacRecord ADD sectorId INTEGER NOT NULL REFERENCES sector(sectorId)'''

FK_pharmacRecord_room='''
  ALTER TABLE pharmacRecord ADD roomId INTEGER NOT NULL REFERENCES room(roomId)'''

FK_materialRecord_user='''
  ALTER TABLE materialRecord ADD nurseId INTEGER NOT NULL REFERENCES user(userId)'''

FK2_materialRecord_user='''
  ALTER TABLE materialRecord ADD auxNurseId INTEGER NOT NULL REFERENCES user(userId)'''

FK_materialRecord_sector='''
  ALTER TABLE materialRecord ADD sectorId INTEGER NOT NULL REFERENCES sector(sectorId)'''

FK_dailyRecord_user='''
  ALTER TABLE dialyRecord  ADD nurseId INTEGER NOT NULL REFERENCES user(userId)'''

FK2_dailyRecord_user='''
  ALTER TABLE dialyRecord  ADD auxNurseId INTEGER NOT NULL REFERENCES user(userId)'''

FK_dailyRecord_sector='''
  ALTER TABLE dialyRecord  ADD sectorId INTEGER NOT NULL REFERENCES sector(sectorId)'''

FK_dailyRecord_room='''
  ALTER TABLE dialyRecord ADD roomId INTEGER NOT NULL REFERENCES room(roomId)'''

IX_room_sector='''
  CREATE INDEX room_sectorId_index ON room(sectorId)
'''
IX_dialyRecord_createdDate='''
  CREATE INDEX dialyRecord_createdDate_index ON dialyRecord(createdDate)
'''
IX_pharmacRecord_createdDate='''
  CREATE INDEX pharmacRecord_createdDate_index ON pharmacRecord(createdDate)
'''
IX_materialRecord_createdDate='''
  CREATE INDEX materialRecord_createdDate_index ON materialRecord(createdDate)
'''

if __name__ == '__main__':
    try:
        print('Creando Base de datos..')
        conexion = sqlite3.connect('../../optosalud.db')
        conexion.execute(FK_ON)

        print('Creando Tablas..')
        conexion.execute(create_role_table)
        conexion.execute(create_task_table)
        conexion.execute(create_user_table)
        conexion.execute(create_sector_table)
        conexion.execute(create_room_table)
        conexion.execute(create_dailyRecord_table)
        conexion.execute(create_drug_table)
        conexion.execute(create_pharmacRecord_table)
        conexion.execute(create_material_table)
        conexion.execute(create_materialRecord_table)

        print('Creando claves foranes..')
        conexion.execute(FK_role_task)
        conexion.execute(FK_user_role)
        conexion.execute(FK_dailyRecord_user)
        conexion.execute(FK2_dailyRecord_user)
        conexion.execute(FK_dailyRecord_sector)
        conexion.execute(FK_dailyRecord_room)
        conexion.execute(FK_materialRecord_user)
        conexion.execute(FK2_materialRecord_user)
        conexion.execute(FK_materialRecord_sector)
        conexion.execute(FK_pharmacRecord_user)
        conexion.execute(FK2_pharmacRecord_user)
        conexion.execute(FK_pharmacRecord_sector)
        conexion.execute(FK_pharmacRecord_room)
        
        print('Optimizando base de datos..')
        conexion.execute(IX_room_sector)
        conexion.execute(IX_dialyRecord_createdDate)
        conexion.execute(IX_pharmacRecord_createdDate)
        conexion.execute(IX_materialRecord_createdDate)

        conexion.close()
        print('Creacion Finalizada.')
    except Exception as e:
        conexion.close()
        print(f'Error creando base de datos: {e}', e)
        print("Conexion cerrada exitosamente.")