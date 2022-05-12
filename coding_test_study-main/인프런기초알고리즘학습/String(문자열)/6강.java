//중복문자제거
import java.util.*;

class Main {
    public String solution(String str) {
        String answer="";
        for(char c: str.toCharArray()){
            if(answer.indexOf(c)==-1)answer+=c;
        }        
        return answer;
    }
    
    
    

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.println(T.solution(str));

    }
}