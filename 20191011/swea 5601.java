import java.util.*;
public class Solution {
	static Scanner sc  = new Scanner(System.in);
	public static void main(String[] args) {
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			StringBuilder sb = new StringBuilder();
			for(int i=0; i<N; i++) {
				sb.append(" 1/");
				sb.append(N);
			}
			System.out.format("#%d%s\n", tc, sb);
		}
	}
}