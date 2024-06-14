DROP TABLE my_employee PURGE;

CREATE TABLE my_employee
(
ID           NUMBER(4) primary key,
LAST_NAME    VARCHAR2(25),
FIRST_NAME   VARCHAR2(25),
USERID       VARCHAR2(8),
SALARY       NUMBER(9,2)
);

