-- -----------------------------------------------------
-- Schema rutinas
-- -----------------------------------------------------
DROP DATABASE IF EXISTS rutinas;
CREATE DATABASE IF NOT EXISTS rutinas;
USE rutinas ;

-- -----------------------------------------------------
-- Table tipo_ejercicio
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS tipo_ejercicio (
  ID_TIPO_EJERCICIO SMALLINT(6) NOT NULL,
  DSC_TIPO_EJERCICIO VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (ID_TIPO_EJERCICIO))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table ejercicio
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ejercicio (
  ID_EJERCICIO INT(11) NOT NULL,
  ID_TIPO_EJERCICIO SMALLINT(6) NULL DEFAULT NULL,
  NOMBRE_EJERCICIO VARCHAR(50) NULL DEFAULT NULL,
  DSC_EJERCICIO VARCHAR(200) NULL DEFAULT NULL,
  PRIMARY KEY (ID_EJERCICIO),
  CONSTRAINT ejercicio_ibfk_1
    FOREIGN KEY (ID_TIPO_EJERCICIO)
    REFERENCES tipo_ejercicio (ID_TIPO_EJERCICIO))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table especialista
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS especialista (
  ID_ESPECIALISTA INT(11) NOT NULL,
  NOMBRE VARCHAR(50) NOT NULL,
  FECHA_NACIMIENTO DATE NOT NULL,
  TARJETA_PROFESIONAL VARCHAR(12) NOT NULL,
  PRIMARY KEY (ID_ESPECIALISTA))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table grupo_deportivo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS grupo_deportivo (
  CSC_INTENTOS INT(11) NOT NULL,
  ID_ESPECIALISTA INT(11) NOT NULL,
  ESP_ID_ESPECIALISTA INT(11) NOT NULL,
  INTENTO INT(11) NOT NULL,
  PRIMARY KEY (CSC_INTENTOS),
  CONSTRAINT grupo_deportivo_ibfk_1
    FOREIGN KEY (ID_ESPECIALISTA)
    REFERENCES especialista (ID_ESPECIALISTA),
  CONSTRAINT grupo_deportivo_ibfk_2
    FOREIGN KEY (ESP_ID_ESPECIALISTA)
    REFERENCES especialista (ID_ESPECIALISTA))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table parte_cuerpo
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS parte_cuerpo (
  ID_MUSCULO INT(11) NOT NULL,
  PAR_ID_MUSCULO INT(11) NULL DEFAULT NULL,
  DSC_MUSCULO VARCHAR(50) NOT NULL,
  PRIMARY KEY (ID_MUSCULO),
  CONSTRAINT parte_cuerpo_ibfk_1
    FOREIGN KEY (PAR_ID_MUSCULO)
    REFERENCES parte_cuerpo (ID_MUSCULO))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table musculo_ejercicio
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS musculo_ejercicio (
  ID_MUSCULO INT(11) NOT NULL,
  ID_EJERCICIO INT(11) NOT NULL,
  PRIMARY KEY (ID_MUSCULO, ID_EJERCICIO),
  CONSTRAINT musculo_ejercicio_ibfk_1
    FOREIGN KEY (ID_EJERCICIO)
    REFERENCES ejercicio (ID_EJERCICIO),
  CONSTRAINT musculo_ejercicio_ibfk_2
    FOREIGN KEY (ID_MUSCULO)
    REFERENCES parte_cuerpo (ID_MUSCULO))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table registro
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS registro (
  ID_REGISTRO INT(11) NOT NULL,
  FECHA_REGISTRO DATE NULL DEFAULT NULL,
  PRIMARY KEY (ID_REGISTRO),
  CONSTRAINT registro_ibfk_1
    FOREIGN KEY (ID_REGISTRO)
    REFERENCES especialista (ID_ESPECIALISTA))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table rutina
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS rutina (
  ID_ESPECIALISTA INT(11) NOT NULL,
  DIA VARCHAR(3) NOT NULL,
  ID_EJERCICIO INT(11) NOT NULL,
  REPETICIONES SMALLINT(6) NOT NULL,
  DURACION TIME NOT NULL,
  PRIMARY KEY (DIA, ID_EJERCICIO, ID_ESPECIALISTA),
  CONSTRAINT rutina_ibfk_1
    FOREIGN KEY (ID_EJERCICIO)
    REFERENCES ejercicio (ID_EJERCICIO),
  CONSTRAINT rutina_ibfk_2
    FOREIGN KEY (ID_ESPECIALISTA)
    REFERENCES especialista (ID_ESPECIALISTA))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;


-- -----------------------------------------------------
-- Table user
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS user (
  ID INT(11) NOT NULL,
  NAME VARCHAR(80) NOT NULL,
  EMAIL VARCHAR(256) NOT NULL,
  PASSWORD VARCHAR(128) NOT NULL,
  IS_ADMIN TINYINT(1) NULL DEFAULT NULL,
  PRIMARY KEY (ID),
  UNIQUE INDEX EMAIL (EMAIL ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;