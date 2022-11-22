CREATE DATABASE cadastro;

--criando tabela 
CREATE TABLE pessoas(
    id int NOT NULL AUTO_INCREMENT,
    nome VARCHAR(30) not null,
    nascimentos date,
    sexo enum('M','F'),
    peso decimal(5,2),
    altura decimal(3,2),
    nacionalidade VARCHAR(20) DEFAULT 'Brasil',
    PRIMARY KEY (id) --evita duplicidade de variaveis
);

