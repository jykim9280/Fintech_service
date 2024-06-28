# 문자형 함수
# 문자의 길이를 알아보는 함수
# char_length : 문자의 길이, length: 바이트만 세어줌
select char_length('sql'), length('sql'), char_length('홍길동'), length('홍길동');

# 문자를 연결하는 함수
select concat('this', 'is', 'MySQL') as concat1;
select concat('this', null, 'MySQL') as concat2;
select concat_ws('vs','this', 'is', 'MySQL') as concat3; #사이에 들어갈 것을 첫번째에 두고 지정.

#대문자를 소문자로, 소문자를 대문자로
select lower('ABcd');
select upper('ABcd');

# lpad, rpad 문자열의 자릿수를 일정하게 하고 빈 공간을 지정한 문자로 채우기
# lpad(값, 자릿수, 채울문자), rpad(값, 자릿수, 채울문자), 레프트 라잇트~~
select lpad('SQL', 7, '#');
select lpad('SQL', 7, '$');
select rpad('SQL', 7, '#');
select rpad('SQL', 7, '$');

# 공백을 없애는 함수.
# ltrim(문자열), rtrim(문자열)
select ltrim('         SQL     ');
select rtrim('             SQL          ');

# 문자열의 공백을 앞 뒤로 삭제하는 trim()
select trim('          mysql             ');
select trim(leading '*' from '***mysql***');
select trim(trailing '*' from '***mysql***');
select trim(both '*' from '***mysql***');

# 문자열을 잘라내는 함수 left(문자열, 길이), right(문자열, 길이)
select left('this is my sql', 4), right('this is my sql', 4);

# 문자열의 중간에서 잘라내는 함수 subster(문자열, 시작위치, 길이)
select substr('this is mysql', 6, 2);
select substr('this is mysql', 6); #길이 부분을 생략하면 시작위치 이후 모두

# 날짜형 함수 (시장의 동향은 모두 시계열이므로 잘 알아두어야 함, 파이썬이나 sql 좀 비슷~~)
select curdate(); # 현재 년월일
select current_date(); # curdate()와 동일
select now(); # 현재 년월일 + 시분초 , 얘로 쓰자!
select current_timestamp(); # 현재 년월일 + 시분초

# 요일 표시 함수 dayname(날짜)
select dayname(now());

# 몇 번째 일인지 dayofweek(날짜) 일(1) ... 토(7)
select dayofweek(now());

# 1년 중 오늘이 며칠째인지 dayofyear(날짜)
select dayofyear(now());

# 날짜를 세분화해서 보는 함수들
# 현재 달의 마지막 날이 며칠까지 있는지 출력
select last_day(now());
select last_day('2024-04-20');
#입력한 날짜에서 연도만 추출
select year(now());
#입력한 날짜에서 월만 추출
select month(now());
#입력한 날짜에서 분기만 추출
select quarter(now());
#입력한 날짜가 몇 주차인지
select weekofyear(now());
#날짜와 시간이 같이 있는 데이터에서 날짜와 시간을 구분해 주는 함수
select date('2024-06-27 17:23:30');
select time('2024-06-27 17:23:30');

#날짜를 지정한 수만큼 더하는 함수 date_add(날짜, interval 더할 일 수 day)
select date_add(now(), interval 5 day);
select adddate(now(), 5); #위와 같음
#날짜를 지정한 수만큼 빼는 함수 subdate(날짜, interval 뺄 일 수 day),  subdate(날짜, 뺄 일 수)
select subdate(now(), 5);

#날짜와 시간을 년월, 일시간, 분초 단위로 추출하는 함수
#extract(옵션, from 날짜시간)
select extract(year_month from now());
select extract(day_hour from '2024-06-27 17:23:30');
select extract(minute_second from '2024-06-27 17:23:30');

# 날짜 포맷 함수 지정한 형식에 맞춰서 출력해주는 함수
# %Y 4자리 연도, %y 2자리 연도
# %m 2자리 월 표기, %M 월의 영문 표기, %b 월의 축약 표기 Jan
# %d 2자리 일 표기, %e 1자리 일 표기
select date_format(now(), '%d-%b-%Y');