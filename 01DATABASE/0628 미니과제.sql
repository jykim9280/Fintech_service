create database naverDB;
create table member 
(아이디 char(8) not null primary key,
이름 varchar(10) not null,
인원 tinyint not null,
주소 char(2) not null,
국번 char(3) null,
전화번호 char(8) null,
평균키 tinyint UNSIGNED null,
데뷔일자 DATE null
);

create table buy
(순번 int AUTO_INCREMENT not null primary key,
아이디 char(8) not null,
물품명 char(6) not null,
분류 char(4) null,
단가 int UNSIGNED not null,
수량 smallint UNSIGNED not null,
FOREIGN KEY(아이디) REFERENCES member(아이디)
);

desc MEMBER;
SELECT * FROM MEMBER;
insert into `member`
values
('TWC', '트와이스', 9, '서울', '02', '11111111', 167, '2015.10.19'),
('BLK', '블랙핑크', 4, '경남', '055', '22222222', 163, '2016.08.08'),
('WMN', '여자친구', 6, '경기', '031', '33333333', 166, '2015.01.15'),
('OMY', '오바이걸', 7, '서울', null, null, 160, '2015.04.21'),
('GRL', '소녀시대', 8, '서울', '02', '44444444', 168, '2007.08.02'),
('ITZ', '잇지', 5, '경남', null, null, 167, '2019.02.12'),
('RED', '레드벨벳', 4, '경북', '054', '55555555', 161, '2014.08.01'),
('APN', '에이핑크', 6, '경기', '031', '77777777', 164, '2011.02.10'),
('SPC', '우주소녀', 13, '서울', '02', '88888888', 162, '2016.02.25'),
('MMU', '마마무', 4, '전남', '061', '99999999', 165, '2014.06.19');

desc buy;
insert into `buy` (아이디, 물품명, 분류, 단가, 수량) #오토인크리먼트 설정했을 때에는 나머지 컬럼명을 써줘야 함
values
('BLK', '지갑', null, 30, 2),
('BLK', '맥북프로', '디지털', 1000, 1),
('APN', '아이폰', '디지털', 200, 1),
('MMU', '아이폰', '디지털', 200, 5),
('BLK', '청바지', '패션', 50, 3),
('MMU', '에어팟', '디지털', 80, 10),
('GRL', '혼공SQL', '서적', 15, 5),
('APN', '혼공SQL', '서적', 15, 2),
('APN', '청바지', '패션', 50, 1),
('MMU', '지갑', null, 30, 1),
('APN', '혼공SQL', '서적', 15, 1),
('MMU', '지갑', null, 30, 4);

select * from member;

# join할 때 원래 겹치는 정보가 있으면 합쳐짐, 근데 왜 FK 를 사용할까?
# 바로 '참조 무결성' 때문.
# MEMBER의 아이디에 해당하면 정보를 받아들이고, 아이디에 없다면 받아들이지 않음

# member와 buy를 inner join

select * from member as m
inner join buy as b
on m.아이디 = b.아이디;

# 서브쿼리
# 쿼리 안에 또 다른 쿼리를 이용해서 원하는 데이터를 조회
# 이름이 에이핑크인 회원의 평균키보다 큰 회원을 조회하기

select 이름, 평균키 from member
where 평균키 > (select 평균키 from member where 이름 = '에이핑크');

# 코드가 길어지면 복잡해짐. 조심해야 함


