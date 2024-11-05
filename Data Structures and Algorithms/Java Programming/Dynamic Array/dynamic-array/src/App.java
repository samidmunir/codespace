public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("\nDynamic Array - Java Implementation");
        System.out.println("Data Structures & Algorithms");
        System.out.println("-----------------------------------\n");

        /*
         * Testing Dynamic_Array object initialization.
         */
        Dynamic_Array d_array = new Dynamic_Array(4);

        /*
         * Testing function insert_head()
         */
        d_array.insert_head(2);
        d_array.insert_head(11);
        d_array.insert_head(64);
        d_array.insert_head(9);
        d_array.insert_head(35); // resize required.
        d_array.insert_head(-8);
        d_array.insert_head(73); // resize required.
    }
}
