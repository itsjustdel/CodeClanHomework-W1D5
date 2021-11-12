def get_pet_shop_name(pet_shop):    
    # return the string value held in the pet shop dictionary under "name"
    return pet_shop["name"]

def get_total_cash(pet_shop):
    # return the integer held in the "total_cash" element of the "admin" dictionary
    # within the "pet_shop" dictionary
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    # integer addition to modify existing element
    pet_shop["admin"]["total_cash"]+= cash

def get_pets_sold(pet_shop):
    # return integer "pets_sold"
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    # add to the existing value of pets sold in the admin section of the pet shop
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    # return the length of the list "pets" in pet_shop
    return len( pet_shop["pets"] )

def get_pets_by_breed(pet_shop, breed):
    #create a list to retun
    breeds_matched = []
    for pet in pet_shop["pets"]:
        #string comparison between dictionary and parameter
        if pet["breed"] == breed:
            #add to our list - we have a match!
            breeds_matched.append(pet)
    
    return breeds_matched

def find_pet_by_name(pet_shop, name):
    # return a dictionary ("pet") from the pets list that has a matching name
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

    #if we don't find anything return None for completeness
    return None

def remove_pet_by_name(pet_shop, name):   
    # one liner to remove the pet from the list
    # this works because either the function "find_pet_by_name" returns a pet which we be removed
    # or it returns None. Removing "None" from a list does nothing
    pet_shop["pets"].remove(find_pet_by_name(pet_shop, name))

def add_pet_to_stock(pet_shop, new_pet):
    # add "new_pet" to the "pets" list in the pet_shop dictionary
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    # grab the value from "cash" within the cust dictionary
    return customer["cash"]

def remove_customer_cash(customer, cash_to_remove):
    # subtract "cash_to_remove" from the customer's cash value
    customer["cash"] -= cash_to_remove

def get_customer_pet_count(customer):
    #return the length of the list "pets" in the customer dictionary
    return len( customer["pets"])

def add_pet_to_customer(customer,new_pet):
    # add a new entry in the customer's pets list
    customer["pets"].append(new_pet)

# OPTIONAL

def customer_can_afford_pet(customer, new_pet):
    # check customer's cash amount against price of "new_pet"
    # return a boolean
    if(customer["cash"] >= new_pet["price"]):
        return True
    else: 
        return False

def sell_pet_to_customer(pet_shop, pet, customer):
    #steps to sell a pet
    # remove pet from pet shop's stock if there and customer has enough money
    if(pet == None or customer_can_afford_pet(customer,pet) == False):
        # can't do business, get out of here! - return a fail with 0 or False
        return 0

    #let's take the pet out of the shop's list,
    #if we made it to this point in the script, we can do business
    remove_pet_by_name(pet_shop, pet["name"])

    # add a pet to customers pets list
    add_pet_to_customer(customer, pet)

    # add 1 to pets sold total in pet shop admin
    increase_pets_sold(pet_shop, 1)

    # subract cash from customer
    remove_customer_cash(customer,pet["price"])
    
    # add it to the pet shop total cash
    add_or_remove_cash(pet_shop, pet["price"])

    #unnecessary return but I like to be able to see all return points 
    # - could return a boolean result to check if we managed to sell or not
    return 1



