// BACKJOON #1074 <Z>
// https://www.acmicpc.net/problem/1074

r,c,x;
main(N){
    scanf("%d%d%d",&N,&r,&c);
    f(0,(int)pow(2,N),0,(int)pow(2,N));
}
f(r1,r2,c1,c2){
    if(r2-r1==2){
        if(r==r1&&c==c1)printf("%d",x);
        else if(r==r1&&c==c2-1)printf("%d",x+1);
        else if(r==r2-1&&c==c1)printf("%d",x+2);
        else if(r==r2-1&&c==c2-1)printf("%d",x+3);
        x+=4;
    }else{
        f(r1,(r1+r2)/2,c1,(c1+c2)/2);
        f(r1,(r1+r2)/2,(c1+c2)/2,c2);
        f((r1+r2)/2,r2,c1,(c1+c2)/2);
        f((r1+r2)/2,r2,(c1+c2)/2,c2);
    }
}