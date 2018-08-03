# MySQL JOIN Introduction

## Joins (7 types)
![Types of Join](join-variations.png) [1]
* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* OUTER JOIN
* LEFT JOIN EXCLUDING INNER JOIN
* RIGHT JOIN EXCLUDING INNER JOIN
* OUTER JOIN EXCLUDING INNER JOIN

## Fundamentals
* **LEFT JOIN** command tells the database to return all rows in the table in the FROM clause, regardless of whether or not they have matches in the table in the LEFT JOIN clause [2]
* **RIGHT JOIN**  similar to left joins except they return all rows from the table in the RIGHT JOIN clause and only matching rows from the table in the FROM clause [2] . RIGHT JOIN is rarely used because you can achieve the results of a RIGHT JOIN by simply switching the two joined table names in a LEFT JOIN
* 

## Syntax
```sql
SELECT <select_list> 
FROM Table_A A
*join_type* Table_B B
ON A.Key = B.Key
WHERE B.Key IS NULL

*join_type* = JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN
```


## Schema
[Download the sample data to get started](https://github.com/harishvc/quick-references/blob/master/mysql/sql/test.sql) 
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

## Reference
 * https://dwbi.org/database/sql/72-top-20-sql-interview-questions-with-answers


## Inner Join (emulate INTERSECT operator)
Question 1: List employees and departments they belong 
```
select emp.name as Employee, department.name as 'Employee Department' 
from emp 
INNER JOIN department 
ON department.id=emp.dept_id 
order by emp.name;
+----------+---------------------+
| Employee | Employee Department |
+----------+---------------------+
| Anno     | Engineering         |
| Bhuti    | Sales               |
| Darl     | Engineering         |
| Hash     | Engineering         |
| Inno     | HR                  |
| Meme     | Marketing           |
| Pete     | Marketing           |
| Privy    | HR                  |
| Robo     | Engineering         |
| Tomiti   | Sales               |
+----------+---------------------+
10 rows in set (0.00 sec)
```


## Left Outer Join (emulate MINUS operator)

### Question: Find the department with no employees 
```
select department.name as Department 
from department 
LEFT OUTER JOIN emp 
on department.id=emp.dept_id 
where emp.name is NULL;
+------------+
| Department |
+------------+
| Logistics  |
+------------+
1 row in set (0.00 sec)
```

### Question: Find the head count in each department
```
mysql> select d.name, count(e.name) from department d
    -> LEFT JOIN emp e
    -> ON e.dept_id = d.id
    -> GROUP BY d.name;
+-------------+---------------+
| name        | count(e.name) |
+-------------+---------------+
| Engineering |             4 |
| HR          |             2 |
| Logistics   |             0 |
| Marketing   |             2 |
| Sales       |             2 |
+-------------+---------------+
5 rows in set (0.01 sec)
```



## RIGHT Outer Join (emulate MINUS operator)



## Full Join (Union and Union All)
* UNION and UNION ALL both unify for add two **structurally similar data sets**, 
* UNION operation returns only the unique records from the resulting data set 
* UNION ALL will return all the rows, even if one or more rows are **duplicated** to each other.
```
SELECT * FROM EMP WHERE ID = 5 UNION  SELECT * FROM EMP WHERE ID = 5;
+----+--------+---------+------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME | SAL | DOJ        |
+----+--------+---------+------+-----+------------+
|  5 |      2 |       2 | Anno |  80 | 2012-02-01 |
+----+--------+---------+------+-----+------------+


SELECT * FROM EMP WHERE ID = 5 UNION ALL SELECT * FROM EMP WHERE ID = 5;
+----+--------+---------+------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME | SAL | DOJ        |
+----+--------+---------+------+-----+------------+
|  5 |      2 |       2 | Anno |  80 | 2012-02-01 |
|  5 |      2 |       2 | Anno |  80 | 2012-02-01 |
+----+--------+---------+------+-----+------------+
2 rows in set (0.00 sec)

```

## Self Joins
* Self Join is the act of joining one table with itself
* Self Join is often very useful to convert a hierarchical structure into a flat structure
````
SELECT e.name EMPLOYEE, m.name MANAGER 
FROM EMP e, EMP m 
WHERE e.mgr_id = m.id;
+----------+---------+
| EMPLOYEE | MANAGER |
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
````

## Find employees who have the highest salary in each department
``` 
 select e1.name, e1.dept_id, d.name, e1.sal 
 from emp e1, (select dept_id, max(sal) as msal from emp group by dept_id) e2, department d
 where e1.dept_id = e2.dept_id and e1.sal=e2.msal and d.id = e1.dept_id;
+--------+---------+-------------+-----+
| name   | dept_id | name        | sal |
+--------+---------+-------------+-----+
| Hash   |       2 | Engineering | 100 |
| Robo   |       2 | Engineering | 100 |
| Privy  |       1 | HR          |  50 |
| Inno   |       1 | HR          |  50 |
| Pete   |       3 | Marketing   |  70 |
| Tomiti |       4 | Sales       |  70 |
+--------+---------+-------------+-----+
6 rows in set (0.00 sec)
```

## Additional Resource
[1] https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins
[2] https://community.modeanalytics.com/sql/tutorial/introduction-to-sql/

