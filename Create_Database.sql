CREATE DATABASE test_database_new;

CREATE TABLE test_database_new.contacts
(
    contactID int auto_increment,
    fName varchar(30) NOT NULL,
    lName varchar(30),
    mName varchar(30),
    workCompany varchar(50),
    mobile varchar(20),
    homePhone varchar(20),
    workPhone varchar(20),
    email varchar(50),
    jobTitle varchar(50),
    primary key (contactID)
);

SELECT * FROM TEST_DATABASE_new.CONTACTS;

DELETE FROM test_database_new.contacts WHERE contactID = 13;