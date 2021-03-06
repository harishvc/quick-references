# MySQL: Basic Queries


## Clause
* **DISTINCT** unique values in a particular column. Can slow your queries down!
* **LIMIT** limit # of rows returned. Takes two arguments start (optional) and how many to return?
* **ORDER BY** defines the rule showing result. Followed by column name and type (ASC, DESC)
* **COUNT** simply counts the total number of non-null rows
* **SUM** totals the values in a given column. you can only use SUM on columns containing numerical values.
* **MIN** and **MAX** are SQL aggregation functions that return the lowest and highest values in a particular column
* **AVG** is a SQL aggregate function that calculates the average of a selected. Can only be used on numerical columns and it ignores *NULL* values
* **GROUP BY** allows you to separate data into groups, which can be aggregated independently of one another
* **HAVING** allow you to filter on aggregate. Used after **GROUP BY** 

## Query Clause Order
* SELECT
* FROM
* WHERE
* GROUP BY
* HAVING
* ORDER BY
* LIMIT

## Query precedence
```sql
SELECT <select_list>
FROM Table_A A
FULL OUTER JOIN Table_B B
ON A.Key = B.Key
   AND A.key2 > x #1
   AND b.key2 > z #2
WHERE
   A.key3 > y     #3
LIMIT 1           #4  

#1 & #2  are applied before the  FULL OUTER JOIN 
#3 is applied to the result of FULL OUTER JOIN
#4 is applied to final result
```

[Download the sample data to get started](https://github.com/harishvc/quick-references/blob/master/mysql/sql/test.sql)
## Schema
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

## Question: Find Employees with hourly salary in range 80-100 (inclusive)
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

## Question: Find Employees with hourly salary in range 80-100 (inclusive) and the department name.
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


## Question: Find employees and their managers
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


## Question: Find the head count in each department :thumbsup:
```
mysql> select d.id, d.name, count(e.name) 
    -> from emp e, department d
    -> where e.dept_id = d.id 
    -> group by d.name, d.id;
+----+-------------+---------------+
| id | name        | count(e.name) |
+----+-------------+---------------+
|  2 | Engineering |             4 |
|  1 | HR          |             2 |
|  3 | Marketing   |             2 |
|  4 | Sales       |             2 |
+----+-------------+---------------+
4 rows in set (0.01 sec)
```

## Question: Find the department with max head count
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

## Question: Find #employees with max salary
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

## Question: Find deparments having head count > 2
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

## Question: Find the Kth highest salary
`limit` takes 2 parameters -  start index (starting 0,optional) and #rows to include.
if K = 4, then start index = 3
```
#Solution 1: using limit
select * from emp order by sal desc,doj limit 3,1;
+----+--------+---------+------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME | SAL | DOJ        |
+----+--------+---------+------+-----+------------+
|  6 |      1 |       2 | Darl |  80 | 2012-02-11 |
+----+--------+---------+------+-----+------------+

#Solution 2: not using limit
#http://www.programmerinterview.com/index.php/database-sql/find-nth-highest-salary-sql/
> select * from emp e1 
  where (3) = (select count(e2.sal) from emp e2 where e2.sal >= e1.sal);

#This process is limited if there are employees with similar salaries
```


## Question: Find the newest employee
```
 SELECT * from emp order by doj desc limit 1;
+----+--------+---------+-------+-----+------------+
| ID | MGR_ID | DEPT_ID | NAME  | SAL | DOJ        |
+----+--------+---------+-------+-----+------------+
| 10 |      9 |       4 | Bhuti |  60 | 2012-08-24 |
+----+--------+---------+-------+-----+------------+
1 row in set (0.00 sec)
```

## Question: Find the total and average salary in each department
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

## Question: Find employees names starting with A
```
select name from emp where name LIKE 'a%';
+------+
| name |
+------+
| Anno |
+------+
1 row in set (0.00 sec)
```

## Question: Group employees by start year
```
SELECT SUBSTRING_INDEX(doj,"-",1) as Year, count(doj) from emp group by Year;
+------+------------+
| Year | count(doj) |
+------+------------+
| 2012 |         10 |
+------+------------+
1 row in set (0.00 sec)
```

## Question: How many employees weere hired in the first quarter of 2012? 
```
mysql> select count(*) from emp 
    -> where doj between '2012-01-01' and '2012-03-31';
+----------+
| count(*) |
+----------+
|        4 |
+----------+
1 row in set (0.00 sec)
```

## Find #employees hired in each department during the third quarter of 2012?
```
mysql> select dept_id, count(dept_id) from emp  
    -> where  doj between '2012-07-01' and '2012-09-30'
    -> group by dept_id
    -> order by count(dept_id) desc;
+---------+----------------+
| dept_id | count(dept_id) |
+---------+----------------+
|       4 |              2 |
|       3 |              1 |
+---------+----------------+
2 rows in set (0.00 sec)
```

## What departments did **not** hire in the third quarter of 2012?
```
mysql> select id,name from department 
    -> where id not in
    -> (select DISTINCT(dept_id) from emp where doj between '2012-07-01' and '2012-09-30');
+----+-------------+
| id | name        |
+----+-------------+
|  1 | HR          |
|  2 | Engineering |
|  5 | Logistics   |
+----+-------------+
3 rows in set (0.00 sec)
```



## Question: Find the direct reports each manager has?
```
mysql> select count(*), e2.name as Manager from emp e1, emp e2 
    -> where e1.mgr_id = e2.id and e1.id <> e2.id
    -> group by manager
    -> order by count(*) desc;
+----------+---------+
| count(*) | Manager |
+----------+---------+
|        4 | Hash    |
|        3 | Robo    |
|        1 | Pete    |
|        1 | Tomiti  |
+----------+---------+
4 rows in set (0.00 sec)
```


## Question: Find the month most employees celebrate their work anniversary?
`substring` returns a specified number of characters from a particular position of a given string. `substring` takes 3 input arguments - col name, start index, #characters
```
mysql> select substring(doj,6,2) as 'Anniversary Month', count(*) 
    -> from emp 
    -> group by substring(doj,6,2) 
    -> order by count(*) desc
    -> limit 1;
+-------------------+----------+
| Anniversary Month | count(*) |
+-------------------+----------+
| 01                |        2 |
+-------------------+----------+
1 row in set (0.00 sec)

```

## What is the weekly salary of the Marketing & Sales team?
```
#create a view for dept_id 3 & 4
mysql> create view sales_marketing_team as select * from emp where dept_id in (4,3);

mysql> select sum(sal) from sales_marketing_team;
+----------+
| sum(sal) |
+----------+
|      260 |
+----------+
1 row in set (0.00 sec)
```

## Reference
 * https://dwbi.org/database/sql/72-top-20-sql-interview-questions-with-answers
