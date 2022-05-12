//큰 수 출력하기
//125ms
import java.util.*;

class Main {
    public ArrayList<Integer> solution(int[] num, int n) {
        ArrayList<Integer> answer = new ArrayList<>();
      	answer.add(num[0]);
        for (int i=1; i < n; i++) {
            if (num[i] > num[i - 1])
                answer.add(num[i]);
        }
        return answer;

    }

    public static void main(String[] args) {
        Main T = new Main();
        Scanner kb = new Scanner(System.in);
        int n = kb.nextInt();
        int[] num = new int[n];
        for (int i = 0; i < n; i++) {
            num[i] = kb.nextInt();
        }
        for (int x : T.solution(num, n))
            System.out.print(x + " ");

    }
}