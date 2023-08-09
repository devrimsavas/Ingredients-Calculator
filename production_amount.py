def production(product_name, product, total_resources):
    global production_numbers

    # Create a copy of total_resources
    total_resources_copy = total_resources.copy()

    # Set found_all to True initially
    found_all = True

    for req_el_name, req_el_amount in product.items():
        found = False
        for ex_el_name, ex_el_amount in total_resources_copy.items():
            if req_el_name == ex_el_name:
                found = True
                if ex_el_amount >= req_el_amount:
                    total_resources_copy[ex_el_name] = ex_el_amount - req_el_amount
                else:
                    found_all = False
                    break
        if not found:
            found_all = False
            break

    if found_all:
        # Update the original total_resources dictionary
        total_resources.update(total_resources_copy)
        production_numbers[product_name] += 1

    print(f'The product: {product_name} -- produced: {production_numbers[product_name]}\n\n')

    remained_material = ""
    for ex_el_name, ex_el_amount in total_resources.items():
        remained_material += (f'{ex_el_name}: {ex_el_amount}\n')
    print('REMAINED MATERIAL')
    print(remained_material)

    
production_numbers={'cake':0,'banana_cake':0,'omlet':0,'meringue':0}

chocolade_cake={'cake':1,
           'cacao':5}
cake={'egg':3,
     'flour':400,
     'sugar': 300,
     'backing_powder':4,
     'cacao':20,
     'milk':2,
     'vanilla':1}
banana_cake={'egg':3,
     'flour':400,
     'sugar': 300,
     'backing_powder':4,
     'banana':2,
     'milk':2,
     'vanilla':1}


omlet={'egg':2,
      'flour':100,
      'backing_powder':1
      }

meringue={'egg':4,
      'sugar':100}


at_home={'egg':500,
     'flour':18400,
     'sugar': 15300,
     'backing_powder':240,
     'cacao':2000,
     'banana':30,
     'milk':80,
     'vanilla':50     }

tur=0
while True:
    t=input(' press enter for production')
    print(f"production : {tur}\n\n")
    print("--------------------------------------------")
    production('cake',cake,at_home)
    production('banana_cake',banana_cake,at_home)
    production('omlet',omlet,at_home)
    production('meringue',meringue,at_home)
    print("--------------------------------------------")

    
    
    tur+=1
    
            


