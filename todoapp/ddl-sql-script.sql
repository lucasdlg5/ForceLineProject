CREATE DATABASE Todo;
USE Todo;

CREATE TABLE tb_user (
	usr_id INT PRIMARY KEY AUTO_INCREMENT,
    usr_name VARCHAR(180) NOT NULL,
    usr_cpf VARCHAR(11) NOT NULL UNIQUE,
    usr_email VARCHAR(200) NOT NULL UNIQUE,
    usr_password VARCHAR(256) NOT NULL
);

CREATE TABLE tb_task (
	tsk_id INT PRIMARY KEY AUTO_INCREMENT,
    tsk_name VARCHAR(150),
    tsk_description VARCHAR(250),
    
    usr_id INT,
    
    FOREIGN KEY (usr_id) REFERENCES tb_user (usr_id)
);