print(
   any(
       map(
           lambda x: int(x) == 0,
           open('input.txt').read().split()
       )
   )
)
