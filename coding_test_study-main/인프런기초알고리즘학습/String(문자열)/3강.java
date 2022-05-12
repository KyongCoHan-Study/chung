//문장 속 단어찾기
//코드리뷰 스플릿 메소드를 사용하는것이 약 8ms 시간복잡도가 적었고
//코드의 줄도 짧았다
import java.util.*;

class Main{
    public String solution(String str){
        String answer="";
        int m = Integer.MIN_VALUE, pos;
        //스플릿 메소드 사용 
        //시간 114ms
        String[] s=str.split(" ");
        for(String x : s){
            int len = x.length();
            if(m<len){
                m=len;
                answer=x;
        }
    }
    //IndexOf 사용
    //시간 122ms
    // str+=' ';
    // while((pos=str.indexOf(' '))!=-1){
    //     String tmp=str.substring(0, pos);
    //     int len = tmp.length();
    //     if(len>m){
    //         m=len;
    //         answer=tmp;
    //     }
    //     str=str.substring(pos+1);
    // }

        return answer;
    }

public static void main(String[] args){
    Main T= new Main();
    Scanner kb = new Scanner(System.in);
    String str=kb.nextLine();
     System.out.print(T.solution(str));
    }
}