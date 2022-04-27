# DiUS computer store

## Installation
* Open the main folder
* Make sure Python 3.9 is installed correctly
  * You can check running the following command `python3 --version`

## Running Project
* To run the project you must first fill the `input.json`, `products.json` and `discounts.json` files inside the `data` folder with the desired inputs.
  * eg:
products.json: This one is the list of products available at the store. The `key` is the `sku` of the item and the value is a list that
the position`0` is the name of the product and the `position` `1` is the `price`.
```json
  {
    "ipd": ["Super iPad", 549.99],
    "mbp": ["MacBook Pro", 1399.99],
    "atv": ["Apple TV", 109.50],
    "vga": ["VGA adapter", 30.00]
  }
```
* eg:
discounts.json: This json we have a list of the applicable discounts. Below it's the definition of each `key`:
  * `sku`: The sku of the item that will have the discount.
  * `discount`: Is the new price that the product will have if this discount is activated.
  * `number_products_activation`: How many products of this type need to be scanned to activate the discount.
  * `extra_products`: A list of free items (`key` is the `sku` of the free item and the `value` is how many of this item) that the user can get in case the discount is activated. 

```json
  [
    {
      "sku": "atv",
      "discount": 0,
      "number_products_activation": 3,
      "extra_products": [
        {
          "atv": 1
        }
      ]
    },
    {
      "sku": "ipd",
      "discount": 499.99,
      "number_products_activation": 5,
      "extra_products": [
      ]
    },
    {
      "sku": "mbp",
      "discount": 0,
      "number_products_activation": 1,
      "extra_products": [
        {
          "vga": 1
        }
      ]
    }
  ]
```
input.json: This is a list of the sku of the items that are going to be scanned
```json
  ["atv", "ipd", "ipd", "atv", "ipd", "ipd", "ipd"]
```

* Then you have to run the following command `python3 main.py`

* The result should appear in the console.

The result should look like as below:

```
atv
ipd
ipd
atv
ipd
ipd
ipd
2718.95
```

## Tests

* Unit tests were implemented to cover the main functions and functionalities of the code.
* In order to run the unit tests you should use the following command `python3 -m unittest discover tests`

## Assumptions

* The types of discounts will be always as described in the guidelines. Any new type of discount will have to be added in the code.
* No function to remove a product was implemented.
* Assumption of keeping as simple as possible to avoid over engineering

