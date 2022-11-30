ALTER TABLE pessoas
add column profissao VARCHAR(10) after nome; -- coloca a columa apos a coluna nome

ALTER TABLE pessoas
add column codigo int first; --coloca a coluna como a primeira 

ALTER TABLE pesssoas
MODIFY COLUMN profissao VARCHAR(20);

ALTER TABLE pessoas
change column profissao prof VARCHAR(20);

ALTER TABLE pessoas
ADD PRIMARY KEY(id);

DROP TABLE pessoas; --deletar toda a tabela 

