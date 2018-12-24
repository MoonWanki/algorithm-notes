// BACKJOON #1011 <Fly me to the Alpha Centrauri>
// https://www.acmicpc.net/problem/1011

unsigned int arr[150000], t, from, to, val = 1, term = 1;

int getMinTimes(unsigned int distance) {
    for(int i=1 ; i<140000 ; i++) {
        if(arr[i] > distance) return i-1;
    }
}

int main() {
    for(int i=1 ; i<140000; i+=2) {
        arr[i] = val;
        val += term;
        arr[i+1] = val;
        val += term;
        term++;
    }
    for(scanf("%d", &t) ; t-->0 ;) {
        scanf("%d %d", &from, &to);
        printf("%d\n", getMinTimes(to - from));
    }
}