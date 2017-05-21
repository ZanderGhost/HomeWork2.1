#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        with open('cook_book.txt') as f:
            for line in f:
                if dish in line:
                    count_ingridients = f.readline()
                    count_ingridients = int(count_ingridients)
                    for i in range(count_ingridients):
                        new_shop_list_item = {}
                        ingridient = f.readline()
                        ingridient = ingridient.strip()
                        ingridient = ingridient.split(' ')
                        new_shop_list_item['ingridient_name'] = ingridient[0]
                        new_shop_list_item['quantity'] = int(ingridient[1])
                        new_shop_list_item['measure'] = ingridient[2]
                        new_shop_list_item['quantity'] *= person_count

                        if new_shop_list_item['ingridient_name'] not in shop_list:
                            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                        else:
                            shop_list[new_shop_list_item['ingridient_name']]['quantity']\
                            += new_shop_list_item['quantity']
                      
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], \
          shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()