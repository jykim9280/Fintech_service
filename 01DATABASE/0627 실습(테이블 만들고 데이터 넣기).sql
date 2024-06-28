use world;
show tables;

describe city;
desc country;
desc countrylanguage;

select * from city;
select countrycode, name, id from city; #원래 테이블은 그대로이고, 불러오는 순서대로

select * from city;
select * from mywork.highschool_students;

# where
select * from city where countrycode = 'KOR';
select * from city where countrycode = 'KOR' and district like '%ong%';
# district 'seoul', 'kyonggi' in 사용
select * from city where countrycode = 'KOR' and district in ('seoul', 'kyonggi');
# country 테이블에서 population이 1억 초과인 나라를 찾기
select * from country where population > 100000000;
# 우리나라 인구 찾기
select * from country where name = 'south korea';

# 우리나라 인구와 비슷한 나라 찾기
select * from country where population between 45000000 and 55000000;


# 박스 오피스 데이터 조회
use mywork;
desc box_office;
select * from box_office limit 5;

select distinct rep_country from box_office;
select * from box_office where rep_country = '한국' and release_date between '2018-01-01' and '2018-12-31';

# 2019년에 개봉한 영화중 관객이 audiunce_num이 1000만 이상인 영화
select * from box_office where release_date between '2019-01-01' and '2019-12-31' and audience_num >= 10000000;

# order by로 정렬하기
# world country 테이블에서 인구가 1억을 초과하는 나라를 추출하고 인구순으로 내림차순
select * from world.country where population > 100000000 order by Population desc;

# 조회된 데이터를 2개 컬럼을 기준으로 정렬하기
# 인구수가 5000만명 이상인 나라를 찾아서 계급별 continent, region 을 기준으로 오름차순 정렬
select * from world.country where population >= 50000000 order by continent, region asc; #(asc 를 안 붙여도 오름차순)
