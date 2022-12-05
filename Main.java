public class Main {


/* Primitive data types in Java 
 * byte - whole numbers from -128 too 127 
 * short - whole numbers from -32,768 to 32,767
 * int - whole numbers from ... lets just use this
 */





    public static void main(String[] args){
        String name = "Subin";
        System.out.println("Hello "+name);
        
        String firstName = "Subin ";
        String lastName = "Saji";
        String fullName = firstName + lastName;
        System.out.println(fullName);

        int x = 5, y = 6, z = 9;
        System.out.println(x+y+z); // print value of x + y

        byte myNum = 100;
        System.out.println(myNum);


        float f1 = 35e3f ;
        double d1 = 12E4d ; 
        System.out.println(f1);
        System.out.println(d1);

        boolean isJavaFun = true;
        boolean isFishTasty = false;

        System.out.println(isJavaFun);
        System.out.println(isFishTasty);

        char myGrade = 'B';
        System.out.println(myGrade);

        // Using ASCII

        char myVar1 = 65, myVar2 = 66, myVar3 = 67;
        System.out.println(myVar1);
        System.out.println(myVar2);
        System.out.println(myVar3);




        /* Non-Primitive Data Types
         * Main difference between primitive and noon-primitive data types are:
         * 
         * - primitive data types are predefined in Java. Non primitive typed are created by the programmer
         * - non primitive data types can be null
         * - Primitive type starts with lower case
         * 
         * 
         * 
         */

         // Castings - Wide

         int myInt = 9;
         double myDouble = myInt; // automatic casting from int to double

         System.out.println(myInt);
         System.out.println(myDouble);
         
        
         // Castings - Narrow
         double myDouble1 = 9.78d;
         int myInt1 = (int)myDouble;

         System.out.println(myDouble1);
         































    
    












    }
}