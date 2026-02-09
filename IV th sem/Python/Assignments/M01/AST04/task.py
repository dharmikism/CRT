def Reverse_String(s: str) -> str:
   S=""
   s=list(s)
   for i in range(len(s)-1,-1,-1):
       S+=s[i]
   return S

if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
