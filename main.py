from DVD import DVD
from DVDStore import DVDStore
from Customer import Customer
from CustomerBTreeType import CustomerBTreeType
from DVListType import DVListType
def main():
# Create an instance of the CustomerBTreeType class
 customer_database = CustomerBTreeType()


# Create customers and add them to the customer database
customer1 = Customer(first_name="John", last_name="Doe", account_number=1)
customer2 = Customer(first_name="Jane", last_name="Doe", account_number=2)
customer3 = Customer(first_name="Jim", last_name="Smith", account_number=3)
# customer_database.insert({'customer': customer1, 'account_number': customer1.account_number})
# customer_database.insert({'customer': customer2, 'account_number': customer2.account_number})
# customer_database.insert({'customer': customer3, 'account_number': customer3.account_number})

# Create an instance of the DVDStore class
store = DVDStore(customers=[customer1, customer2, customer3])

# Add DVDs to the store
dvd1 = DVD(name="The Shawshank Redemption", copies=3, stars="Tim Robbins", producer="N/A", director="Frank Darabont", production_company="Columbia Pictures")
dvd2 = DVD(name="The Godfather", copies=2, stars="Marlon Brando", producer="Albert S. Ruddy", director="Francis Ford Coppola", production_company="Paramount Pictures")
dvd3 = DVD(name="The Dark Knight", copies=1, stars="Christian Bale", producer="Emma Thomas", director="Christopher Nolan", production_company="Warner Bros. Pictures")

store.dvds = [dvd1, dvd2, dvd3]

# Rent a DVD
store.rent_dvd(dvd1, customer1)

# Return a DVD
store.return_dvd(dvd1, customer1)

# Print the list of all of the DVDs in the store
store.print_dvds()

# Check whether a particular DVD is in the store
if dvd1 in store.dvds:
    print("The DVD 'The Shawshank Redemption' is in the store.")
else:
    print("The DVD 'The Shawshank Redemption' is not in the store.")

# Print the list of all of the DVDs rented by each customer
for customer in store.customers:
    print(customer.first_name, customer.last_name, "has rented:")
    for dvd in customer.rented_dvds:
        print("-", dvd.name)
if __name__ == '__main__':

 main()