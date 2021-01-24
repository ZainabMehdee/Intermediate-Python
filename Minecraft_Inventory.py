def add_item(inventory):
    resource_name = input('What is the new resource you want to add? ').lower()
    if resource_name in inventory:
        print('Item Already Exists...')
    else:
        inventory[resource_name] = 0 # will create a new item with key=resource_name if does not exist. If it does exist, it will update

def list_inventory(inventory):
    for key, value in inventory.items():
        print(f'{key.ljust(15)} : {value}')

def add_resource(inventory):
    resource_name = input('Resource Name: ').lower()
    count = int(input('How many? '))
    inventory[resource_name] += count

def remove_item(inventory):
    resource_name = input('Resource Name: ').lower()
    count = int(input('How many? '))
    if inventory[resource_name] >= count:
        inventory[resource_name] -= count
    else:
        print(f'Not enough {resource_name}')

def display_menu():
    print('1. Add item to inventory')
    print('2. List all items in inventory')
    print('3. Resource found')
    print('4. Remove item')
    print('0. Exit')

def main():
    inventory = {'coal':0, 'iron':0, 'gold':0, 'diamond':0, 'lapis':0 }
    while True:
        display_menu()
        choice = input('Enter Choice: ')
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            list_inventory(inventory)
        elif choice == '3':
            add_resource(inventory)
        elif choice == '4':
            remove_item(inventory)
        elif choice == '0':
            break
        else:
            print('Invalid Choice. Try again...')

if __name__ =='__main__':
    main()
