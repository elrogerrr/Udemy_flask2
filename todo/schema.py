instructions = [
    
    'SET GLOBAL foreign_key_checks=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET GLOBAL foreign_key_checks=1;',
    """
        CREATE TABLE `rogerdb`.`user` (`id` INT NOT NULL AUTO_INCREMENT , 
        `username` VARCHAR(50) NOT NULL , 
        `password` VARCHAR(80) NOT NULL , PRIMARY KEY (`id`), 
        UNIQUE `i_user` (`username`(20))) ENGINE = InnoDB;
    """
    
]