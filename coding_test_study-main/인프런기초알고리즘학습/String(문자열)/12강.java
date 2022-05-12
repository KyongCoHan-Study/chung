
//암호
//시간 117ms
import java.util.*;

class Main {
    public String solution(String str, int x) {
        String answer = "";
        str=str.replace("#", "1").replace("*", "0");
        int i = 0;
        char c;
        for (int a = 0; a < str.length() / 7; a++) {
            for (int j = 0; j < 7; j++) {
                String tmp = str.substring(0, 7);
                str = str.substring(7);
                i = Integer.parseInt(tmp,2);
                c = (char) i;
                answer += c;
            }
        }
        return answer;

    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int i = kb.nextInt();

        String str = kb.nextLine();

        System.out.print(T.solution(str, i));

    }
}