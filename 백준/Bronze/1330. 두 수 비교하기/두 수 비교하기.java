
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		int a, b;
		Scanner in = new Scanner(System.in);
		
		a = in.nextInt();
		b = in.nextInt();
		
		if(a < b)
		{
			System.out.println("<");
		}
		if(a > b)
		{
			System.out.println(">");
		}
		if(a == b)
		{
			System.out.println("==");
		}
		

	}

}
