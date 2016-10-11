
#MySQL Introduction: Query

[Download the sample data to get started](https://github.com/harishvc/quick-references/blob/master/mysql/sql/test.sql)

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

##Reference
 * https://dwbi.org/database/sql/72-top-20-sql-interview-questions-with-answers

##Question 1: Find Employees with hourly salary in range 80-100 (inclusive)
```
SELECT emp.Name as Employee, emp.sal as 'Hourly Salary' 
FROM emp where emp.sal between 80 and 100;
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

##Question 2: Find Employees with hourly salary in range 80-100 (inclusive) and the department name.
```
SELECT e.Name as Employee, e.sal as 'Hourly Salary', 
(select d.name from department d where d.id = e.id) as 'Department Name' 
FROM emp e 
where e.sal between 80 and 100;
+----------+---------------+-----------------+
| Employee | Hourly Salary | Department Name |
+----------+---------------+-----------------+
| Hash     |           100 | HR              |
| Robo     |           100 | Engineering     |
| Anno     |            80 | Logistics       |
| Darl     |            80 | NULL            |
+----------+---------------+-----------------+
4 rows in set (0.00 sec)
```


##Question 3: Find employees and their managers
**Self Join** is the act of joining one table with itself  - creating a **flat structure** from a table with hierarchy.
```
#Solution 1:
select e1.name as Employee, e2.name as Manager 
FROM emp e1, emp e2 
where  e1.mgr_id = e2.id;
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
select e1.name as Employee, e2.name as Manager 
from emp e1, emp e2 
where  e1.mgr_id = e2.id and e1.name <> e2.name;
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


##Question 4: Get head count in each deparment
```
select dept_id, count(dept_id) as 'Head Count' 
from emp GROUP BY dept_id;
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

##Question 5: Find the department with max head count
```
#Solution 1:
select dept_id, count(dept_id) as 'Head Count' 
from emp 
GROUP BY dept_id  
ORDER BY COUNT(dept_id) 
desc LIMIT 1;
+---------+------------+
| dept_id | Head Count |
+---------+------------+
|       2 |          4 |
+---------+------------+
1 row in set (0.00 sec)
```

##Question 5: Find #employees with max salary
```
select sal, count(sal) 
from emp 
GROUP BY sal 
order by sal desc 
limit 1;
+-----+------------+
| sal | count(sal) |
+-----+------------+
| 100 |          2 |
+-----+------------+
1 row in set (0.00 sec)
```

##Question 6: Find deparments having head count > 2
```
select dept_id, count(dept_id) as 'Head Count' 
from emp 
GROUP BY dept_id  
HAVING count(dept_id) > 2;
+---------+------------+
| dept_id | Head Count |
+---------+------------+
|       2 |          4 |
+---------+------------+
1 row in set (0.01 sec)
```

##Question 7: Find the Kth highest salary
`limit` takes 2 parameters -  start index (starting 0,optional) and #rows to include.
if K = 4, then start index = 3
```
select * from emp order by sal desc,doj ;
+----+--------+---------+--------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME   | SAL | DOJ        |
+----+--------+---------+--------+-----+------------+
|  1 |      1 |       2 | Hash   | 100 | 2012-01-01 |
|  2 |      1 |       2 | Robo   | 100 | 2012-01-01 |
|  5 |      2 |       2 | Anno   |  80 | 2012-02-01 |
|  6 |      1 |       2 | Darl   |  80 | 2012-02-11 |
|  7 |      1 |       3 | Pete   |  70 | 2012-04-16 |
|  9 |      2 |       4 | Tomiti |  70 | 2012-07-07 |
|  8 |      7 |       3 | Meme   |  60 | 2012-07-26 |
| 10 |      9 |       4 | Bhuti  |  60 | 2012-08-24 |
|  3 |      2 |       1 | Privy  |  50 | 2012-05-01 |
|  4 |      1 |       1 | Inno   |  50 | 2012-05-01 |
+----+--------+---------+--------+-----+------------+

select * from emp order by sal desc,doj limit 3,1;
+----+--------+---------+------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME | SAL | DOJ        |
+----+--------+---------+------+-----+------------+
|  6 |      1 |       2 | Darl |  80 | 2012-02-11 |
+----+--------+---------+------+-----+------------+
```

##Question 8: Find the newest employee
```
 SELECT * from emp order by doj desc limit 1;
+----+--------+---------+-------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME  | SAL | DOJ        |
+----+--------+---------+-------+-----+------------+
| 10 |      9 |       4 | Bhuti |  60 | 2012-08-24 |
+----+--------+---------+-------+-----+------------+
1 row in set (0.00 sec)
```

##Question 9: Find the total and average salary in each department
```
select emp.dept_id,sum(emp.sal) as 'total salary' ,count(emp.id) as 'head count' ,avg(emp.sal) from emp group by emp.dept_id;
+---------+--------------+------------+--------------+
| dept_id | total salary | head count | avg(emp.sal) |
+---------+--------------+------------+--------------+
|       1 |          100 |          2 |      50.0000 |
|       2 |          360 |          4 |      90.0000 |
|       3 |          130 |          2 |      65.0000 |
|       4 |          130 |          2 |      65.0000 |
+---------+--------------+------------+--------------+
4 rows in set (0.00 sec)
```

##Question 10: Find employees names starting with A
```
select name from emp where name LIKE 'a%';
+------+
| name |
+------+
| Anno |
+------+
1 row in set (0.00 sec)
```

##Question 11: Group employees by start year
```
SELECT SUBSTRING_INDEX(doj,"-",1) as Year, count(doj) from emp group by Year;
+------+------------+
| Year | count(doj) |
+------+------------+
| 2012 |         10 |
+------+------------+
1 row in set (0.00 sec)
```



