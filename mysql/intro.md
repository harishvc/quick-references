
#MySQL Query Introduction

[Download the SQL](https://github.com/harishvc/quick-references/blob/master/mysql/sql/test.sql) to get started

##Schema
```
CREATE TABLE DEPARTMENT 
(
ID INT NOT NULL PRIMARY KEY, 
NAME VARCHAR(30)   
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

mysql> describe department;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| ID    | int(11)     | NO   | PRI | NULL    |       |
| NAME  | varchar(30) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
2 rows in set (0.00 sec)
```

##Reference
 * https://dwbi.org/database/sql/72-top-20-sql-interview-questions-with-answers

##Question 1: Find Employees with hourly salary in range 80-100 (inclusive)
```
SELECT emp.Name as Employee, emp.sal as 'Hourly Salary' FROM emp where emp.sal between 80 and 100;
+----------+---------------+
| Employee | Hourly Salary |
+----------+---------------+
| Hash     |           100 |
| Robo     |           100 |
| Anno     |            80 |
| Darl     |            80 |
+----------+---------------+
4 rows in set (0.00 sec)
```


##Question 2: Find employees and their managers
Self Join is the act of joining one table with itself  - creating a flat structure from a table with hierarchy.
```
#Solution 1:
select e1.name as Employee, e2.name as Manager from emp e1, emp e2 where  e1.mgr_id = e2.id;
+----------+---------+
| Employee | Manager |
+----------+---------+
| Hash     | Hash    |
| Robo     | Hash    |
| Privy    | Robo    |
| Inno     | Hash    |
| Anno     | Robo    |
| Darl     | Hash    |
| Pete     | Hash    |
| Meme     | Pete    |
| Tomiti   | Robo    |
| Bhuti    | Tomiti  |
+----------+---------+
10 rows in set (0.00 sec)
Observation: "Hash" is a manager of "Hash"!


#Solution 2:
select e1.name as Employee, e2.name as Manager from emp e1, emp e2 where  e1.mgr_id = e2.id and e1.name <> e2.name;
+----------+---------+
| Employee | Manager |
+----------+---------+
| Robo     | Hash    |
| Privy    | Robo    |
| Inno     | Hash    |
| Anno     | Robo    |
| Darl     | Hash    |
| Pete     | Hash    |
| Meme     | Pete    |
| Tomiti   | Robo    |
| Bhuti    | Tomiti  |
+----------+---------+
9 rows in set (0.00 sec)
Observation: "Hash" is not listed
```


##Question 3: Get head count in each deparment
```
select dept_id, count(dept_id) as 'Head Count' from emp GROUP BY dept_id;
+---------+------------+
| dept_id | Head Count |
+---------+------------+
|       1 |          2 |
|       2 |          4 |
|       3 |          2 |
|       4 |          2 |
+---------+------------+
4 rows in set (0.01 sec)
```

##Question 4: Find the department with max head count
```
#Solution 1:
select dept_id, count(dept_id) as 'Head Count' from emp GROUP BY dept_id  ORDER BY COUNT(dept_id) desc LIMIT 1;
+---------+------------+
| dept_id | Head Count |
+---------+------------+
|       2 |          4 |
+---------+------------+
1 row in set (0.00 sec)
```

##Question 5: Find #employees with max salary
```
select sal, count(sal) from emp GROUP BY sal order by sal desc limit 1;
+-----+------------+
| sal | count(sal) |
+-----+------------+
| 100 |          2 |
+-----+------------+
1 row in set (0.00 sec)
```

##Question 6: Find deparments having head count > 2
```
select dept_id, count(dept_id) as 'Head Count' from emp GROUP BY dept_id  HAVING count(dept_id) > 2;
+---------+------------+
| dept_id | Head Count |
+---------+------------+
|       2 |          4 |
+---------+------------+
1 row in set (0.01 sec)
```


##TODO
1. Find Employees & their department with hourly salary in range 80-100 (inclusive)