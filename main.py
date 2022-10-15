# Функция, которая подсчитывает, попадающих в каждую группу,
# если нумерация ID сквозная и начинается с 0.
# На вход функция получает целое число n_customers (количество клиентов).

# Функция для подсчета суммы цифр в числе
def sum_of_digit_in_the_number(number, sum = 0):
    '''
    Recursive function for calculating the sum of digits of a number

    number:param number: number to count sum
    sum:param sum: 0 or don't pass
    :return: sum of digit in number
    '''
    if number > 0:
        sum += number % 10
        return sum_of_digit_in_the_number(number // 10, sum)
    else:
        return sum

# подсчет покупателей в каждой группе, если id покупателей начинаются с 0
def number_of_customers_in_each_group_from_0(n_customers):
    '''
    Count of customers in group
    :param n_customers: last id or count
    :return: dict with key from sum of digital in id and value from the quantity customers in group
    '''
    group_dict = {}
    customer_id = 0
    while n_customers >= customer_id:
        sum = sum_of_digit_in_the_number(customer_id)

        if sum in group_dict.keys():
            group_dict[sum] += 1
        else:
            group_dict[sum] = 1

        customer_id += 1

    return group_dict

# Функция, аналогичная первой, если ID начинается с произвольного числа.
# На вход функция получает целые числа: n_customers (количество клиентов) и n_first_id (первый ID в последовательности).

# подсчет покупателей в каждой группе, если id покупателей начинаются с какого-то числа
def number_of_customers_in_each_group_from_first_id(n_customers, n_first_id):
    '''
    Count of customers in group
    :param n_customers: Number of customers in the sample
    :param n_first_id: id from which the semple begin
    :return: dict with key from sum of digital in id and value from the quantity customers in group
    '''
    group_dict = {}
    customer_id = n_customers + n_first_id
    while customer_id >= n_first_id:
        sum = sum_of_digit_in_the_number(customer_id)
        if sum in group_dict.keys():
            group_dict[sum] += 1
        else:
            group_dict[sum] = 1
        customer_id -= 1
    return group_dict


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(number_of_customers_in_each_group_from_0(7412567))
    print(number_of_customers_in_each_group_from_first_id(74125, 89435))
    # print(sum_of_digit_in_the_number(6999999))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
