// BACKJOON #2010 <플러그>
// https://www.acmicpc.net/problem/2010

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(), sum = 1;
        for(int i=0 ; i<n ; i++) {
            sum += sc.nextInt();
        }
        System.out.println("%d",sum-n);
    }
}