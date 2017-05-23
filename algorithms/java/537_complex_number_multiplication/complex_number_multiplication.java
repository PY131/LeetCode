import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Peng
 *
 * @Problem_Link 
 *      https://leetcode.com/problems/complex-number-multiplication/#/description
 *      
 * @Problem_Description
 *      calculate the multiplication of complex number.
 *      base on the form of string.
 */
public class complex_number_multiplication {

    /**
     * Solution 1:
     *      using str.split() to get the number by spliting the string 
     * @param a, b, complex number with integer x,y -> x + yi 
     * @return c, String, the multiplication of complex number a and b.
     */
    public static String complexNumberMultiply_1(String a, String b) {
        // split the string
        String[] A = a.split("\\+");
        String[] B = b.split("\\+"); 
        
        // get the number
        int a0 = Integer.parseInt(A[0]);  
        int a1 = Integer.parseInt(A[1].replace("i",""));  
        int b0 = Integer.parseInt(B[0]);  
        int b1 = Integer.parseInt(B[1].replace("i","")); 
        
        // calculate multiplication and form the result string
        // (a0+a1*i)*(b0+b1*i)=(a0*b0-a1*b1)+(a1*b0+a0*b1)*i
        String c = (a0*b0-a1*b1) + "+" + (a1*b0+a0*b1) + "i";
        return c;
    }

    // test code
    public static void main(String[] args) {
        String a = "1+-1i";
        String b = "-1+2i";
        System.out.println(complexNumberMultiply_1(a, b));
    }
}
