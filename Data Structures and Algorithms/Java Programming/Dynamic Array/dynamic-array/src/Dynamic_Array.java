public class Dynamic_Array {
    private int[] main;
    private int pointer = -1;
    private int capacity;
    private int available;
    private int BYTES_PER_ELEMENT = 4;
    public Dynamic_Array(int initial_capacity) {
        if (initial_capacity <= 0) {
            throw new IllegalArgumentException("Initial capacity must be greater than 0.");
        }
        capacity = initial_capacity;
        main = new int[capacity];
        available = capacity * BYTES_PER_ELEMENT;
    }
}