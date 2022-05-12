//숫자만 추출
//시간 117ms
import java.util.*;

class Main {
    public int solution(String str) {
        int answer = 0;
        str = str.toUpperCase().replaceAll("[^0-9]", "");
        answer= Integer.parseInt(str);

        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.nextLine();
        System.out.println(T.solution(str));

    }
}