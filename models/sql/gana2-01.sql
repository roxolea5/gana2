-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.7.31-log - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for rancho_dev
DROP DATABASE IF EXISTS `rancho_dev`;
CREATE DATABASE IF NOT EXISTS `rancho_dev` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_spanish_ci */;
USE `rancho_dev`;

-- Dumping structure for table rancho_dev.adm_personas
DROP TABLE IF EXISTS `adm_personas`;
CREATE TABLE IF NOT EXISTS `adm_personas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_persona` tinyint(1) DEFAULT NULL,
  `curp` varchar(18) COLLATE utf8_spanish_ci DEFAULT NULL,
  `rfc` varchar(25) COLLATE utf8_spanish_ci DEFAULT NULL,
  `nombre` varchar(75) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellido_paterno` varchar(150) COLLATE utf8_spanish_ci DEFAULT NULL,
  `apellido_materno` varchar(150) COLLATE utf8_spanish_ci DEFAULT NULL,
  `direccion` text COLLATE utf8_spanish_ci,
  `estado_id` int(11) DEFAULT NULL,
  `municipio_id` int(11) DEFAULT NULL,
  `localidad_id` int(11) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  `usuario_creacion_id` int(11) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `adm_personas_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `cat_estados` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.adm_personas: ~0 rows (approximately)
/*!40000 ALTER TABLE `adm_personas` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_personas` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.adm_propietarios
DROP TABLE IF EXISTS `adm_propietarios`;
CREATE TABLE IF NOT EXISTS `adm_propietarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `correo_electronico` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  `identificador` varchar(250) COLLATE utf8_spanish_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.adm_propietarios: ~0 rows (approximately)
/*!40000 ALTER TABLE `adm_propietarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_propietarios` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.adm_roles
DROP TABLE IF EXISTS `adm_roles`;
CREATE TABLE IF NOT EXISTS `adm_roles` (
  `rol` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`rol`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.adm_roles: ~0 rows (approximately)
/*!40000 ALTER TABLE `adm_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_roles` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.adm_roles_usuario
DROP TABLE IF EXISTS `adm_roles_usuario`;
CREATE TABLE IF NOT EXISTS `adm_roles_usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `rol` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_modificacion_id` int(11) DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rol` (`rol`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `adm_roles_usuario_ibfk_1` FOREIGN KEY (`rol`) REFERENCES `adm_roles` (`rol`),
  CONSTRAINT `adm_roles_usuario_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `adm_usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.adm_roles_usuario: ~0 rows (approximately)
/*!40000 ALTER TABLE `adm_roles_usuario` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_roles_usuario` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.adm_usuarios
DROP TABLE IF EXISTS `adm_usuarios`;
CREATE TABLE IF NOT EXISTS `adm_usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `session_id` varchar(70) COLLATE utf8_spanish_ci DEFAULT NULL,
  `correo_electronico` varchar(255) COLLATE utf8_spanish_ci DEFAULT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `usuario_modificacion_id` int(11) DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `correo_electronico` (`correo_electronico`),
  UNIQUE KEY `username` (`username`),
  KEY `propietario_id` (`propietario_id`),
  CONSTRAINT `adm_usuarios_ibfk_1` FOREIGN KEY (`propietario_id`) REFERENCES `adm_propietarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.adm_usuarios: ~0 rows (approximately)
/*!40000 ALTER TABLE `adm_usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_usuarios` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.adm_usuario_persona
DROP TABLE IF EXISTS `adm_usuario_persona`;
CREATE TABLE IF NOT EXISTS `adm_usuario_persona` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `persona_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `persona_id` (`persona_id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `adm_usuario_persona_ibfk_1` FOREIGN KEY (`persona_id`) REFERENCES `adm_personas` (`id`),
  CONSTRAINT `adm_usuario_persona_ibfk_2` FOREIGN KEY (`usuario_id`) REFERENCES `adm_usuarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.adm_usuario_persona: ~0 rows (approximately)
/*!40000 ALTER TABLE `adm_usuario_persona` DISABLE KEYS */;
/*!40000 ALTER TABLE `adm_usuario_persona` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.alembic_version
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.alembic_version: ~1 rows (approximately)
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
REPLACE INTO `alembic_version` (`version_num`) VALUES
	('b3b66a6d5aad');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_colores
DROP TABLE IF EXISTS `cat_colores`;
CREATE TABLE IF NOT EXISTS `cat_colores` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_creacion_id` int(11) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_colores: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_colores` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_colores` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_destinos
DROP TABLE IF EXISTS `cat_destinos`;
CREATE TABLE IF NOT EXISTS `cat_destinos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_creacion_id` int(11) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_destinos: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_destinos` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_destinos` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_diagnosticos_palpado
DROP TABLE IF EXISTS `cat_diagnosticos_palpado`;
CREATE TABLE IF NOT EXISTS `cat_diagnosticos_palpado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) COLLATE utf8_spanish_ci DEFAULT NULL,
  `activo` int(11) DEFAULT NULL,
  `es_valor_reservado` int(11) DEFAULT NULL,
  `usuario_creacion_id` varchar(45) COLLATE utf8_spanish_ci DEFAULT NULL,
  `fecha_creacion` int(11) DEFAULT NULL,
  `usuario_modificacion_id` int(11) DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_diagnosticos_palpado: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_diagnosticos_palpado` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_diagnosticos_palpado` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_estados
DROP TABLE IF EXISTS `cat_estados`;
CREATE TABLE IF NOT EXISTS `cat_estados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc_estado` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `pais_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `pais_id` (`pais_id`),
  CONSTRAINT `cat_estados_ibfk_1` FOREIGN KEY (`pais_id`) REFERENCES `cat_paises` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_estados: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_estados` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_estados` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_localidades
DROP TABLE IF EXISTS `cat_localidades`;
CREATE TABLE IF NOT EXISTS `cat_localidades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc_localidad` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `municipio_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `estado_id` (`estado_id`),
  KEY `municipio_id` (`municipio_id`),
  CONSTRAINT `cat_localidades_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `cat_estados` (`id`),
  CONSTRAINT `cat_localidades_ibfk_2` FOREIGN KEY (`municipio_id`) REFERENCES `cat_municipios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_localidades: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_localidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_localidades` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_lotes
DROP TABLE IF EXISTS `cat_lotes`;
CREATE TABLE IF NOT EXISTS `cat_lotes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rancho_id` int(11) NOT NULL,
  `potrero_id` int(11) NOT NULL,
  `nombre` varchar(75) COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_creacion_id` int(11) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `potrero_id` (`potrero_id`),
  KEY `rancho_id` (`rancho_id`),
  CONSTRAINT `cat_lotes_ibfk_1` FOREIGN KEY (`potrero_id`) REFERENCES `cat_potreros` (`id`),
  CONSTRAINT `cat_lotes_ibfk_2` FOREIGN KEY (`rancho_id`) REFERENCES `cat_ranchos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_lotes: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_lotes` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_lotes` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_municipios
DROP TABLE IF EXISTS `cat_municipios`;
CREATE TABLE IF NOT EXISTS `cat_municipios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `desc_municipio` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `estado_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `estado_id` (`estado_id`),
  CONSTRAINT `cat_municipios_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `cat_estados` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_municipios: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_municipios` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_municipios` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_paises
DROP TABLE IF EXISTS `cat_paises`;
CREATE TABLE IF NOT EXISTS `cat_paises` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(250) COLLATE utf8_spanish_ci NOT NULL,
  `abreviatura` varchar(5) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_paises: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_paises` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_paises` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_potreros
DROP TABLE IF EXISTS `cat_potreros`;
CREATE TABLE IF NOT EXISTS `cat_potreros` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `rancho_id` int(11) NOT NULL,
  `nombre` varchar(75) COLLATE utf8_spanish_ci DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_creacion_id` int(11) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `rancho_id` (`rancho_id`),
  CONSTRAINT `cat_potreros_ibfk_1` FOREIGN KEY (`rancho_id`) REFERENCES `cat_ranchos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_potreros: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_potreros` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_potreros` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_ranchos
DROP TABLE IF EXISTS `cat_ranchos`;
CREATE TABLE IF NOT EXISTS `cat_ranchos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `direccion` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `ciudad` varchar(50) COLLATE utf8_spanish_ci DEFAULT NULL,
  `telefono` varchar(12) COLLATE utf8_spanish_ci DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `municipio_id` int(11) DEFAULT NULL,
  `localidad_id` int(11) DEFAULT NULL,
  `pais_id` int(11) DEFAULT NULL,
  `rfc` varchar(18) COLLATE utf8_spanish_ci DEFAULT NULL,
  `email` varchar(75) COLLATE utf8_spanish_ci DEFAULT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  `como_llegar` text COLLATE utf8_spanish_ci NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_creacion_id` int(11) DEFAULT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `estado_id` (`estado_id`),
  KEY `localidad_id` (`localidad_id`),
  KEY `municipio_id` (`municipio_id`),
  KEY `pais_id` (`pais_id`),
  KEY `propietario_id` (`propietario_id`),
  CONSTRAINT `cat_ranchos_ibfk_1` FOREIGN KEY (`estado_id`) REFERENCES `cat_estados` (`id`),
  CONSTRAINT `cat_ranchos_ibfk_2` FOREIGN KEY (`localidad_id`) REFERENCES `cat_localidades` (`id`),
  CONSTRAINT `cat_ranchos_ibfk_3` FOREIGN KEY (`municipio_id`) REFERENCES `cat_municipios` (`id`),
  CONSTRAINT `cat_ranchos_ibfk_4` FOREIGN KEY (`pais_id`) REFERENCES `cat_paises` (`id`),
  CONSTRAINT `cat_ranchos_ibfk_5` FOREIGN KEY (`propietario_id`) REFERENCES `adm_propietarios` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_ranchos: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_ranchos` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_ranchos` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_razas
DROP TABLE IF EXISTS `cat_razas`;
CREATE TABLE IF NOT EXISTS `cat_razas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(75) COLLATE utf8_spanish_ci DEFAULT NULL,
  `activo` tinyint(1) NOT NULL,
  `usuario_creacion_id` int(11) NOT NULL,
  `fecha_creacion` datetime NOT NULL,
  `usuario_modificacion_id` int(11) NOT NULL,
  `fecha_modificacion` datetime NOT NULL,
  `propietario_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_razas: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_razas` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_razas` ENABLE KEYS */;

-- Dumping structure for table rancho_dev.cat_tipo_movimientos
DROP TABLE IF EXISTS `cat_tipo_movimientos`;
CREATE TABLE IF NOT EXISTS `cat_tipo_movimientos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) COLLATE utf8_spanish_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- Dumping data for table rancho_dev.cat_tipo_movimientos: ~0 rows (approximately)
/*!40000 ALTER TABLE `cat_tipo_movimientos` DISABLE KEYS */;
/*!40000 ALTER TABLE `cat_tipo_movimientos` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
