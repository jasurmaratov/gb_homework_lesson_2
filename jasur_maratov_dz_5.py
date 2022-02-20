input_list = [57.8, 46.51, 97, 76.05, 13.11, 87.93, 27, 97.09, 0.16, 42,
              96.64, 34.17, 97.45, 40.62, 84.94, 7, 52.23, 93.74, 89, 3.93]

for i, num in enumerate(input_list):

    fix_price = str(f"{float(num):.2f}").split(".")

    if i == len(input_list) - 1:
        end_word = "\n"

    print(f"{fix_price[0]} руб {fix_price[1]} коп")