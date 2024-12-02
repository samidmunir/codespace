fn main() {
    println!("\nData types -->\n");

    /*
        SCALAR TYPES
     */

    /*
        Types of int
        i8, i16, i32, i64, i128
     */
    let a: i32 = 5;

    /*
        Types of unsigned
        u8, u16, u32, u64, u128
     */
    let b: u8 = 1;

    /*
        Floating-point values
        f32, f64 : (single-precision, double-precision)
     */
    let floating_point: f32 = 3.14;

    /*
        Boolean
        - true/false
        - 0 / 1
     */
    let true_or_false: bool = true;

    /*
        char (character)
     */
    let letter: char = 'S';

    /*
        COMPOUND TYPES
     */

    /*
        Tuples
        - fixed-length sequence of elements that is immutable.
     */
    println!("Tuple (compound type) -->");
    let tup: (i32, bool, char, f32) = (1, true, '$', 3.14);
    println!("tup.0: {}", tup.0);
    println!("tup.1: {}", tup.1);
    println!("tup.2: {}", tup.2);
    println!("tup.3: {}", tup.3);

    /*
        Arrays
        - variable-length sequence of elements that is immutable (same element-type)
     */
    println!("\nArray (compound type) -->");
    let arr: [i32; 5] = [1, 2, 3, 4, 5];
    println!("arr[0]: {}", arr[0]);
    println!("arr[1]: {}", arr[1]);
    println!("arr[2]: {}", arr[2]);
    println!("arr[3]: {}", arr[3]);
    println!("arr[4]: {}", arr[4]);

    /*
        Strings
     */

}