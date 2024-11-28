use campeonatobrasileiro;

delete from estadio where id_estadio >= 1; -- apagar os registros da tabela
ALTER TABLE estadio AUTO_INCREMENT = 1; -- reiniciar o auto_increment

-- insert para unica linha
insert into estadio(nome, endereco, capacidade)
value('Maracanã','Av. Pres. Castelo Branco, Portão 3 - Maracanã, Rio de Janeiro - RJ',78838);

-- insert para multiplas linhas
insert into estadio(nome, endereco, capacidade) values
('Morumbi (Estádio Cícero Pompeu de Toledo)','Praça Roberto Gomes Pedrosa, 1 - Morumbi, São Paulo - SP','66795'),
('Mineirão (Estádio Governador Magalhães Pinto)','Av. Antônio Abrahão Caram, 1001 - Pampulha, Belo Horizonte - MG','61846'),
('Arena do Grêmio','Av. Padre Leopoldo Brentano, 110 - Humaitá, Porto Alegre - RS','55662'),
('Allianz Parque','Av. Francisco Matarazzo, 1705 - Água Branca, São Paulo - SP','43713'),
('Beira-Rio (Estádio José Pinheiro Borda)','Av. Padre Cacique, 891 - Praia de Belas, Porto Alegre - RS','50128'),
('Arena Fonte Nova','Ladeira da Fonte das Pedras - Nazaré, Salvador - BA','47907'),
('Arena Castelão (Estádio Governador Plácido Castelo)','Av. Alberto Craveiro, 2901 - Castelão, Fortaleza - CE','63903'),
('Neo Química Arena','Av. Miguel Ignácio Curi, 111 - Artur Alvim, São Paulo - SP','49205'),
('Estádio Nilton Santos (Engenhão)','R. José dos Reis, 425 - Engenho de Dentro, Rio de Janeiro - RJ','46831'),
('Arena da Baixada (Estádio Joaquim Américo)','R. Buenos Aires, 1260 - Água Verde, Curitiba - PR','42372'),
('Arena Pantanal','Av. Agrícola Paes de Barros - Verdão, Cuiabá - MT','44000'),
('Estádio Serra Dourada','Av. Fued José Sebba - Jardim Goiás, Goiânia - GO','50049'),
('Arena Pernambuco','Av. Deus é Fiel, 1 - São Lourenço da Mata, Recife - PE','44300'),
('Estádio Couto Pereira','R. Ubaldino do Amaral, 37 - Alto da Glória, Curitiba - PR','40502'),
('Vila Belmiro (Estádio Urbano Caldeira)','R. Princesa Isabel, 77 - Vila Belmiro, Santos - SP','16068'),
('Estádio São Januário','R. Gen. Almério de Moura, 131 - Vasco da Gama, Rio de Janeiro - RJ','21880'),
('Estádio Independência (Arena Independência)','R. Pitangui, 3230 - Horto, Belo Horizonte - MG','23018'),
('Arena da Amazônia','Av. Constantino Nery, 5001 - Flores, Manaus - AM','44310'),
('Estádio Mané Garrincha','SRPN - Asa Norte, Brasília - DF','72788');

select * from estadio;