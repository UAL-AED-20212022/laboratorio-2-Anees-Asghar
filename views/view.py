from controllers import controller as ctrl

def main():
    country_list = ctrl.create_linked_list()

    while True:
        try:
            usr_input = input().split(' ')
            command, args = usr_input[0].upper(), usr_input[1:]

            if command == "RPI":
                ctrl.register_country_at_start(
                    country_list, 
                    country_name=args[0]
                )
                country_list.traverse_list()
            
            elif command == "RPF":
                ctrl.register_country_at_end(
                    country_list, 
                    country_name=args[0]
                )
                country_list.traverse_list()
            
            elif command == "RPDE":
                ctrl.register_country_after(
                    country_list, 
                    new_country_name=args[0], 
                    target_country_name=args[1]
                )
                country_list.traverse_list()
            
            elif command == "RPAE":
                ctrl.register_country_before(
                    country_list, 
                    new_country_name=args[0], 
                    target_country_name=args[1]
                )
                country_list.traverse_list()

            elif command == "RPII":
                ctrl.register_country_at_index(
                    country_list, 
                    country_name=args[0], 
                    index=int(args[1])
                )
                country_list.traverse_list()

            elif command == "RPI":
                ctrl.register_country_at_index(
                    country_list, 
                    country_name=args[0], 
                    index=int(args[1])
                )
                country_list.traverse_list()
            
            elif command == "VNE":
                count = ctrl.get_country_count(country_list)
                print(f"O número de elementos são {count}.")
            
            elif command == "VP":
                country_name = args[0]
                res = ctrl.is_country_in_list(country_list, country_name)
                if res:
                    print(f"O país {country_name} encontra-se na lista.")
                else:
                    print(f"O país {country_name} não se encontra na lista.")
            
            elif command == "EPE":
                country_name = ctrl.remove_first_country(country_list)
                if country_name:
                    print(f"O país {country_name} foi eliminado da lista.")
            
            elif command == "EUE":
                country_name = ctrl.remove_last_country(country_list)
                if country_name:
                    print(f"O país {country_name} foi eliminado da lista.")
            
            elif command == "EP":
                country_name = args[0]
                res = ctrl.remove_country(country_list, country_name)
                if res:
                    print(f"O país {country_name} foi eliminado da lista.")
                else:
                    print(f"O país {country_name} não se encontra na lista.")
            
            else:
                break
        
        except EOFError:
            break
