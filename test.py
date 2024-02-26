// ax + by = gcd (a, b)
// When finding gcd you do a mod m and b mod m and the result, aka the remainder, is the r0, r1,...rk+1, and r0 = a and r1 = b
// gcd(a,b) = rk = a*sk + b*tk
// ax + by
// Take user input for modulus m and k
// check for k being positive and less than m
// the program prints k mod m if it exists
// the gcd of k and m has to be equal to 1 to exist.
// It doesn't exist if it is not equal to 1, and it prints "the inverse doesn't exist"
import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.print("Enter value of k: ");
    long k = input.nextLong();
    System.out.print("Enter value of m: ");
    long m = input.nextLong();
    while (k <= 0 || k >= m) {
      System.out.println ("\nThat is an invalid value for k. Please enter a positive value less than m.");
      System.out.print("Enter value of k: ");
      k = input.nextLong ();
    }
    while (m <= 0) {
      System.out.println ("\nThat is an invalid value for m. Please enter a positive value.");
      System.out.print("Enter value of m: ");
      m = input.nextLong ();
    }
    long greatestcd = gcd (k, m);
    System.out.println (greatestcd);
    if (greatestcd != 1) {
      System.out.println ("\nThe inverse doesn't exist.");
      return;
    }
    System.out.println ("\nThe greatest common divisor of k and m is " + greatestcd + ".");
    System.out.println ("The multiplicative inverse of k mod m is " + inverse (k, m) + ".");
    // m / k = quotient (when integer division occurs and the quotient is truncated.)
    // m / k = qq2
    // m % k = rr1
    // k / rr1 = qq2
    // k % qq2 = rr2
    System.out.println (m + " mod " + k + " = " + (m % k));
  }
  public static long gcd (long k, long m) {
    long quotient = m / k; // 1
    long remainder = m % k; // 2
    if (remainder == 0) {
      return k;
    }
    if (k % remainder == 0) { // This base case checks if the next remainder is 0, and it it is then it returns the remainder calculated before it.
      return remainder;
    }
    // m = k --> k is remainder of previous values.
    // m / k
    return gcd (remainder, k);
  }
  public static long inverse (long k, long m) {
    long t = 0;
    long r = m;
    long newt = 1;
    long newr = k;
    while (newr != 0) {
      long quotient = r / newr;
      long container1 = newt; // This is used so that the different variables are not depending on each other. They need to be assigned in parallel.
      long container2 = newr;
      newt = t - quotient * newt;
      t = container1;
      newr = r - quotient * newr;
      r = container2;
    }
    if (r > 1) {
      System.out.println ("The value of k is not invertible.");
    }
    if (t < 0) {
      t = t + m;
    }
    return t;
  }
}