-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mypets_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mypets_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mypets_schema` DEFAULT CHARACTER SET utf8 ;
USE `mypets_schema` ;

-- -----------------------------------------------------
-- Table `mypets_schema`.`budget`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`budget` (
  `id` INT NOT NULL,
  `food` DECIMAL(16,2) NULL,
  `medications` DECIMAL(16,2) NULL,
  `essentials` DECIMAL(16,2) NULL,
  `pet_rent` DECIMAL(16,2) NULL,
  `yearly_exams` DECIMAL(16,2) NULL,
  `license` DECIMAL(16,2) NULL,
  `misc` DECIMAL(16,2) NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mypets_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `password` CHAR(60) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `pet_id` INT NOT NULL,
  `reminder_id` INT NOT NULL,
  `budget_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_budget1_idx` (`budget_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_budget1`
    FOREIGN KEY (`budget_id`)
    REFERENCES `mypets_schema`.`budget` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mypets_schema`.`diet`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`diet` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mypets_schema`.`species`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`species` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mypets_schema`.`breeds`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`breeds` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mypets_schema`.`pets`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`pets` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `dob` DATE NULL,
  `weight` DECIMAL(5,2) NULL,
  `on_meds` TINYINT(1) NULL,
  `users_id` INT NOT NULL,
  `diet_id` INT NOT NULL,
  `species_id` INT NOT NULL,
  `breeds_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pets_users_idx` (`users_id` ASC) VISIBLE,
  INDEX `fk_pets_diet1_idx` (`diet_id` ASC) VISIBLE,
  INDEX `fk_pets_species1_idx` (`species_id` ASC) VISIBLE,
  INDEX `fk_pets_breeds1_idx` (`breeds_id` ASC) VISIBLE,
  CONSTRAINT `fk_pets_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `mypets_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pets_diet1`
    FOREIGN KEY (`diet_id`)
    REFERENCES `mypets_schema`.`diet` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pets_species1`
    FOREIGN KEY (`species_id`)
    REFERENCES `mypets_schema`.`species` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pets_breeds1`
    FOREIGN KEY (`breeds_id`)
    REFERENCES `mypets_schema`.`breeds` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mypets_schema`.`reminders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mypets_schema`.`reminders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `reminder` VARCHAR(255) NULL,
  `pet_id` INT NOT NULL,
  `users_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_reminders_users1_idx` (`users_id` ASC) VISIBLE,
  CONSTRAINT `fk_reminders_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `mypets_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
