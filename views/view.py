from controllers import controller as ctrl

def main():
    # initialize the linked list
    country_list = ctrl.create_linked_list()

    while True:
        try:
            # get user input
            usr_input = input().split(' ')
            command, args = usr_input[0].upper(), usr_input[1:]

            if command == "RPI": # Register country at the beginning
                ctrl.register_country_at_start(
                    country_list, 
                    country_name=args[0]
                )

                # print updated list
                country_list.traverse_list()
            
            elif command == "RPF": # Register country at the end
                ctrl.register_country_at_end(
                    country_list, 
                    country_name=args[0]
                )
                
                # print updated list
                country_list.traverse_list()
            
            elif command == "RPDE": # Register country after specified country
                ctrl.register_country_after(
                    country_list, 
                    new_country_name=args[0], 
                    target_country_name=args[1]
                )
                
                # print updated list
                country_list.traverse_list()
            
            elif command == "RPAE": # Register country before specified country
                ctrl.register_country_before(
                    country_list, 
                    new_country_name=args[0], 
                    target_country_name=args[1]
                )
                
                # print updated list
                country_list.traverse_list()

            elif command == "RPII": # Register country at specified index
                ctrl.register_country_at_index(
                    country_list, 
                    country_name=args[0], 
                    index=int(args[1])
                )
                
                # print updated list
                country_list.traverse_list()
            
            elif command == "VNE": # Get number of countries in list
                count = ctrl.get_country_count(country_list)
                print(f"O número de elementos são {count}.")
            
            elif command == "VP": # Check if country is in list
                country_name = args[0]
                is_present = ctrl.is_country_in_list(
                    country_list, 
                    country_name
                )
                
                if is_present: print(f"O país {country_name} encontra-se na lista.")
                else: print(f"O país {country_name} não se encontra na lista.")
            
            elif command == "EPE": # Remove first country in list
                country_name = ctrl.remove_first_country(country_list)

                # print the country that was removed
                if country_name: print(f"O país {country_name} foi eliminado da lista.")
            
            elif command == "EUE": # Remove last country in list
                country_name = ctrl.remove_last_country(country_list)

                # print the country that was removed
                if country_name: print(f"O país {country_name} foi eliminado da lista.")
            
            elif command == "EP": # Remove the country specified
                country_name = args[0]
                res = ctrl.remove_country(
                    country_list, 
                    country_name
                )
                
                # print status message
                if res: print(f"O país {country_name} foi eliminado da lista.")
                else: print(f"O país {country_name} não se encontra na lista.")
            
            else: break
        
        except EOFError: break
