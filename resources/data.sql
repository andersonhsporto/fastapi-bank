CREATE TABLE IF NOT EXISTS conta
(
    id_conta BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome_responsavel VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS transferencia
(
    id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    data_transferencia TIMESTAMP NOT NULL,
    valor NUMERIC (20,2) NOT NULL,
    tipo VARCHAR(15) NOT NULL,
    nome_operador_transacao VARCHAR (50),
    conta_id BIGINT NOT NULL,

    CONSTRAINT fk_conta_id FOREIGN KEY (conta_id) REFERENCES conta (id_conta)
);

INSERT IGNORE INTO conta (id_conta, nome_responsavel)
VALUES (1, 'Fulano');

INSERT IGNORE INTO conta (id_conta, nome_responsavel)
VALUES (2, 'Sicrano');

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (1, '2019-01-01 12:00:00', 30895.46, 'DEPOSITO', null, 1);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (2, '2019-02-03 09:53:27', 12.24, 'DEPOSITO', null, 2);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (3, '2019-05-04 08:12:45', -500.50, 'SAQUE', null, 1);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (4, '2019-08-07 08:12:45', -530.50, 'SAQUE', null, 2);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (5, '2020-06-08 10:15:01', 3241.23, 'TRANSFERENCIA', 'Beltrano', 1);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (6, '2021-04-01 12:12:04', 25173.09, 'TRANSFERENCIA', 'Ronnyscley', 2);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (7, '2021-04-01 12:12:04', 42.00, 'TRANSFERENCIA', 'Beltrano', 2);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (8, '2021-04-01 12:12:04', -42.00, 'TRANSFERENCIA', 'Beltrano', 2);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (9, '2021-04-01 12:12:04', -128.00, 'TRANSFERENCIA', 'Beltrano', 2);

INSERT IGNORE INTO transferencia (id, data_transferencia, valor, tipo, nome_operador_transacao, conta_id)
VALUES (10, '2022-12-22 12:12:04', -42.00, 'TRANSFERENCIA', 'Anderson', 2);