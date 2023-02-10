class DVDStore:
    def __init__(self, dvds=[], customers=[]):
        self.dvds = dvds
        self.customers = customers
    
    def rent_dvd(self, dvd_name, customer):
        # Check if the DVD is in the store
        dvd = self.get_dvd(dvd_name)
        if dvd:
            # Check if there are any available copies of the DVD
            if dvd.copies > 0:
                # Decrement the number of copies
                dvd.copies -= 1
                # Add the DVD to the customer's list of rented DVDs
                customer.rented_dvds.append(dvd)
                print(f"DVD '{dvd_name}' rented successfully.")
            else:
                print(f"Sorry, all copies of the DVD '{dvd_name}' are rented out.")
        else:
            print(f"The DVD '{dvd_name}' is not in the store.")
    
    def return_dvd(self, dvd_name, customer):
        # Check if the DVD is in the store
        dvd = self.get_dvd(dvd_name)
        if dvd:
            # Check if the customer has rented the DVD
            if dvd in customer.rented_dvds:
                # Remove the DVD from the customer's list of rented DVDs
                customer.rented_dvds.remove(dvd)
                # Increment the number of copies
                dvd.copies += 1
                print(f"DVD '{dvd_name}' returned successfully.")
            else:
                print(f"The customer has not rented the DVD '{dvd_name}'.")
        else:
            print(f"The DVD '{dvd_name}' is not in the store.")
    
    def add_dvd(self, dvd):
        self.dvds.append(dvd)
        print(f"DVD '{dvd.name}' added to the store.")
    
    def get_dvd(self, dvd_name):
        for dvd in self.dvds:
            if dvd.name == dvd_name:
                return dvd
        return None
    
    def show_dvd_details(self, dvd_name):
        dvd = self.get_dvd(dvd_name)
        if dvd:
            print("Details of DVD '{}':".format(dvd.name))
            print("- Name:", dvd.name)
            print("- Director:", dvd.director)
            print("- Year:", dvd.year)
            print("- Copies:", dvd.copies)
        else:
            print(f"The DVD '{dvd_name}' is not in the store.")
    
    def print_dvds(self):
        print("List of DVDs:")
        for dvd in self.dvds:
            print("-", dvd.name)
    
    def print_customers(self):
        print("List of customers:")
       
