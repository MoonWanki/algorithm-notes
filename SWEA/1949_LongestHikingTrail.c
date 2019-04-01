// SWEA #1949 [모의 SW 역량테스트] 등산로 조성

N, K;
dfs(int i, int j, int** arr, int worked, int**visited, int length) {
    // printf("[Stage %d] Searching %d,%d (%d)...\n", length, i, j, arr[i][j]);
    visited[i][j] = 1;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};
    int maxLength = length;
    for(int t=0 ; t<4 ; t++) {
        int nx = i+dx[t], ny = j+dy[t];
        if(nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if(!visited[nx][ny]) {
                if(arr[nx][ny] < arr[i][j]) {
                    // printf("%d,%d (%d) looks good.\n", nx, ny, arr[nx][ny]);
                    int l = dfs(nx, ny, arr, worked, visited, length+1);
                    if(maxLength < l) {
                        maxLength = l;
                    }
                }
                else if(!worked) {
                    int minDig = arr[nx][ny] - arr[i][j] + 1;
                    worked = 1;
                    for(int s=minDig ; s<=K ; s++) {
                        arr[nx][ny]-=s;
                        // printf("%d,%d (%d) looks good. Let me dig down by %d\n", nx, ny, arr[nx][ny], s);
                        int l = dfs(nx, ny, arr, worked, visited, length+1);
                        if(maxLength < l) {
                            maxLength = l;
                        }
                        arr[nx][ny]+=s;
                    }
                    worked = 0;
                }
            }
        }
    }
    visited[i][j] = 0;
    return maxLength;
}

main(t) {
    scanf("%d",&t);
    for(int tt=1 ; tt<=t ; tt++) {
        scanf("%d %d", &N, &K);
        int** arr = (int**)malloc(sizeof(int*)*N);
        int** visited = (int**)malloc(sizeof(int*)*N);
        for(int i=0 ; i<N ; i++) {
            arr[i] = (int*)malloc(sizeof(int)*N);
            visited[i] = (int*)malloc(sizeof(int)*N);
        }
        int maxI=0, maxJ=0;
        for(int i=0 ; i<N ; i++) {
            for(int j=0 ; j<N ; j++) {
                scanf("%d", &arr[i][j]);
                visited[i][j] = 0;
                if(arr[i][j] > arr[maxI][maxJ]) {
                    maxI=i; maxJ=j;
                }
            }
        }
        int maxLength = 0;
        for(int i=0 ; i<N ; i++) {
            for(int j=0 ; j<N ; j++) {
                if(arr[i][j]==arr[maxI][maxJ]) {
                    int length = dfs(i, j, arr, 0, visited, 1);
                    if(length > maxLength) {
                        maxLength = length;
                    }
                }
            }
        }
        printf("#%d %d\n", tt, maxLength);
    }
}