// BACKJOON #1931 <카잉 달력>
// https://www.acmicpc.net/problem/6064

M,N,x,y;
main() {
    for(scanf("%d",&M);~scanf("%d%d%d%d",&M,&N,&x,&y);printf("%d\n",f()));
}
f() {
    if(x==y) return x;
    if(M>N) {
        int t=N; N=M; M=t;
        t=x; x=y; y=t;
    }
    int xyg = y-x;
    for(int i=1,j=1 ; i<=M ; i++) {
        int mng = j-i;
        if(xyg==mng) {

        }
        j+=N;
    }
}