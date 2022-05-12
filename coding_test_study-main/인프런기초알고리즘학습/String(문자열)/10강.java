
//가장 짧은 문자열 거리
//119ms
import java.util.*;

class Main {
    public int[] solution(String str,char t) {
        int len = str.length();
        int[] answer= new int[len];
      	int num=1000;

		for(int i=0;i<len;i++){
          if(str.charAt(i)==t)num=0;
        answer[i]=num;
          num++
        }
		num=1000;
      	for(int i=len-1;i>=0;i--){
          if(str.charAt(i)==t)num=0;
          if(answer[i]>num)answer[i]=num;
          num++;
        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
      	char t = kb.next().charAt(0);
      for(int i : T.solution(str,t)){  
      System.out.print(i+" ");
      }
    }
}