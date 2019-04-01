// SWEA #1953 [모의 SW 역량테스트] 탈주범 검거
N,M,R,C,L;
dfs(int i, int j, int left, int** arr, int** visited, int** check) {
    if(left==0) return;
    // printf("[%d left] Searching %d,%d (%d)...\n", left, i, j, arr[i][j]);
    visited[i][j] = 1;
    check[i][j] = 1;
    int dx[4] = {-1, 1, 0, 0};
    int dy[4] = {0, 0, -1, 1};

    int pt = arr[i][j];

    int nx = i+dx[0], ny = j+dy[0];
    if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
        int npt = arr[nx][ny];
        if(!visited[nx][ny]
        && (pt==1 || pt==2 || pt==4 || pt==7)
        && (npt==1 || npt==2 || npt==5 || npt==6)) {
            // printf("%d,%d (%d) looks good.\n", nx, ny, arr[nx][ny]);
            dfs(nx, ny, left-1, arr, visited, check);
        }
    }
    nx = i+dx[1], ny = j+dy[1];
    if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
        int npt = arr[nx][ny];
        if(!visited[nx][ny]
        && (pt==1 || pt==2 || pt==5 || pt==6)
        && (npt==1 || npt==2 || npt==4 || npt==7)) {
            // printf("%d,%d (%d) looks good.\n", nx, ny, arr[nx][ny]);
            dfs(nx, ny, left-1, arr, visited, check);
        }
    }
    nx = i+dx[2], ny = j+dy[2];
    if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
        int npt = arr[nx][ny];
        if(!visited[nx][ny]
        && (pt==1 || pt==3 || pt==6 || pt==7)
        && (npt==1 || npt==3 || npt==4 || npt==5)) {
            // printf("%d,%d (%d) looks good.\n", nx, ny, arr[nx][ny]);
            dfs(nx, ny, left-1, arr, visited, check);
        }
    }
    nx = i+dx[3], ny = j+dy[3];
    if(nx >= 0 && nx < N && ny >= 0 && ny < M) {
        int npt = arr[nx][ny];
        if(!visited[nx][ny]
        && (pt==1 || pt==3 || pt==4 || pt==5)
        && (npt==1 || npt==3 || npt==6 || npt==7)) {
            // printf("%d,%d (%d) looks good.\n", nx, ny, arr[nx][ny]);
            dfs(nx, ny, left-1, arr, visited, check);
        }
    }
    visited[i][j] = 0;
}
main(T) {
    scanf("%d", &T);

    for(int t=1 ; t<=T ; t++) {
        scanf("%d%d%d%d%d", &N, &M, &R, &C, &L);
        int** arr = (int**)malloc(sizeof(int*)*N);
        int** visited = (int**)malloc(sizeof(int*)*N);
        int** check = (int**)malloc(sizeof(int*)*N);
        for(int i=0 ; i<N ; i++) {
            arr[i] = (int*)malloc(sizeof(int)*M);
            visited[i] = (int*)malloc(sizeof(int)*M);
            check[i] = (int*)malloc(sizeof(int)*M);
        }
        for(int i=0 ; i<N ; i++) {
            for(int j=0 ; j<M ; j++) {
                scanf("%d", &arr[i][j]);
                visited[i][j] = 0;
                check[i][j] = 0;
            }
        }
        dfs(R,C,L,arr,visited, check);

        int count=0;
        for(int i=0 ; i<N ; i++) {
            for(int j=0 ; j<M ; j++) {
                if(check[i][j]) count++;
            }
        }

        printf("#%d %d\n", t, count);
    }
}