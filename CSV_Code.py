import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\24009620\\Downloads\\CSV\\File.csv", index_col="Product")

while True:
    print("1. Lowest to Highest")
    print("2. Highest to Lowest")
    print("3. Highest only")
    print("4. Lowest only")
    print("5. Sum of all")
    print("6. Show CSV")

    try:
        choice = int(input("Please enter an option from above (1-6): "))

        if choice == 1:
            df_sorted = df.sort_values(by='price', ascending=True)
        elif choice == 2:
            df_sorted = df.sort_values(by='price', ascending=False)
        elif choice == 3:
            df_sorted = df.loc[[df['price'].idxmax()]]
        elif choice == 4:
            df_sorted = df.loc[[df['price'].idxmin()]]
        elif choice == 5:
            print("Sum of all prices: ", df['price'].sum())
            continue
        elif choice == 6:
            print(df)
            continue
        else:
            print("Invalid choice. Please select an option from 1 to 5.")
            continue

        x = df_sorted.index
        y = df_sorted['price']

        plt.clf()

        plt.bar(x, y)

        plt.xlabel('Product')
        plt.ylabel('Price')
        plt.title('Product Prices')

        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Error! Please retry")