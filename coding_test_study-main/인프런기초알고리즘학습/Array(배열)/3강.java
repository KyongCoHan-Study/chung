
//가위 바위 보
//147ms
import java.util.*;

class Main {
    public String[] solution(int[] a,int[] b, int n) {
        String[] answer = new String[n];		
      	for (int i = 0; i < n; i++) {
            if (a[i]==b[i])answer[i]="D";
            else if(a[i]-b[i]==1 || a[i]-b[i]==-2)answer[i]="A";
          	else answer[i]="B";
        }
        return answer;

    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = kb.nextInt();
        }
              int[] b = new int[n];

      for (int i = 0; i < n; i++) {
            b[i] = kb.nextInt();
        }
      for(String s : T.solution(a,b,n))  
      System.out.println(s);

    }
}