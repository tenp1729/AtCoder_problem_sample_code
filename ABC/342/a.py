#   前後で異なるところを見つけ最初の場合だけ気を付ける
import sys

s = input()
for i in range(len(s)-1):
    if s[i+1] != s[i]:
        if i == 0 and s[1] == s[2]:
            print(1)
            sys.exit()
        print(i+2)
        sys.exit()
