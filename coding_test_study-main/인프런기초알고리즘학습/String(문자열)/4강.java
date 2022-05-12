
//단어 뒤집기
// 코드라뷰 스트링 빌더를 사용하거나 직접 뒤집거나 시간복잡도 부분은 별차이는 없다.
import java.util.*;

class Main {
    public ArrayList<String> solution(String[] str, int n) {
        ArrayList<String> answer = new ArrayList<>();

        // 포문으로 직접 뒤집는 방법
        // 시간 126ms
        // for(String x : str){
        // String alpha="";
        // char[] y = x.toCharArray();
        // for(int i=y.length-1;i>0;i--){
        // alpha+=y[i];
        // }
        // answer.add(alpha);
        // }

        // StringBuilder reverse() 함수 사용
        // 시간복123ms
        // for(String x: str){
        // String tmp = new StringBuilder(x).reverse().toString();
        // answer.add(tmp);
        // }
        // stack 활용
        // Stack<String> st = new Stack<String>();
        // for(String s : str){
        //     for(char c:s.toCharArray()){
        //         st.push(String.valueOf(c));
        //     }
        //     while(!st.isEmpty()){
        //         answer.add(e)
        //     }
        // }
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        String[] str = new String[n];
        for (int i = 0; i < n; i++) {
            str[i] = kb.next();
        }
        for (String x : T.solution(str, n)) {
            System.out.println(x);
        }
    }
}