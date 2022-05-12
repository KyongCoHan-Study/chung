
//뒤집은 소수
//122ms
import java.util.*;

class Main {
	public ArrayList<Integer> solution(int n, int[] m) {
		ArrayList<Integer> answer = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			int tmp = 0;
			while (m[i]>0) {
				int t=m[i]%10;
				tmp=tmp*10+t;
				m[i]=m[i]/10;
			}
			tmp += m[i];
			if (tf(tmp)) {
				answer.add(tmp);
			}
		}
		return answer;
	}

	public boolean tf(int n) {
		if(n==1)return false;
		for (int i = 2; i <= n / 2; i++) {
			if (n % i == 0)
				return false;
		}
		return true;

	}

	public static void main(String[] args) {
		Main T = new Main();
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int[] m = new int[n];
		for (int i = 0; i < n; i++) {
			m[i] = kb.nextInt();
		}
		for (int x : T.solution(n, m))
			System.out.print(x+" ");
	}
}