import string

alphabets = string.ascii_uppercase

# b, c = map(int, input().split())
N, Q = 3 ,10


s = alphabets[0:N]
for i in range(N):
    for j in range(N-1):
        print('? {} {}'.format(s[j], s[j+1]))
        print('\033[2A')
        ans = input()
        if ans == '>':
            ret = '!{}{}'.format()


# for(i=0;i<N;i++) 
# for(j=0;j<N-1;j++){
#     printf("? %c %c\n", s[j], s[j+1]);
#     fflush(stdout);
#     char ans;
#     scanf(" %c", &ans);
#     if(ans == '>') swap(s[j], s[j+1]);
#   }