CREATE TABLE User (
  UserId int NOT NULL AUTO_INCREMENT,
  FirstName varchar(255) NOT NULL,
  LastName varchar(255) NOT NULL,
  Password varchar(255) NOT NULL,
  IdentityNumber char(11) NOT NULL,
  PRIMARY KEY (UserId),
  UNIQUE (IdentityNumber)
);

CREATE TABLE Account (
  AccountId int NOT NULL AUTO_INCREMENT,
  AccountName varchar(255) NOT NULL,
  CurrencyType varchar(5) NOT NULL,
  Balance double NOT NULL DEFAULT '0',
  UserId int NOT NULL,
  PRIMARY KEY (AccountId),
  FOREIGN KEY (UserId) REFERENCES user (UserId)
);

alter table Account auto_increment=1000000;

CREATE TABLE Transaction (
  TransactionId int NOT NULL AUTO_INCREMENT,
  SenderAccountId int NOT NULL,
  ReceiverAccountId int NOT NULL,
  TransactionDate datetime NOT NULL,
  Amount double NOT NULL,
  CurrencyType varchar(5) NOT NULL,
  PRIMARY KEY (TransactionId),
  FOREIGN KEY (SenderAccountId) REFERENCES Account (AccountId),
  FOREIGN KEY (ReceiverAccountId) REFERENCES Account (AccountId)
);