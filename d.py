import re

p = re.compile("ca.e") 
# . : 하나의 문자 ab.c abac abbc
# ^ : 문자열의 시작 ^ab abaa abbb
# $ : 문자열의 끝 ab$ abab baab

def print_match(m):
    if m:
        print("m.group():",m.group()) # 일치하는 문자열 반환
        print("m.string:",m.string) # 입력받은 문자열
        print("m.start():",m.start()) # 일치하는 문자열의 시작 index
        print("m.end():",m.end()) # 일치하는 문자열의 끝 index
        print("m.span():",m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭 실패")

# m = p.match("good care") # match : 문자열의 처음부터 일치하는지 확인
# print_match(m)

# m = p.search("careless") # search : 문자열 중에 일치하는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # careless : 일치하는 모든 것을 리스트 형태로 변환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") :  문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 문자열 중에 일치하는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는것 "리스트" 형태로 반환

# 정규식
# . : 하나의 문자 ab.c abac abbc | abaac(x)
# ^ : 문자열의 시작 ^ab abaa abbb | bbaa (x)
# $ : 문자열의 끝 ab$ abab baab | abaa(x)