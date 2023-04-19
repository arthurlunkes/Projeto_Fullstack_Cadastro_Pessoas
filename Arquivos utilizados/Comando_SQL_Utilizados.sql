CREATE TABLE USER(
	ID_USER INTEGER NOT NULL,
	USER_NAME VARCHAR(60) NOT NULL,
	EMAIL VARCHAR(60) NOT NULL,
	CD_CIDADE INTEGER NOT NULL,
	CONSTRAINT PK_USER PRIMARY KEY(ID_USER)
	CONSTRAINT FK_CIDADE FOREIGN KEY(CD_CIDADE) REFERENCES CIDADE
);

CREATE TABLE CIDADE(
	ID_CIDADE INTEGER NOT NULL,
	NOME_CIDADE VARCHAR(60) NOT NULL,
	SG_UF VARCHAR(2) NOT NULL,
	CONSTRAINT PK_CIDADE PRIMARY KEY(ID_CIDADE)
);