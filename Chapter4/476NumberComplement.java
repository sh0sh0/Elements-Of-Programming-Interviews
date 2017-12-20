//This is a problem from Leetcode, no 476

/*
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
*/

//example: input = 5, out = 2

public class NumberComplement{
  public static int findComplement(int num){
    int n = 0;
  
    while (n < num) {
      n = (n << 1) | 1;
    }
    return n - num;
  }
  
  public static void main(String[] args){
  long fc = findComplement(5);
  System.out.println(fc);
  }
}
