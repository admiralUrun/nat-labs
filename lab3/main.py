from Until import TwoDimensionalArray

def main():
    rows, cols = 5, 5
    array_obj = TwoDimensionalArray(rows, cols)

    array_obj.fill_random()

    print("Оригінал:")
    array_obj.print_array()

    avg_positive, avg_negative = array_obj.average_positive_negative()
    print(f"\nсередньоарифметичне негативних та позитивних: {avg_negative} ||| {avg_positive}")

    print("\nІнший  масив (element - avg_positive):")
    array_obj.print_difference_array()

if __name__ == "__main__":
    main()
