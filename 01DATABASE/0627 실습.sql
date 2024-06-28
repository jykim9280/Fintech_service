USE mywork;
SHOW TABLES;
select * from student_info;

DROP TABLE test_table; # DROP TABLE IF EXISTS test_table;
# 식별자 명명 규칙
# 식별자 : 데이터베이스 이름, 테이블 이름, 컬럼명
# 1. 최대 길이 64글자까지 가능
# 2. 사용 가능 문자 0-9, 영문자, 한글, $,_를 사용할 수 있다. (ex.물음표 불가능)
# 3. 예약어(create, database, avg, show)는 사용할 수 없다.
# 4. 대소문자 구분(windows는 관계없음), linux, unix 는 대소문자 구분

# 컬럼 생성시 주의사항
# 1. 한 테이블에 최대 4,096개까지 컬럼을 만들 수 있다.
# 2. 한 테이블에서 같은 컬럼명을 사용할 수 없다.
# 3. 데이터 베이스 내에서 같은 테이블명도 사용할 수 없다.

# SQL을 사용해서 테이블 만들기 create table
use mywork; #use로 꼭 선택 필요
create table highschool_students
(
	student_no VARCHAR(20),
    student_name VARCHAR(100),
    grade		TINYINT,
    class		VARCHAR(50),
    gender		VARCHAR(20),
    age			SMALLINT,
    enter_date	DATE
);

# 생성한 테이블의 구조를 출력 describe, desc (order by의 desc와 다름)
DESCRIBE highschool_students;
DESC highschool_students;

# 제약 조건을 넣어서 만들기 NULL, NOT NULL
 create table highschool_students2
 (
	student_no varchar(20) not null,
    student_name varchar(100) not null,
    grade tinyint null,
    class varchar(50) null,
    gender varchar(20) null,
    age smallint null,
    enter_date date
    );

DESCRIBE highschool_students2;
DROP TABLE highschool_students;

# 기본키 포함해서 만들기 (기본키 : primary key)
 create table highschool_students
 (
	student_no varchar(20) not null primary key,
    student_name varchar(100) not null,
    grade tinyint null,
    class varchar(50) null,
    gender varchar(20) null,
    age smallint null,
    enter_date date
    );
    
DESC highschool_students;
drop table highschool_students;

create table highschool_students
 (
	student_no varchar(20) not null,
    student_name varchar(100) not null,
    grade tinyint null,
    class varchar(50) null,
    gender varchar(20) null,
    age smallint null,
    enter_date date,
    primary key(student_no)
    );
drop table highschool_students;

#constraint primary key로 기본키 설정하기.
create table highschool_students
 (
	student_no varchar(20) not null,
    student_name varchar(100) not null,
    grade tinyint null,
    class varchar(50) null,
    gender varchar(20) null,
    age smallint null,
    enter_date date,
    constraint primary key(student_no)
    );
desc highschool_students;

# 기본 키 삭제하기 alter
# alter는 만들어진 데이터베이스나 테이블을 수정할 때 사용하는 명령어
alter table highschool_students drop primary key;
DESC highschool_students;

#기본 키 추가하기 add
alter table highschool_students add primary key(student_no);
desc highschool_students;

# 기본 키 생성시 주의사항
# 1. 한 테이블에서 기본 키는 1개만 생성할 수 있다.
# 2. 1개 이상의 컬럼으로 기본 키를 생성할 수 있다.
# 3. 기본 키 컬럼에는 not null을 적용한다.


SELECT COUNT(*) FROM box_office;
SELECT COUNT(*) FROM employees;
SELECT COUNT(*) FROM dept_manager;
SELECT COUNT(*) FROM dept_emp;
SELECT COUNT(*) FROM departments;
SELECT COUNT(*) FROM salaries;
SELECT COUNT(*) FROM titles;

# 테이블에 데이터 넣어보기
# insert into `테이블명` (컬럼명1, 컬럼명2...) values (컬럼1 데이터, 컬럼2 데이터);
# ` = 백틱
use mywork;
select * from highschool_students;
DESC highschool_students;
insert into `highschool_students` (student_no, student_name, grade, class, gender, age, enter_date) #컬럼명을 순서대로 넣어야 함
values
('TB0002', '홍길동' , 1, '11반', '남자', 20, '2024-03-02'),
('TB0002', '홍길동' , 1, '11반', '남자', 20, '2024-03-02'),
('TB0002', '홍길동' , 1, '11반', '남자', 20, '2024-03-02'),
('TB0003', '둘리', 2, '3반', '남자', 100, '2024-03-02');

#  INSERT INTO `salaries` VALUES (10001,60117,'1986-06-26','1987-06-26'),
# (10001,62102,'1987-06-26','1988-06-25')(정해진 순서대로 넣어줄게)

