# select sysdate() 현재 날짜와 시간 반환
select sysdate();
select sysdate(), sleep(2), sysdate();
select now(), sleep(2), now();

# 현재 날짜를 기준으로 현재 일이 속한 월의 마지막 날짜에
# 해당하는 요일을 구하는 쿼리를 작성하세요.
select dayname(last_day(now()));

# 형 변환 함수 : 형 변환 데이터 타입을 변환하는 함수
# CAST(값 as 변환할 데이터 타입)

select cast(10 as char);
select cast('-10' as signed);


# CRUD 연습
use mywork;
create table emp_test
(
	emp_no int not null,
    emp_name varchar(30) not null,
    hire_date date       null,
    salary int           null,
    primary key(emp_no)
);

desc emp_test;

insert into `emp_test`
(emp_no, emp_name, hire_date, salary)
values (1007, '패러데이', '2021-04-01', 2200),
(1008, '맥스웰', '2021-04-05', 3300),
(1009, '플랑크', '2021-04-05', 4400);

select * from emp_test;

# 테이블 데이터 수정하기
# update 테이블 set 컬럼1 = 값, 컬럼2 = 값 where 찾을 값 (where 필수, 특정 행을 지정하지 않으면 그 컬럼 값이 싹 바뀜, 근데 mysql이 막아놓음 !! 굿굿)
# where 절 다음 키값으로만 하도록 초기 설정되어있음. edit > preference > sql editor > safe update uncheked시, 변경 가능
update emp_test
set salary = 4400 where emp_no = 1009;
# delete 문으로 데이터 삭제하기
# delete from 테이블 where 조건
delete from emp_test; #전체 삭제
select * from emp_test;

# 트랜잭션 처리하기
# 오토 커밋 옵션 활성화 확인
# @@autocommit  1 활성화 0 비활성화
select @@autocommit;

# 오토 커밋 설정 set autocommit = 0,1
# Query > Auto-Commit Transactions의 체크박스를 해제
set autocommit = 0;
select @@autocommit;

create table emp_tran1 as select * from emp_test;
desc emp_tran1;
alter table emp_tran1 add primary key(emp_no);

create table emp_tran2 as select * from emp_test;
desc emp_tran2;
alter table emp_tran2 add primary key(emp_no);

delete from emp_tran1;
select * from emp_tran1;
commit;
select * from emp_tran1;
rollback;
select * from emp_tran1; #커밋을 먼저 했으니 롤백은 소용 없음 살릴 방법이 없음

#금융상에서는 오토커밋을 꺼놓고 그때 그때 커밋
#데이터를 조회하는 역할정도만 하는 코드인 경우 오토커밋을 켜놓고 편하게 진행 (상황판단이 중요)