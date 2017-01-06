import java.util.Scanner;

public class hamming_distance {
    
	public int hammingDistance(int x, int y) {
        int ham_dis;
        int z = x ^ y; 
        for(ham_dis=0; z!=0; z=z>>1){
        	if(z%2 != 0) ham_dis++;
        }
        return ham_dis;
    }
	
	public static void main(String[] args) {
		int x1, x2;
		hamming_distance hd1 = new hamming_distance();
		Scanner sc1 = new Scanner(System.in);
		
		System.out.println("input two integers:");
		x1 = sc1.nextInt();
		x2 = sc1.nextInt();
		System.out.printf("hamming distance is: %d", hd1.hammingDistance(x1, x2));
		sc1.close();
	}

}
