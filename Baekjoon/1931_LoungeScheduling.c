// BACKJOON #1931 <회의실 배정>
// https://www.acmicpc.net/problem/1011

unsigned int a[100000][2];
i,x,c;
main(n) {
    for(scanf("%d",&n) ; i<n ; i++) {
        scanf("%u%u",&a[i][0],&a[i][1]);
    }
    qs(0, n-1);
    puts("qs"); for(i=0 ; i<n ; i++) printf("%u %u\n", a[i][0], a[i][1]);
    for(i=0 ; i<n ; i++) {
        if(a[i][0] >= x) {
            c++;
            printf("%d: %u %u\n", c, a[i][0], a[i][1]);
            x = a[i][1];
        }
    }
    printf("%d",c);
}

void qs(int l, int r) {
    int i = l, j = r, m = (l+r)/2;
    unsigned int pv[2] = {a[m][0],a[m][1]};
    do {
        while (a[i][1] < pv[1])
            i++;
        while (a[j][1] > pv[1])
            j--;
        if (i<=j) {
            unsigned int t[2] = {a[i][0], a[i][1]};
            a[i][0] = a[j][0];
            a[i][1] = a[j][1];
            a[j][0] = t[0];
            a[j][1] = t[1];
            i++;
            j--;
        }
    } while(i<=j);
    if(l < j) qs(l, j);
    if(i < r) qs(i, r);
}

// unsigned int s[100000], e[100000], ns[100000], ne[100000], nns[100000], nne[100000];
// b[100000], bc;
// i;max;t;
// main() {
//     for(scanf("%d",&t) ; i<t ; i++) {
//         scanf("%d%d",&s[i],&e[i]);
//     }
//     sort();
//     puts("sorted"); for(int i=0 ; i<t ; i++) printf("%u %u\n", s[i], e[i]);
//     minify();
//     puts("minified"); for(int i=0 ; i<t ; i++) printf("%u %u\n", ns[i], ne[i]);
//     minify2();
//     puts("minified2"); for(int i=0 ; i<t ; i++) printf("%u %u\n", nns[i], nne[i]);
//     greedy(0, 0, 0);
//     printf("%d",max, 0);
// }

// sort() {
//     for(int i=0 ; i<t-1 ; i++) for(int j=0 ; j<t-i-1 ; j++) {
//         if(s[j]>s[j+1]) {
//             int ts = s[j], te = e[j];
//             s[j] = s[j+1]; e[j] = e[j+1];
//             s[j+1] = ts; e[j+1] = te;
//         }
//     }
// }

// minify() {
//     int idx = 0;
//     for(int i=0 ; i<t ; i++) {
//         int j, minE = e[i];
//         for(j=i+1 ; j<t ; j++) {
//             if(s[j] > s[i]) {
//                 break;
//             }
//             else {
//                 if(e[j] < minE) minE = e[j];
//             }
//         }
//         ns[idx] = s[i];
//         ne[idx] = minE;
//         idx++;
//         i=j-1;       
//     }
//     t = idx;
// }

// minify2() {
//     int idx=0;
//     for(int i=0 ; i<t-1 ; i++) {
//         if(ne[i+1] < ne[i]) {
//             b[i] = 1;
//         }
//     }
//     for(int i=0 ; i<t ; i++) {
//         if(b[i]!=1) {
//             nns[idx] = ns[i];
//             nne[idx] = ne[i];
//             idx++;
//         }
//     }
//     t = idx;
// }

// greedy(unsigned int _s, int c, int idx){
//     for( ; idx<t ; idx++) {
//         if(nns[idx]>=_s) {
//             greedy(nne[idx], c+1, idx);
//         }
//     }
//     max = c>max ? c : max;
// }