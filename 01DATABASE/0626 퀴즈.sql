# 1. passenger, ticket, survived 테이블을 조인하고 Survived가 1인 사람들만 찾아서 Name, Age, Sex, Pclass, survived 컬럼을 출력하시오.
select Name, Age, Sex, Pclass, survived
from passenger as p
inner join ticket as t
on p.PassengerId = t.PassengerId
inner join survived as s
on p.PassengerId = s.PassengerId #여기까지 하나의 테이블이 됐다고 생각하면 됨
where survived ='1';

# 2. 1의 결과를 10개만 출력하시오.
select Name, Age, Sex, Pclass, survived
from passenger as p
inner join ticket as t
on p.PassengerId = t.PassengerId
inner join survived as s
on p.PassengerId = s.PassengerId 
where survived ='1' limit 10;

# 3. Passenger 테이블을 기준으로 LEFT JOIN 한 결과에서 
#성별이 여성이면서 Pclass가 1인 사람 중 생존자를 찾아 이름, 성별, Pclass를 표시하시오.
select Name, Sex, Pclass
from passenger as p
left join ticket as t
on p.PassengerId = t.PassengerId
left join survived as s
on p.PassengerId = s.PassengerId
WHERE sex = 'female' and Pclass = 1 and survived = 1;

# 4. 나이가 10세 이상 20세 이하 이면서 Pclass 2인 사람 중 생존자를 표시하시오.
select * from passenger as p
left join ticket as t
on p.PassengerId = t.PassengerId
left join survived as s
on p.PassengerId = s.PassengerId
WHERE Age between 10 and 20 
and Pclass = 2
and survived = 1;

# 5. 성별이 여성 또는 Pclass 가 1인 사람 중 생존자를 표시하시오.
select * from passenger as p
left join ticket as t
on p.PassengerId = t.PassengerId
left join survived as s
on p.PassengerId = s.PassengerId
WHERE (sex = 'female' or Pclass = 1) and survived = 1;

# 6
select Name, Pclass, Age, Parch, Survived from passenger as p
left join ticket as t
on p.PassengerId = t.PassengerId
left join survived as s
on p.PassengerId = s.PassengerId
where survived = 1 and name like '%Mrs%';

# 7.
SELECT Name, Sex, Age from passenger as p
left join ticket as t on p.PassengerId = t.passengerId
left join survived as s on p.PassengerId = s.PassengerId
where Pclass in (1,2) and Embarked in ('s','c')
and survived = 1;

# 8.
SELECT Name, Sex, Age from passenger as p
left join ticket as t on p.PassengerId = t.passengerId
left join survived as s on p.PassengerId = s.PassengerId
where name like '%James%' and survived = 1
order by Age DESC;

# 9.
SELECT sex, count(Survived) as Total from passenger as p
inner join ticket as t on p.PassengerId = t.passengerId
inner join survived as s on p.PassengerId = s.PassengerId
where survived = 1 Group by Sex;

# 10.
SELECT sex, count(Survived) as Total, avg(AGE) from passenger as p
inner join ticket as t on p.PassengerId = t.passengerId
inner join survived as s on p.PassengerId = s.PassengerId
where survived = 1 Group by Sex;
