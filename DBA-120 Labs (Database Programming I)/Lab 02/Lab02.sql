Question 1:
SQL> sqlplus scott/tiger

Question 2:
No. SQLPlus commands do not allow manipulation of values in the database.

Question 3:
True.

Question 4:
True.

Question 5:
1. Comma after ename
2. Column salary is equal to sal
3. Multiplication should be done by an asterix
4. The new name of the column should be double quoted

SQL> SELECT empno, ename,
  2  sal*12 "ANNUAL SALARY"
  3  FROM emp;

Question 6:
SQL> SELECT *
  2  FROM dept;

    DEPTNO DNAME          LOC                                                                                                                                                                                                                                                                               
---------- -------------- -------------                                                                                                                                                                                                                                                                     
        10 ACCOUNTING     NEW YORK                                                                                                                                                                                                                                                                          
        20 RESEARCH       DALLAS                                                                                                                                                                                                                                                                            
        30 SALES          CHICAGO                                                                                                                                                                                                                                                                           
        40 OPERATIONS     BOSTON                                                                                                                                                                                                                                                                            

Question 7:
SQL> SELECT empno, ename, job, hiredate
  2  FROM emp;

     EMPNO ENAME      JOB       HIREDATE                                                                                                                                                                                                                                                                    
---------- ---------- --------- ---------                                                                                                                                                                                                                                                                   
      7839 KING       PRESIDENT 17-NOV-81                                                                                                                                                                                                                                                                   
      7698 BLAKE      MANAGER   01-MAY-81                                                                                                                                                                                                                                                                   
      7782 CLARK      MANAGER   09-JUN-81                                                                                                                                                                                                                                                                   
      7566 JONES      MANAGER   02-APR-81                                                                                                                                                                                                                                                                   
      7654 MARTIN     SALESMAN  28-SEP-81                                                                                                                                                                                                                                                                   
      7499 ALLEN      SALESMAN  20-FEB-81                                                                                                                                                                                                                                                                   
      7844 TURNER     SALESMAN  08-SEP-81                                                                                                                                                                                                                                                                   
      7900 JAMES      CLERK     03-DEC-81                                                                                                                                                                                                                                                                   
      7521 WARD       SALESMAN  22-FEB-81                                                                                                                                                                                                                                                                   
      7902 FORD       ANALYST   03-DEC-81                                                                                                                                                                                                                                                                   
      7369 SMITH      CLERK     17-DEC-80                                                                                                                                                                                                                                                                   
      7788 SCOTT      ANALYST   09-DEC-82                                                                                                                                                                                                                                                                   
      7876 ADAMS      CLERK     12-JAN-83                                                                                                                                                                                                                                                                   
      7934 MILLER     CLERK     23-JAN-82                                                                                                                                                                                                                                                                   

14 rows selected.

SQL> SAVE p1q7.txt
Created file p1q7.txt

Question 8:
SQL> SELECT DISTINCT job
  2  FROM emp;

JOB                                                                                                                                                                                                                                                                                                         
---------                                                                                                                                                                                                                                                                                                   
SALESMAN                                                                                                                                                                                                                                                                                                    
CLERK                                                                                                                                                                                                                                                                                                       
ANALYST                                                                                                                                                                                                                                                                                                     
MANAGER                                                                                                                                                                                                                                                                                                     
PRESIDENT                                                                                                                                                                                                                                                                                                   

Question 9:
SQL> GET p1q7.txt
  1  SELECT empno, ename, job, hiredate
  2* FROM emp
SQL> EDIT p1q7.txt

SQL> @p1q7.txt

     Emp # Employee   Job       Hire Date                                                                                                                                                                                                                                                                   
---------- ---------- --------- ---------                                                                                                                                                                                                                                                                   
      7839 KING       PRESIDENT 17-NOV-81                                                                                                                                                                                                                                                                   
      7698 BLAKE      MANAGER   01-MAY-81                                                                                                                                                                                                                                                                   
      7782 CLARK      MANAGER   09-JUN-81                                                                                                                                                                                                                                                                   
      7566 JONES      MANAGER   02-APR-81                                                                                                                                                                                                                                                                   
      7654 MARTIN     SALESMAN  28-SEP-81                                                                                                                                                                                                                                                                   
      7499 ALLEN      SALESMAN  20-FEB-81                                                                                                                                                                                                                                                                   
      7844 TURNER     SALESMAN  08-SEP-81                                                                                                                                                                                                                                                                   
      7900 JAMES      CLERK     03-DEC-81                                                                                                                                                                                                                                                                   
      7521 WARD       SALESMAN  22-FEB-81                                                                                                                                                                                                                                                                   
      7902 FORD       ANALYST   03-DEC-81                                                                                                                                                                                                                                                                   
      7369 SMITH      CLERK     17-DEC-80                                                                                                                                                                                                                                                                   
      7788 SCOTT      ANALYST   09-DEC-82                                                                                                                                                                                                                                                                   
      7876 ADAMS      CLERK     12-JAN-83                                                                                                                                                                                                                                                                   
      7934 MILLER     CLERK     23-JAN-82                                                                                                                                                                                                                                                                   

14 rows selected.

Question 10:
SQL> SELECT ename ||', '|| job "Employee and Title"
  2  FROM emp;

Employee and Title                                                                                                                                                                                                                                                                                          
---------------------                                                                                                                                                                                                                                                                                       
KING, PRESIDENT                                                                                                                                                                                                                                                                                             
BLAKE, MANAGER                                                                                                                                                                                                                                                                                              
CLARK, MANAGER                                                                                                                                                                                                                                                                                              
JONES, MANAGER                                                                                                                                                                                                                                                                                              
MARTIN, SALESMAN                                                                                                                                                                                                                                                                                            
ALLEN, SALESMAN                                                                                                                                                                                                                                                                                             
TURNER, SALESMAN                                                                                                                                                                                                                                                                                            
JAMES, CLERK                                                                                                                                                                                                                                                                                                
WARD, SALESMAN                                                                                                                                                                                                                                                                                              
FORD, ANALYST                                                                                                                                                                                                                                                                                               
SMITH, CLERK                                                                                                                                                                                                                                                                                                
SCOTT, ANALYST                                                                                                                                                                                                                                                                                              
ADAMS, CLERK                                                                                                                                                                                                                                                                                                
MILLER, CLERK                                                                                                                                                                                                                                                                                               

14 rows selected.

Question 11:
SQL> SELECT empno ||','|| ename ||','|| job ||','|| mgr ||','|| hiredate ||','|| sal ||','|| comm ||','|| deptno "THE_OUTPUT"
  2  from emp;

THE_OUTPUT                                                                                                                                                                                                                                                                                                  
------------------------------------------------                                                       
7839,KING,PRESIDENT,,17-NOV-81,5000,,10                                                                                                                                                                                                                                                                     
7698,BLAKE,MANAGER,7839,01-MAY-81,2850,,30                                                                                                                                                                                                                                                                  
7782,CLARK,MANAGER,7839,09-JUN-81,2450,,10                                                                                                                                                                                                                                                                  
7566,JONES,MANAGER,7839,02-APR-81,2975,,20                                                                                                                                                                                                                                                                  
7654,MARTIN,SALESMAN,7698,28-SEP-81,1250,1400,30                                                                                                                                                                                                                                                            
7499,ALLEN,SALESMAN,7698,20-FEB-81,1600,300,30                                                                                                                                                                                                                                                              
7844,TURNER,SALESMAN,7698,08-SEP-81,1500,0,30                                                                                                                                                                                                                                                               
7900,JAMES,CLERK,7698,03-DEC-81,950,,30                                                                                                                                                                                                                                                                     
7521,WARD,SALESMAN,7698,22-FEB-81,1250,500,30                                                                                                                                                                                                                                                               
7902,FORD,ANALYST,7566,03-DEC-81,3000,,20                                                                                                                                                                                                                                                                   
7369,SMITH,CLERK,7902,17-DEC-80,800,,20                                                                                                                                                                                                                                                                     
7788,SCOTT,ANALYST,7566,09-DEC-82,3000,,20                                                                                                                                                                                                                                                                  
7876,ADAMS,CLERK,7788,12-JAN-83,1100,,20                                                                                                                                                                                                                                                                    
7934,MILLER,CLERK,7782,23-JAN-82,1300,,10                                                                                                                                                                                                                                                                   

14 rows selected.

SQL> SPOOL off
