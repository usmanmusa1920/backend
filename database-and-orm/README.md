
# Database (db)

This repository contains how to use SQL (structure query langage) database with python using sqlalchemy, sqlite3, and that of mysql-connector for mysql

## Mysql 1

mysql> select * from students;
+----+----------+--------+----------+------------+---------+-------+
| id | username | name   | admin    | department | faculty | field |
+----+----------+--------+----------+------------+---------+-------+
|  1 | Shehu    | Usman  | jambitor | NULL       | physics |       |
|  3 | Man      | Usman  | jambitor | NULL       | NULL    |       |
|  4 | Myusuf   | Yusuf  | jambitor | NULL       | NULL    |       |
|  6 | Mami     | Aisha  | jambitor | NULL       | NULL    |       |
|  7 | Fati     | Fatima | jambitor | NULL       | NULL    |       |
|  8 | A        | a      | jam      | NULL       | p       | o     |
+----+----------+--------+----------+------------+---------+-------+
6 rows in set (0.00 sec)

mysql> insert into students(username, name, admin, field, faculty) values ('Usman', 'Usman', '2021', 'quantum', 'physics');
Query OK, 1 row affected (0.15 sec)

mysql> select count(name) from students where faculty = 'physics';
+-------------+
| count(name) |
+-------------+
|           2 |
+-------------+
1 row in set (0.00 sec)

mysql> select * from students;
+----+----------+--------+----------+------------+---------+---------+
| id | username | name   | admin    | department | faculty | field   |
+----+----------+--------+----------+------------+---------+---------+
|  1 | Shehu    | Usman  | jambitor | NULL       | physics |         |
|  3 | Man      | Usman  | jambitor | NULL       | NULL    |         |
|  4 | Myusuf   | Yusuf  | jambitor | NULL       | NULL    |         |
|  6 | Mami     | Aisha  | jambitor | NULL       | NULL    |         |
|  7 | Fati     | Fatima | jambitor | NULL       | NULL    |         |
|  8 | A        | a      | jam      | NULL       | p       | o       |
| 12 | Usman    | Usman  | 2021     | NULL       | physics | quantum |
+----+----------+--------+----------+------------+---------+---------+
7 rows in set (0.00 sec)

mysql> delete from students where admin = '2021';
Query OK, 1 row affected (0.16 sec)

mysql> select * from students;
+----+----------+--------+----------+------------+---------+-------+
| id | username | name   | admin    | department | faculty | field |
+----+----------+--------+----------+------------+---------+-------+
|  1 | Shehu    | Usman  | jambitor | NULL       | physics |       |
|  3 | Man      | Usman  | jambitor | NULL       | NULL    |       |
|  4 | Myusuf   | Yusuf  | jambitor | NULL       | NULL    |       |
|  6 | Mami     | Aisha  | jambitor | NULL       | NULL    |       |
|  7 | Fati     | Fatima | jambitor | NULL       | NULL    |       |
|  8 | A        | a      | jam      | NULL       | p       | o     |
+----+----------+--------+----------+------------+---------+-------+
6 rows in set (0.00 sec)

mysql> 


## Mysql 2

usman@usman-X140-L75BK in:~
 $ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 26
Server version: 8.0.28-0ubuntu0.20.04.3 (Ubuntu)

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.05 sec)

mysql> CREATE DATABASE fug_students;
Query OK, 1 row affected (0.21 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| fug_students       |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.05 sec)

mysql> USE fug_students;
Database changed
mysql> SHOW TABLES;
Empty set (0.00 sec)

mysql> CREATE TABLE student_info(name VARCHAR(255), faculty VARCHAR(255), dept VARCHAR(255), field VARCHAR(255) DEFAULT 'quantum', admin_no INT NOT NULL UNIQUE, cgpa INT NOT NULL, serial INT NOT NULL AUTO_INCREMENT, PRIMARY KEY (`serial`), created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
Query OK, 0 rows affected (2.25 sec)

mysql> SHOW TABLES;
+------------------------+
| Tables_in_fug_students |
+------------------------+
| student_info           |
+------------------------+
1 row in set (0.03 sec)

mysql> INSERT INTO student_info(name, faculty, dept, field, admin_no, cgpa) VALUES ('Usman Musa', 'sciense', 'physics', 'quantum programming', 2021, 3.98);
Query OK, 1 row affected (0.16 sec)

mysql> SELECT * FROM student_info;
+------------+---------+---------+---------------------+----------+------+--------+---------------------+
| name       | faculty | dept    | field               | admin_no | cgpa | serial | created             |
+------------+---------+---------+---------------------+----------+------+--------+---------------------+
| Usman Musa | sciense | physics | quantum programming |     2021 |    4 |      1 | 2023-02-05 09:49:09 |
+------------+---------+---------+---------------------+----------+------+--------+---------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO student_info(name, faculty, dept, field, admin_no, cgpa) VALUES ('Usman Musa', 'sciense', 'physics', 2021,
3.98);
ERROR 1136 (21S01): Column count doesn't match value count at row 1
mysql> INSERT INTO student_info(name, faculty, dept, field, admin_no, cgpa) VALUES ('Usman Musa', 'sciense', 'physics', 2022,
3.98);
ERROR 1136 (21S01): Column count doesn't match value count at row 1
mysql> INSERT INTO student_info(name, faculty, dept, admin_no, cgpa) VALUES ('Usman Musa', 'sciense', 'physics', 2021, 3.98);
ERROR 1062 (23000): Duplicate entry '2021' for key 'student_info.admin_no'
mysql> INSERT INTO student_info(name, faculty, dept, admin_no, cgpa) VALUES ('Usman Musa', 'sciense', 'physics', 2022, 3.98);
Query OK, 1 row affected (0.14 sec)

mysql> SELECT * FROM student_info;
+------------+---------+---------+---------------------+----------+------+--------+---------------------+
| name       | faculty | dept    | field               | admin_no | cgpa | serial | created             |
+------------+---------+---------+---------------------+----------+------+--------+---------------------+
| Usman Musa | sciense | physics | quantum programming |     2021 |    4 |      1 | 2023-02-05 09:49:09 |
| Usman Musa | sciense | physics | quantum             |     2022 |    4 |      3 | 2023-02-05 09:50:32 |
+------------+---------+---------+---------------------+----------+------+--------+---------------------+
2 rows in set (0.00 sec)

mysql> INSERT INTO student_info(name, faculty, dept, field, admin_no, cgpa) VALUES ('Aliyu Adam', 'science', 'chemistry', 'radiography', 1922,
Query OK, 1 row affected (0.25 sec)

mysql> SELECT * FROM student_info;
+------------+---------+-----------+---------------------+----------+------+--------+---------------------+
| name       | faculty | dept      | field               | admin_no | cgpa | serial | created             |
+------------+---------+-----------+---------------------+----------+------+--------+---------------------+
| Usman Musa | sciense | physics   | quantum programming |     2021 |    4 |      1 | 2023-02-05 09:49:09 |
| Usman Musa | sciense | physics   | quantum             |     2022 |    4 |      3 | 2023-02-05 09:50:32 |
| Aliyu Adam | science | chemistry | radiography         |     1922 |    3 |      4 | 2023-02-05 09:52:04 |
+------------+---------+-----------+---------------------+----------+------+--------+---------------------+
3 rows in set (0.00 sec)

mysql> 
