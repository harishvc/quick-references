
#MySQL Fundamentals

## What is MySQL?
MySQL is an open source, multithreaded, multi-user SQL database management system.

## Explain various MySQL Engines?
```
mysql> SHOW ENGINES;
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                        | Transactions | XA   | Savepoints |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
| InnoDB             | DEFAULT | Supports transactions, row-level locking, and foreign keys     | YES          | YES  | YES        |
| MRG_MYISAM         | YES     | Collection of identical MyISAM tables                          | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables      | NO           | NO   | NO         |
| BLACKHOLE          | YES     | /dev/null storage engine (anything you write to it disappears) | NO           | NO   | NO         |
| MyISAM             | YES     | MyISAM storage engine                                          | NO           | NO   | NO         |
| CSV                | YES     | CSV storage engine                                             | NO           | NO   | NO         |
| ARCHIVE            | YES     | Archive storage engine                                         | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                             | NO           | NO   | NO         |
| FEDERATED          | NO      | Federated MySQL storage engine                                 | NULL         | NULL | NULL       |
+--------------------+---------+----------------------------------------------------------------+--------------+------+------------+
9 rows in set (0.00 sec)
```
MySQL supports 9 engines out of the box. The most popular ones are **InnoDB** and **MyISAM**

InnoDB
	- Supports Foreign Keys
	- Supports transactions
	- Row level locking
	- Stores data in clustered indexes to reduce I/O
	- Full text search

MyISAM
	- Table level locking
	- Small Footprint
	- Table-level locking limits the performance in write workloads, so it is often used in 
	  read-only or read-mostly workloads 
	- Full text search


## What is ACID?
ACID (Atomicity, Consistency, Isolation, Durability) is a set of properties of database transactions
* **Atomicity** - Atomicity requires that each transaction be "all or nothing": if one part of the transaction fails, then the entire transaction fails, and the database state is left unchanged
* **Consistency** -  Consistency property ensures that any transaction will bring the database from one valid state to another. Any data written to the database **must be valid** according to all defined rules, including constraints, cascades, triggers, etc
* **Isolation** -  Isolation property ensures that the concurrent execution of transactions results in a system state that would be obtained if transactions were executed serially
* **Durability** - Durability property ensures that once a transaction has been committed, it will remain so, even in the event of power loss, crashes, or errors.

## What is CRUD?
CRUD stands for Create Read Update Delete


## How many Triggers are possible in MySQL?
There are only six Triggers allowed to use in MySQL database.
 - Before Insert
 - After Insert
 - Before Update
 - After Update
 - Before Delete
 - After Delete

## What is the difference between CHAR and VARCHAR?
 - CHAR and VARCHAR are differ in storage and retrieval
 - CHAR column length is fixed while VARCHAR length is variable.
 - CHAR data type can hold is 255 character while VARCHAR can hold up to 4000 characters.
 - CHAR is 50% faster than VARCHAR.
 - CHAR uses static memory allocation while VARCHAR uses dynamic memory allocation

## How many columns can you index?
 - 16


## How will you get current date in MySQL?
```
SELECT CURRENT_DATE;
+----------------+
| CURRENT_DATE() |
+----------------+
| 2016-10-09     |
+----------------+
1 row in set (0.01 sec)
```

## Find all databases?
```
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
```

## Find a table schema?
```
mysql> use mysql
Database changed

mysql> show tables;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| db                        |
| engine_cost               |
| event                     |
| func                      |

mysql> describe  user;
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Field                  | Type                              | Null | Key | Default               | Extra |
+------------------------+-----------------------------------+------+-----+-----------------------+-------+
| Host                   | char(60)                          | NO   | PRI |                       |       |
| User                   | char(32)                          | NO   | PRI |                       |       |

```

## How do you backup MySQL database?
`mysqladmin` can be run from the command lime to back up a specific database or mysql databases. if the database is large, you can `|` the output to `gzip` . `mysqladmin` can alos be configured to run via the `cron` on a regular basics.


## What is an index?
Index is a database is similar to the Index in the back of a book - you can find all pages with reference to a topic. Main purpose of index is to improve performance. More information about [index](https://github.com/harishvc/quick-references/blob/master/mysql/intro-performance-tuning.md).  

## What are views?
**Views** are virtual tables. View looks and acts like a table as far a user is concerned. View is a predefined query and **does not require physical memory** . More information about [views](https://github.com/harishvc/quick-references/blob/master/mysql/intro-performance-tuning.md).
```
#create view
mysql>> create view sales_marketing_team as select * from emp where dept_id in (4,3);


#show views
mysql> SHOW FULL TABLES;
+----------------------+------------+
| Tables_in_test1002   | Table_type |
+----------------------+------------+
| DEPARTMENT           | BASE TABLE |
| EMP                  | BASE TABLE |
| sales_marketing_team | VIEW       |
+----------------------+------------+

mysql>SHOW FULL TABLES WHERE TABLE_TYPE LIKE 'VIEW';
+----------------------+------------+
| Tables_in_test1002   | Table_type |
+----------------------+------------+
| sales_marketing_team | VIEW       |
+----------------------+------------+
1 row in set (0.02 sec)

```

## Primary vs Foreign key?
* Primary Key is the term used to identify one or more columns in table that make a row of data unique. Primary Key is assigned during table creation.
* Foreign Key is a column that references a primary key in another table. A foreign Key constraint is the main mechanism used to enforce referential integrity between tables in a relational database.
```
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
```

## What is normalization?
Database normalization, or simply normalization, is the process of organizing the columns (attributes) and tables (relations) of a relational database to reduce data redundancy and improve data integrity. Key benefits include flexible database design, better handle on security and data consistency. There may be performance issues.

