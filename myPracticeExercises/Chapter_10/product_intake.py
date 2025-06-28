import logging, json

logging.basicConfig(filename = '/Users/mariadelacruz/Documents/AWS Coding Exercises/src/myPracticeExercises/Chapter_10/prod_validation.log',
                    format = '%(asctime)s %(levelname)s %(message)s',
                    level = logging.INFO)

def parse_products(file_path): 
    try: 
        with open(file_path) as f: 
            data = json.load(f)
    except FileNotFoundError:
        # TODO: Write a "File not found: {file_path}" error to the log
        logging.error(f"File not found {file_path}")
        return []

    products = []

    for product in data: 
        if "name" not in product: 
            # TODO: Write a "Product missing required field: name" error to the log
            logging.warning(f"Product missing required field: name")
            continue
        if "price" not in product: 
            # TODO: Write a "Product missing required field: price" error to the log
            logging.warning(f"Product missing required field: price")
            continue
        products.append(product)
        # TODO: Write an "Added product to inventory: {product['name']}" informational message to the log
        logging.info(f"Added product to inventory: {product['name']}")

    return products


parse_products("/Users/mariadelacruz/Documents/AWS Coding Exercises/src/myPracticeExercises/Chapter_10/prod_sample.json")

'''
            ADDITIONAL CHALLENGE

Write validated products list: Create a new function called write_products with two parameters: file_path and products, 
where file_path is a string and products is a list. The function should open and write a file to the specified path. 
It should use the dump method from the JSON module to convert the Python object to a JSON object.

2
Run functions: Use the if __name__ == "__main__" pattern to run your two functions, parse_products and write_products. 
Save the result of calling parse_products to a variable, and pass that value to write_products as its second argument. 
You can use any JSON file name for the file_path string for the first argument of write_products, such as "validated_products.json".
'''