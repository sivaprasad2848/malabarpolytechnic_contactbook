class vehicle:
    engine_capacity=None
    fuel_type=None 
    def set_data(self,ec,ft):
        self.engine_capacity=ec 
        self.fuel_type=ft
class car(vehicle):
    brand_name=None 
    def set_brand(self,bn):
        self.brand_name=bn 
    def display(self):
        print("Brand Name:"+self.brand_name)
        print("Fuel Type:"+self.fuel_type) 
        print("Engine capacity:"+self.engine_capacity)
c=car()
c.set_data("1200cc","petrol")
c.set_brand("Toyota")
c.display()   