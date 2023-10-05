from functions import *

def main():
    operations_List = get_json_file()
    sorted_operations = sort_ex(operations_List)
    sorted_date_operations = sort_date(sorted_operations)
    print_operations = []
    for operation in sorted_date_operations:
        print_operations.append(for_print(operation))
    for operation in print_operations:
        print(operation)


if __name__ == "__main__":
    main()
