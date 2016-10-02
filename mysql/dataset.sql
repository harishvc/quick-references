/* SOURCE: https://dwbi.org/database/sql/72-top-20-sql-interview-questions-with-answers */

/* CREATE TABLE FOR DEPARTMENT */


/*
drop table if exists DEPARTMENT;
CREATE TABLE DEPARTMENT 
(
ID INT NOT NULL PRIMARY KEY, 
NAME VARCHAR(30)   
); 



/* CREATE TABLE FOR EMP */


drop table if exists EMP;
CREATE TABLE EMP
(
ID INT NOT NULL PRIMARY KEY, 
MGR_ID INT NOT NULL,
DEPT_ID INT NOT NULL, 
NAME VARCHAR(30), 
SAL INT NOT NULL, 
DOJ DATE, 
FOREIGN KEY (MGR_ID) REFERENCES EMP (ID), 
FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT (ID)
); 

*/


/* INSERT STATEMENT FOR DEPARTMENT */


INSERT INTO DEPARTMENT  values (1,'HR');
INSERT INTO DEPARTMENT  values (2,'Engineering');
INSERT INTO DEPARTMENT  values (3,'Marketing');
INSERT INTO DEPARTMENT  values (4,'Sales');
INSERT INTO DEPARTMENT  values (5,'Logistics');



/* INSERT STATEMENT FOR EMP */
INSERT INTO EMP  values (1, 1,  2,'Hash', 100, '2012-01-01');
INSERT INTO EMP  values (2, 1, 2, 'Robo', 100, '2012-01-01');
INSERT INTO EMP  values (3, 2, 1, 'Privy', 50, '2012-05-01');
INSERT INTO EMP  values (4, 1, 1, 'Inno', 50, '2012-05-01');
INSERT INTO EMP  values (5, 2, 2, 'Anno', 80, '2012-02-01');
INSERT INTO EMP  values (6, 1, 2, 'Darl', 80, '2012-02-11');
INSERT INTO EMP  values (7, 1, 3, 'Pete', 70, '2012-04-16');
INSERT INTO EMP  values (8, 7, 3, 'Meme', 60, '2012-07-26');
INSERT INTO EMP  values (9, 2, 4, 'Tomiti', 70, '2012-07-07');
INSERT INTO EMP  values (10, 9, 4, 'Bhuti', 60, '2012-08-24');
*/
