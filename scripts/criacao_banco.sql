USE zoologico;

-- Script para criar a tabela 'especies'
CREATE TABLE especies (
    especie_id INT AUTO_INCREMENT PRIMARY KEY,
    nome_especie VARCHAR(50) NOT NULL,
    descricao VARCHAR(255),
    habitat VARCHAR(100),
    curiosidade VARCHAR(255),
    dieta VARCHAR(100),
    expectativa_vida_anos INT
);

-- Script para criar a tabela 'animais'
CREATE TABLE animais (
    animal_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    foto BLOB,
    especie_id INT,
    sexo CHAR(1),
    data_nascimento VARCHAR(10),
    FOREIGN KEY (especie_id) REFERENCES especies(especie_id)
);

-- Inserir uma espécie com ID auto-incrementado
INSERT INTO especies (nome_especie, descricao, habitat, curiosidade, dieta, expectativa_vida_anos)
VALUES ('Sapo', 'O leão é um grande felino conhecido por sua juba.', 'Savana', 'Os leões são os únicos felinos que vivem em grupos sociais chamados de "coalizões".', 'Carnívoro', 15);

INSERT INTO animais (nome, especie_id, sexo, data_nascimento)
values ( 'Matheus', 1, 'F', '08-03-2001' );
-- Exibir os registros da tabela especies
SELECT * FROM especies;


-- DELETE FROM animais WHERE animal_id IN (3, 4);

-- Exibir os registros da tabela animais
SELECT * FROM animais;
