//알파벳만 뒤집기
//시간 133ms
import java.util.*;

class Main {
    public String solution(String str) {
        String answer;
        char[] c = str.toCharArray();
        int lt = 0;
        int rt = str.length() - 1;
        while (lt < rt) {
            if (!Character.isAlphabetic(c[lt]))
                lt++;
            else if (!Character.isAlphabetic(c[rt]))
                rt--;
            else {
                char tmp = c[lt];
                c[lt] = c[rt];
                c[rt] = tmp;
                lt++;
                rt--;
            }
        }
        answer = String.valueOf(c);
        return answer;
    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        String str = kb.next();
        System.out.println(T.solution(str));

    }
}