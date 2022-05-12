
//뒤집은 소수
//138ms
import java.util.*;

class Main {
    public int[] solution(int n, int[] m) {
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i]=1;
            for(int j=0;j<n;j++){
              if(m[i]<m[j])answer[i]+=1;
            }
        }
        return answer;
    }
    
    

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] m = new int[n];
        for (int i = 0; i < n; i++) {
            m[i] = kb.nextInt();
        }
        for (int x : T.solution(n, m))
            System.out.print(x + " ");
    }
}