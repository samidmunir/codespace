public class Dynamic_Array {
    private int[] main;
    private int pointer = -1;
    private int capacity;
    private int used = 0;
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
            used = 0 * BYTES_PER_ELEMENT;
            available = (capacity - used) * BYTES_PER_ELEMENT;
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
        System.out.println("\tSuccessfully created new Dynamic_Array object.");
        print_data_structure_dynamic_array();
    }

    private void print_data_structure_stats() {
        System.out.println("\t\tpointer: " + pointer);
        System.out.println("\t\tcapacity: " + capacity);
        System.out.println("\t\tused: " + (used * BYTES_PER_ELEMENT) + " bytes");
        System.out.println("\t\tavailable: " + (available * BYTES_PER_ELEMENT) + " bytes / " + (capacity * BYTES_PER_ELEMENT) + " bytes");
    }

    private void print_data_structure_dynamic_array() {
        System.out.println("main[]:");
        if (is_null() || is_empty()) {
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
            return false;
        }
    }

    private boolean is_full() {
        if (main != null && pointer == capacity - 1) {
            return true;
        } else {
            return false;
        }
    }

    /*
     * function insert_head(int data):
     * - CASE 1: inserting in empty array.
     * - CASE 2: inserting in non-empty array with one element (one shift to the right).
     * - CASE 3: inserting in non-empty array with more than one element (shift to the right n times).
     * - CASE 4: array is at maximum capacity... resizing needed.
     */
    public void insert_head(int data) {
        System.out.println("\nDynamic_Array.insert_head(" + data + ") called...");
        if (is_null()) {
            System.out.println("\tERROR: cannot insert into null dynamic array.");
            print_data_structure_dynamic_array();
            return;
        } else {
            if (is_empty()) {
                pointer++;
                main[pointer] = data;
                used++;
                available = capacity - used;
            } else if (!is_empty() && !is_full()) {
                pointer++;
                for (int i = pointer; i > 0; i--) {
                    main[i] = main[i - 1];
                }
                main[0] = data;                
                used++;
                available = capacity - used;
            } else {
                pointer++;
                int new_capacity = (capacity / 2) + capacity;
                System.out.println("\tResizing dynamic array[" + capacity + "] -> [" + new_capacity + "]");
                int[] new_main = new int[new_capacity];
                for (int i = 0; i < pointer; i++) {
                    new_main[i + 1] = main[i];
                }
                new_main[0] = data;
                main = new_main;
                capacity = new_capacity;
                used++;
                available = capacity - used;
            }
        }
        System.out.println("\tSuccessfully inserted " + data + " at head of the dynamic array.");
        print_data_structure_dynamic_array();
    }
}