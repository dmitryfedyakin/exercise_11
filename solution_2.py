class Product:
    '''
    Represents a product.
    '''
    
    def __init__(self, ean_code, name, price):
        '''
        Initializes product data.

        :param ean_code: Barcode number
        :param name: Product name
        :param price: Product price
        '''
        
        self.__ean_code = ean_code
        self.__name = name
        self.__price = price
        self.__country_code = None

    def get_ean_code(self):
        '''
        Returns EAN code value.
        '''
       
        return self.__ean_code

    def get_name(self):
        '''
        Returns product name.
        '''
       
        return self.__name

    def get_price(self):
        '''
        Returns product price value.
        '''
       
        return self.__price

    country_code = property()

    @country_code.setter
    def country_code(self, value):
        '''
        Sets code of the particual country.

        :param value: Country code value
        '''
        
        self.__country_code = value

    @country_code.getter
    def country_code(self):
        '''
        Returns country code.
        '''
        
        return self.__country_code

class Basket:
    '''
    Represents a products basket.
    '''

    def __init__(self):
        '''
        Initializes products basket information
        '''

        self.__items = {}
        self.__total_price = 0.0
        self.__products = []
        self.__country_codes = {}

    def load_products_from_file(self, filename):
        '''
        Loads information about products.

        :param filename: Name of the file
        '''
        
        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                ean_code, name, price_str = line.strip().split(";")
                price = float(price_str)
                product = Product(ean_code, name, price)
                self.__products.append(product)
                country_num  = ean_code[:3]
                if country_num in self.__country_codes:
                    product.country_code = self.__country_codes[country_num]

    def load_country_codes(self, filename):
        '''
        Loads information about country codes.

        :param filename: Name of the file
        '''

        with open(filename, "r", encoding='utf-8') as file:
            for line in file:
                num_range, country = line.strip().split(";")
                start, end = map(int, num_range.split("-"))
                for num in range(start, end + 1):
                    self.__country_codes[str(num).zfill(3)] = country    

    def find_product(self, ean_code):
        '''
        Finds product by its EAN code.

        :param ean_code: Barcode number 
        '''
        
        for product in self.__products:
            if product.get_ean_code() == ean_code:
                return product
        return None

    def add_item(self, product, quantity):
        '''
        Adds particular item to the basket.

        :param product: Product name
        :param qunatity: Nescessary quantity of the products
        '''
        
        if quantity <= 0:
            return
        if product.get_ean_code() in self.__items:
            self.__items[product.get_ean_code()] += quantity
        else:
            self.__items[product.get_ean_code()] = quantity
        self.__total_price += product.get_price() * quantity

    def remove_item(self, product, quantity):
        '''
        Removes particular item from the basket.

        :param product: Product name
        :param qunatity: Nescessary quantity of the products
        '''
        
        if product.get_ean_code() in self.__items:
            if quantity >= self.__items[product.get_ean_code()]:
                self.__total_price -= product.get_price() \
                    * self.__items[product.get_ean_code()]
                del self.__items[product.get_ean_code()]
            else:
                self.__items[product.get_ean_code()] -= quantity
                self.__total_price -= product.get_price() * quantity

    def get_items(self):
        '''
        Returns dictionary with product attributes.
        '''
        
        return self.__items

    def get_total_price(self):
        '''
        Returns total price of the basket.
        '''
        
        return self.__total_price
