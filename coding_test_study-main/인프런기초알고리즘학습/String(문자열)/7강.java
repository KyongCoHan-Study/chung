//회문 문자열
//코드리뷰 charAt을 이용해 직접 비교하는것이 시간복잡도와 코드길이면에서 유리했지만
//스택사용이 가장 오래걸릴것이라는 예상과 달리 배열의 인덱스 값으로 비교하는 방법이 제일
//오래걸렸다. 그 이유는 반복문안에서 증감연산이 두번 들어가서 그런것으로 추측한다.
import java.util.*;

class Main {
    public String solution(String str) {
        String answer = "YES";
        str = str.toLowerCase();
        // 스택사용
        // 시간 121ms
        // Stack<Character> st = new Stack<>();
        // for(char c:str.toCharArray()){
        // st.push(c);
        // }
        // for(char c:str.toCharArray()){
        // if(st.pop()!=c)answer="NO";
        // }
        // charAt 으로 반 나워서 비교
        // 시간 117ms
        // for(int i=0;i<str.length()/2;i++){
        // if(str.charAt(i)!=str.charAt(str.length()-1-i))answer="NO";
        // }
        // 배열의 위치로 직접 비교
        // 시간 130ms
        char[] c = str.toCharArray();
        int lt = 0, rt = str.length() - 1;
        while (lt < rt) {
            if (c[lt] != c[rt]) {
                answer = "NO";
                break;
            }
            lt++;
            rt--;
        }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.println(T.solution(str));

    }
}