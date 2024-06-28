#절대값
SELECT ABS(1), ABS(-1);

# 문자열의 길이 츶겅 : LENGTH (문자열);
SELECT LENGTH('mysql');

# 반올림함수
select round(3.1234567, 2);
select round(3.1234567); #뒤에 소수점아래 숫자 미지정시, 정수로 반환

# 숫자형 함수 +, -, *, /, %(나머지) mod, div(몫만 반황)
select 7 / 2;
select 7 % 2; # 나머지 반환
select 7 mod 2; # 나머지 반환
select 7 div 2;

# 올림 ceil, 내림 floor
select ceil(4.5);
select floor(4.5);

# 제곱, 루트, 음수 양수 확인
select power(4, 3); #제곱
select sqrt(3); #루트
select sign(-5); #양수면 1 음수면 -1 반환

# truncate 버림 (단, 소수점아래 몇번째 숫자 미지정시, 작동 안 됨)
select round(2.2345,3), truncate(2.2345,3);
select round(1153.456, -2), truncate(1153.456, -2); #소수점 앞에자리 기준으로 반올림, 버림이 됨
