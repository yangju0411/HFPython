from sanitize import sanitize
#분을 초로 변환
mins = [1,2,3]
secs = [m * 60 for m in mins]
print(secs)
#미터를 피트로 변환
meters = [1,10,3]
feets = [m * 3.281 for m in meters]
print(feets)
#대문자와 소문자가 섞인 리스트를 대문자로 모두 변환
lower = ['I', 'don\'t', 'like', 'spam']
upper = [s.upper() for s in lower]
print(upper)
#sanitize로 리스트를 가공
dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)
#원래 리스트에 문자열 리스트를 부동소숫점숫자형(float)로 변환 후 넣어줌
clean = [float(t) for t in clean]
print(clean)
#함수 연속 호출
clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)