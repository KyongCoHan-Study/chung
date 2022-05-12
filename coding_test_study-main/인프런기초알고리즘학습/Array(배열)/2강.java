
//보이는 학생
//610ms
import java.util.*;

class Main {
    public int solution(int[] num, int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(num[0]);
        int x = 0;
        for (int i = 1; i < n; i++) {
            if (num[i] > answer.get(x)) {
                answer.add(num[i]);
                x++;
            }
        }
        return answer.size();

    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] num = new int[n];
        for (int i = 0; i < n; i++) {
            num[i] = kb.nextInt();
        }
        System.out.print(T.solution(num, n));

    }
}