// BACKJOON #10250 <ACM Hotel>
// https://www.acmicpc.net/problem/10250

main(t,h,w,n){for(scanf("%d",&t);t-->0;printf("%d\n",((n-1)%h+1)*100+(n-1)/h+1))scanf("%d%d%d",&h,&w,&n);}