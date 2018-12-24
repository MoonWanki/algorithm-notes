// BACKJOON #10815 <숫자 카드>
// https://www.acmicpc.net/problem/10815

N[500000],n,i;

main(){
    for(scanf("%d",&n);i<n;i++)scanf("%d",&N[i]);
    qs(0,n-1);
    for(scanf("%d",&i);~scanf("%d",&i);printf("%d ",bs()));
}

bs(){
    int l=0, r=n-1, m;
    while(l<=r) {
        m=(l+r)/2;
        if(i<N[m]) r=m-1;
        else if(i>N[m]) l=m+1;
        else return 1;
    }
    return 0;
}

qs(l,r){
    int i=l, j=r, m=(l+r)/2, t, p = N[m];
    while(i<=j) {
        while(N[i] < p) i++;
        while(N[j] > p) j--;
        if(i<=j) {
            t = N[i];
            N[i] = N[j];
            N[j] = t;
            i++;
            j--;
        }
    };
    if(l < j) qs(l, j);
    if(i < r) qs(i, r);
}