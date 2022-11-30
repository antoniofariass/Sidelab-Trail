INSERT INTO pessoas --inserindo dados na tabela pessoas 
(id,nome, nascimento, sexo, peso,altura, nacionalidade);
VALUES
('1','Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil');

--ou 

INSERT INTO pessoas VALUES --caso os campos estejam na ordem que voce deseja adicionar
('1','Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil');

--cadastrar varios de uma vez
INSERT INTO pessoas VALUES 
('1','Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil'),
('1','Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil'),
('1','Godofredo', '1984-01-02', 'M', '78.5','1.83','Brasil');