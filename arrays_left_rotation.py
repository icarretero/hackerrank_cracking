def array_left_rotation(a, n, k):
    return [a[(i+k)%n] for i in range(n)]
  

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
