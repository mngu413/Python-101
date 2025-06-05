def display_menu():
    print('1) eggs          $3.25')
    print('2) bacon         $4.00')
    print('3) pancakes      $2.50')
    print('4) orange juice  $1.25')
    print('5) oatmeal       $3.99')
    print('6) milk          $1.25')
    print('7) donut         $2.00')
    
def get_menu_choice():
    print('Enter a menu choice :')
    choice = int(input())
    return choice
    
def get_price_of_menu_choice(food_num):
    choice = {1 : 3.25,
              2 : 4.00,
              3 : 2.50,
              4 : 1.25,
              5 : 3.99,
              6 : 1.25,
              7 : 2.00}
    return (choice[food_num])
    
def diner_wants_another_item():
    answer = input()
    if answer == 'yes':
        return True
    else:
        return False
        
def get_diners_order():
    total_cost = 0.0
    display_menu()

    while diner_wants_another_item():
        food_num = get_menu_choice()
        get_price_of_menu_choice(food_num)
        total_cost += get_price_of_menu_choice(food_num)

    return total_cost
    
def get_number_of_diners_at_table():
    print('Enter number of diners at this table: ')
    diners = int(input())
    return diners
    
def display_suggested_tip_amounts(cost):
    print('10% tip:', f'{(cost * 0.10):.2f}')
    print('15% tip:', f'{(cost * 0.15):.2f}')
    print('20% tip:', f'{(cost * 0.20):.2f}')
    print('25% tip:', f'{(cost * 0.25):.2f}')
    
def get_table_order():
    table_total = 0.0
    number_of_diners = get_number_of_diners_at_table()

    while number_of_diners > 0:
        cost = get_diners_order()
        table_total = table_total + cost
        number_of_diners = number_of_diners - 1

    tax = table_total * 0.08

    print(table_total)
    print(tax)
    print(display_suggested_tip_amounts(cost))
    
    table_total += tax

    return table_total
    
def more_tables_to_serve():
    answer = input()
    if answer == 'yes':
        return True
    else:
        return False
        
def get_all_table_orders():
    total_register_amount = 0.0

    while more_tables_to_serve():
        table_total = get_table_order()
        total_register_amount += table_total

    return total_register_amount

def main():
	total_register_amount = get_all_table_orders()
	print("ticket totals + tax for the entire day: $", total_register_amount)

main()
