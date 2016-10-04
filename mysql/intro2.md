#MySQL Introduction: Schema


##Data Integrity 
Data Integrity constraints are used to ensure accuracy and consistency of data in a relational
database.

* **Primary Key** is the term used to identify one or more columns in table that make a row of data unique. Primary Key is assigned during table creation.
* **Foreign Key** is a column that references a primary key in another table. A foreign Key constraint is the main mechanism used to enforce referential integrity  between tables in a relational database.
* **Database normalization**, or simply normalization, is the process of organizing the columns (attributes) and tables (relations) of a relational database to reduce data redundancy and improve data integrity. Key benefits include flexible database design, better handle on security and data consistency. There may be performance issues.
* **Denormalization** is the process of taking a normalized database and modifying the structure to add **controlled redundency** to improve performance.


##Schema
```
CREATE TABLE DEPARTMENT 
(
ID INT NOT NULL PRIMARY KEY, 
NAME VARCHAR(30)   
); 

mysql> describe department;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| ID    | int(11)     | NO   | PRI | NULL    |       |
| NAME  | varchar(30) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)

#
#
#

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

describe emp;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| ID      | int(11)     | NO   | PRI | NULL    |       |
| MGR_ID  | int(11)     | NO   | MUL | NULL    |       |
| DEPT_ID | int(11)     | NO   | MUL | NULL    |       |
| NAME    | varchar(30) | YES  |     | NULL    |       |
| SAL     | int(11)     | NO   |     | NULL    |       |
| DOJ     | date        | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
6 rows in set (0.00 sec)
```



##SQL Performance Tuning
* **Index** is a pointer to data in a table. Index is a database is similar to the Index in the back of a book - you can find all pages with reference to a topic
   * Index is stored seperately from the table for which index was created
   * Main purpose of index is to improve performance
   * Index can be created and dropped with **no effect on data**
   * Index types Single-column, Unique and Composite (two or more columns)
   * Index creation may impact performance of insert operations and be avoided on small tables, data is frequently manipulated, columns with high # of NULL values, large batch update processes. 
* **SQL Tuning** is the process of optimally building SQL statements to achieve results
	* Placing the **most restrictive conditions** in the WHERE clause
	* Format SQL for readability
	* Arrangement of tables in the FROM clause - smaller tables followed by larger tables
	* Avoid using LIKE, OR, HAVING, ORDER BY
* **Views** are virtual tables. View looks and acts like a table as far a user is concerned.
    * View is a predefined query and **does not require physical memory**
    * A view can contain all rows of a table or select rows from a table. 
    * A view can be created from one or many tables - depends on the query that created the view
    * View hides complexity
    * Views can be used as a security mechanism
    * Views can be used to support legacy systems
    * if data changes, view data change!


##SQL Injection  
* Source: https://www.interviewcake.com/article/javascript/sql
* Example:  
  ``` 
   var sqlText = "SELECT * FROM customers WHERE phone = '" + phoneInput + "';"   
   #phoneInput is provided by user via Browser   
   #phoneInput = 1' or 1=1;--   
   #resulting query 1=1 is always true    
   #-- comments out rest of the SQL   
  ```
* Prepare SQL statements **not build dynamic SQL**
* Validate input
* Sanitize input - escape special characters like " '
* Limit database access
* Don't log messages for end-users . Log messages to log files on the server with severity level.


