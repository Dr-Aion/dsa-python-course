
def sum_product(input_tuple):
    sum = 0
    product = 1
    for i in input_tuple:
        sum += i
        product *= i
    return sum, product
    # TODO
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24