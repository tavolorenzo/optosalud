import sqlite3
  create_role_table='''
  CREATE TABLE role (
    roleId INTEGER PRIMARY KEY AUTOINCREMENT,
    description varchar(20) NOT NULL,
    access varchar(50) NOT NULL,
)
'''
create_user_table='''
CREATE TABLE user (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    document varchar(20) UNIQUE INDEX NOT NULL,
    name varchar(20) NOT NULL,
    lastname varchar(20) NOT NULL,
    photoURI varchar(255),
    phone varchar(10) NOT NULL,
    jobPosition varchar(20)NOT NULL ,
    email varchar(50) NOT NULL,
    password varchar(255) NOT NULL ,
    status boolean DEFAULT TRUE,
)'''
create_sector_table='''
CREATE TABLE sector (
    sectorId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(20) NOT NULL,
    photoURI varchar(255),
)'''
create_room_table='''
CREATE TABLE room (
    roomId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(20) NOT NULL,
)'''
create_daily_table='''
CREATE TABLE dialyRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    dateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    bed varchar(5) NOT NULL,
    pacientDocument varchar(20) NOT NULL,
    pacientName varchar(20) NOT NULL,
    pacientLastName varchar(20) NOT NULL,
    comment varchar(500) NOT NULL,
)'''
create_drug_table='''
CREATE TABLE drug (
    drugId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(50) NOT NULL,
    pharmaceuticalForm varchar(50) NOT NULL,
    quantity INTEGRER NOT NULL,
    unit varchar(10) NOT NULL,
)'''
create_pharmac_table='''
CREATE TABLE pharmacRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    dateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    isPrevision boolean DEFAULT FALSE,
)'''
create_material_table='''
CREATE TABLE material (
    materialId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(50) NOT NULL,
    comment varchar(50) NOT NULL,
    quantity INTEGRER NOT NULL,
    units varchar(10) NOT NULL,
)'''
create_materialrecord_table='''
CREATE TABLE materialRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    dateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    isPrevision boolean DEFAULT FALSE,
)'''

alter_user_table='''
ALTER TABLE user ADD roleId INTEGER NOT NULL
  REFERENCES role (roleId)'''
alter_room_table='''
ALTER TABLE room ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId)'''
  alter_drug_table='''
  ALTER TABLE drug ADD recordId INTEGER NOT NULL
  REFERENCES pharmacRecord (recordId)'''
  alter_pharmac_table='''
  ALTER TABLE pharmacRecord ADD nurseId INTEGER NOT NULL
  REFERENCES user (userId)'''
  alter_pharmacrecord_table='''
  ALTER TABLE pharmacRecord ADD auxNurseId INTEGER NOT NULL
  REFERENCES user (userId)'''
  alter_pharmacrecord_add_sectorid_table='''
  ALTER TABLE pharmacRecord ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId)'''
  alter_pharmacrecord_add_roomid_table='''
  ALTER TABLE pharmacRecord ADD roomId INTEGER NOT NULL
  REFERENCES room (roomId)'''
  alter_material_table='''
  ALTER TABLE material ADD recordId INTEGER NOT NULL
  REFERENCES materialRecord (recordId)'''
  alter_materialrecord_add_nurseid_table='''
  ALTER TABLE materialRecord ADD nurseId INTEGER NOT NULL
  REFERENCES user (userId)'''
  alter_materialrecord_add_auxnurseid_table='''
  ALTER TABLE materialRecord ADD auxNurseId INTEGER NOT NULL
  REFERENCES user (userId)'''
  alter_materialrecord_add_sectorid_table='''
  ALTER TABLE materialRecord ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId)'''
  alter_dailyrecord_table='''
  ALTER TABLE dialyRecord  ADD nurseId INTEGER NOT NULL
  REFERENCES user (userId)'''
  alter_dilyrecord_add_auxnurseid_table='''
  ALTER TABLE dialyRecord  ADD auxNurseId INTEGER NOT NULL
  REFERENCES user (userId)'''
  alter_dailyrecord_add_sectorid_table='''
  ALTER TABLE dialyRecord  ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId)'''
  alter_dailyrecord_add_roomid_table='''
  ALTER TABLE dialyRecord ADD roomId INTEGER NOT NULL
  REFERENCES room (roomId)'''
  
  
  

  
  
  
  
  







