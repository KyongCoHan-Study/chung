
//문자열 압축
//시간 117ms
import java.util.*;

class Main {
    public String solution(String str) {
        String answer = "";
        int count=1;
        char[] c=str.toCharArray();
        for(int i=0;i<str.length();i++){
            if(answer.charAt(i-1)==c[i]){
                count++;
            }
            else if(count!=1){
                answer+=Integer.toString(count);
                count=1;
              	answer+=c[i];

            }
        }
        
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.print(T.solution(str));

    }
}