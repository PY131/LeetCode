import java.util.*;

public class fizz_buzz {

	public List<String> fizzBuzz(int n) {
		List<String> str_list = new ArrayList<String>();
		
		for(int i=1; i<=n; i++){
			if(i%3 != 0 && i%5 != 0)  str_list.add(String.valueOf(i));
			else if(i%3 == 0){
				if(i%5 == 0)  str_list.add("FizzBuzz");
				else str_list.add("Fizz");
			}
			else  str_list.add("Buzz");
		}
		return str_list;
	}
    
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n;
		fizz_buzz hd1 = new fizz_buzz();
		List<String> str1 = new ArrayList<String>();
		Scanner sc1 = new Scanner(System.in);
		
		System.out.println("input:");
		n = sc1.nextInt();
		
		str1 = hd1.fizzBuzz(n);
		for (int i = 0; i < str1.size(); i++){
			System.out.println(str1.get(i));
		}
		sc1.close();
	}
	
}
