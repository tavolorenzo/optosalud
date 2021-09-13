/*********************************************** 
TABLA ROLE
***********************************************/

CREATE TABLE role (
    roleId INTEGER PRIMARY KEY AUTOINCREMENT,
    description varchar(20) NOT NULL,
    access varchar(50) NOT NULL,
);

/*********************************************** 
TABLA TASK
***********************************************/

CREATE TABLE task (
    taskId INTEGER PRIMARY KEY AUTOINCREMENT,
    description varchar(20) NOT NULL,
);


/*********************************************** 
TABLA USER
***********************************************/

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
);

/*********************************************** 
TABLA SECTOR
***********************************************/

CREATE TABLE sector (
    sectorId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(20) NOT NULL,
    photoURI varchar(255),
);

/*********************************************** 
TABLA ROOM
***********************************************/

CREATE TABLE room (
    roomId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(20) NOT NULL,
);


/*********************************************** 
TABLA DIALY RECORD
***********************************************/

CREATE TABLE dialyRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    dateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    bed varchar(5) NOT NULL,
    pacientDocument varchar(20) NOT NULL,
    pacientName varchar(20) NOT NULL,
    pacientLastName varchar(20) NOT NULL,
    comment varchar(500) NOT NULL,
);


/*********************************************** 
TABLA DURG
***********************************************/

CREATE TABLE drug (
    drugId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(50) NOT NULL,
    pharmaceuticalForm varchar(50) NOT NULL,
    quantity INTEGRER NOT NULL,
    unit varchar(10) NOT NULL,
);

/*********************************************** 
TABLA PHARMAC RECORD
***********************************************/

CREATE TABLE pharmacRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    dateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    isPrevision boolean DEFAULT FALSE,
);


/*********************************************** 
TABLA MATERIAL
***********************************************/

CREATE TABLE material (
    materialId INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(50) NOT NULL,
    comment varchar(50) NOT NULL,
    quantity INTEGRER NOT NULL,
    units varchar(10) NOT NULL,
);

/*********************************************** 
TABLA MATERIAL RECORD
***********************************************/

CREATE TABLE materialRecord (
    recordId INTEGER PRIMARY KEY AUTOINCREMENT,
    dateAndTime DATETIME DEFAULT CURRENT_TIMESTAMP INDEX,
    isPrevision boolean DEFAULT FALSE,
);


/***********************************************
RELACION CADA USER DEBE TENER UN ROLE ASIGNADO
***********************************************/

ALTER TABLE user ADD roleId INTEGER NOT NULL
  REFERENCES role (roleId);
  
/***********************************************
RELACION CADA TASK TENER UN ROLE ASIGNADO
***********************************************/

ALTER TABLE task ADD roleId INTEGER NOT NULL
  REFERENCES role (roleId);

/***********************************************
RELACION CADA ROOM DEBE TENER UN SECTOR ASIGNADO
***********************************************/

ALTER TABLE room ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId);


/***********************************************
RELACIONES PHARMAC RECORD 
DRUG N:1 - USER (NURSE) N:1 - USER (AUX NURSE) N:1 - SECTOR N:1 - ROOM N:1 
***********************************************/

ALTER TABLE drug ADD recordId INTEGER NOT NULL
  REFERENCES pharmacRecord (recordId);

ALTER TABLE pharmacRecord ADD nurseId INTEGER NOT NULL
  REFERENCES user (userId);

ALTER TABLE pharmacRecord ADD auxNurseId INTEGER NOT NULL
  REFERENCES user (userId);

ALTER TABLE pharmacRecord ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId);

ALTER TABLE pharmacRecord ADD roomId INTEGER NOT NULL
  REFERENCES room (roomId);


/***********************************************
RELACIONES MATERIAL RECORD 
DRUG N:1 - USER (NURSE) N:1 - USER (AUX NURSE) N:1 - SECTOR N:1 
***********************************************/

ALTER TABLE material ADD recordId INTEGER NOT NULL
  REFERENCES materialRecord (recordId);

ALTER TABLE materialRecord ADD nurseId INTEGER NOT NULL
  REFERENCES user (userId);

ALTER TABLE materialRecord ADD auxNurseId INTEGER NOT NULL
  REFERENCES user (userId);

ALTER TABLE materialRecord ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId);


/***********************************************
RELACIONES DAILY RECORD 
SECTOR N:1- ROOM N:1 - USER (NURSE) N:1 - USER (AUX NURSE) N:1 
***********************************************/

ALTER TABLE dialyRecord  ADD nurseId INTEGER NOT NULL
  REFERENCES user (userId);

ALTER TABLE dialyRecord  ADD auxNurseId INTEGER NOT NULL
  REFERENCES user (userId);

ALTER TABLE dialyRecord  ADD sectorId INTEGER NOT NULL
  REFERENCES sector (sectorId);

  ALTER TABLE dialyRecord ADD roomId INTEGER NOT NULL
  REFERENCES room (roomId);
