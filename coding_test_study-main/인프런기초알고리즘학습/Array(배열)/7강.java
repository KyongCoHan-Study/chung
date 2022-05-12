
//점수계산
//131ms
import java.util.*;

class Main {
	public int solution(int n, int[] m) {
		int answer = 0;
		int count = 1;
		for (int i = 0; i < n; i++) {
			if (m[i] != 0) {
				answer += count;
				count++;
			} else
				count = 1;
		}
		return answer;
	}

	public static void main(String[] args) {
		Main T = new Main();
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int[] m = new int[n];
		for (int i = 0; i < n; i++) {
			m[i] = kb.nextInt();
		}
		System.out.println(T.solution(n, m));
	}
}