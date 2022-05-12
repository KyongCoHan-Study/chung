
import java.util.*;

//대소문자 변환 문제
//코드 최종 리뷰 함수>ascii>xor 비트연산 순으로 시간복잡도가 낮았으며 
//함수와 비교연산자는 약 10ms 차이로 유의미한 차이를 보여줬다
//많은 참조가 이뤄지고 팀의 수준이 높다면 비트연산자를
//많은 수정이 이뤄지고 적은 참조가 있다면 if 연산자를 활용하는 것이 좋을거같다
class Main{
    public String solution(String str){
        String answer="";
        //함수활용
        //시간 123ms
        // for(char x : str.toCharArray()){
        //     if(Character.isLowerCase(x)) answer+=Character.toUpperCase(x);
        //   	else answer+=Character.toLowerCase(x);
        // }
        //ascii 값활용
        //시간 121ms
        // for(char x : str.toCharArray()){
        //     if(x>65&&x<92)answer+=(char)(x+32);
        //     else answer+=(char)(x-32);
        // }
        //xor 연산
        //시간 114ms
        for(char x : str.toCharArray()){
            answer+=(char)(x^32);
        }
        return answer;
    }

public static void main(String[] args){
    Main T= new Main();
    Scanner kb = new Scanner(System.in);

    String str=kb.next();
     System.out.print(T.solution(str));
    }
}
