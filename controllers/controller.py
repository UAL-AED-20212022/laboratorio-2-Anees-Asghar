from models.LinkedList import LinkedList


def create_linked_list():
    return LinkedList()


def register_country_at_start(country_list, country_name):
    country_list.insert_at_start(country_name)


def register_country_at_end(country_list, country_name):
    country_list.insert_at_end(country_name)


def register_country_after(country_list, new_country_name, target_country_name):
    country_list.insert_after_item(target_country_name, new_country_name)


def register_country_before(country_list, new_country_name, target_country_name):
    country_list.insert_before_item(
        target_country_name, 
        new_country_name
    )


def register_country_at_index(country_list, country_name, index):
    country_list.insert_at_index(index, country_name)


def get_country_count(country_list):
    return country_list.get_count()


def is_country_in_list(country_list, country_name):
    return country_list.search_item(country_name)


def remove_first_country(country_list):
    country_name = country_list.start_node.item
    country_list.delete_at_start()
    return country_name


def remove_last_country(country_list):
    country_name = country_list.get_last_node() 
    country_list.delete_at_end()
    return country_name


def remove_country(country_list, country_name):
    res = country_list.search_item(country_name)
    if res: 
        country_list.delete_element_by_value(country_name)
    return res


def register_country_at_index(country_list, country_name, index):
    country_list.insert_at_index(index, country_name)
