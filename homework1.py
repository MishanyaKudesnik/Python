gor1 = int(input())
wer1 = int(input())
gor2 = int(input())
wer2 = int(input())
if (gor2>gor1 and wer2 > wer1) and (gor1 + (abs(gor2-gor1)) and wer1 + (abs(wer2-wer1))) or (gor1>gor2 and wer1 > wer2) and (gor1 - (abs(gor2-gor1)) and wer1 - (abs(wer2-wer1)))      or (gor2>gor1 and wer1 > wer2) and (gor1 + (abs(gor2-gor1)) and wer1 - (abs(wer2-wer1))) or (gor1>gor2 and wer2 > wer1) and (gor1 - (abs(gor2-gor1)) and wer1 + (abs(wer2-wer1))):
  print("YES")
else:
  print("NO")
  
