public class Dynamic_Array {
    private int[] main;
    private int pointer = -1;
    private int capacity;
    private int available;
    private int BYTES_PER_ELEMENT = 4;
    public Dynamic_Array(int initial_capacity) {
        System.out.println("\nDynamic_Array.Dynamic_Array() called...");
        try {
            Thread.sleep(1500);
            System.out.println("\ttrying to create new Dynamic_Array object.");
            if (initial_capacity <= 0) {
                throw new IllegalArgumentException("Initial capacity must be greater than 0.");
            }
            capacity = initial_capacity;
            main = new int[capacity];
            available = capacity * BYTES_PER_ELEMENT;
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
        System.out.println("\tSuccessfully created new Dynamic_Array object.");
        print_data_structure_dynamic_array();
    }

    private void print_data_structure_stats() {
        System.out.println("\t\tpointer: " + pointer);
        System.out.println("\t\tcapacity: " + capacity);
        System.out.println("\t\tavailable: " + available + " bytes");
    }

    private void print_data_structure_dynamic_array() {
        System.out.println("main[]:");
        if (main == null || capacity == 0 || main.length == 0) {
            System.out.println("\tEMPTY ARRAY main[]: []");
            print_data_structure_stats();
            return;
        }
        System.out.print("\t[");
        for (int i = 0; i < main.length; i++) {
            System.out.print(main[i] + ", ");
        }
        System.out.print("\b\b]\n");
        print_data_structure_stats();
    }

    private boolean is_null() {
        if (main == null) {
            return true;
        } else {
            return false;
        }
    }

    private boolean is_empty() {
        if (main != null && pointer == -1) {
            return true;
        } else {
            return false;}
    }

    private boolean is_full() {
        if (main != null && pointer == capacity - 1) {
            return true;
        } else {
            return false;
        }
    }
}