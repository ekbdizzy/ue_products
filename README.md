## Simple XML-based API on Django REST framework.

This is a simple Django REST framework project that provides an API for a simple XML-based data format. The API provides
the following endpoint:
/products/ - GET

The purposes of project show:

1. How to work with XML data in Django REST framework. The project uses Django REST framework and Django REST framework
   XML package.
2. How to create a simple API with Django REST framework using SOLID principals, such as Single Responsibility and
   Dependency Inversion.
3. How to optimize SQL queries in Django REST framework using Model's Manager to avoid queries outside of Data Access
   Layer.

The API returns a list of products with the biggest discount in tariffs in the following XML format:

```xml

<root>
    <list-item>
        <id>1</id>
        <name>Product 1</name>
        <tariffs>
            <list-item>
                <id>1</id>
                <name>Tariff 1</name>
                <base_price>1000.00</base_price>
                <discount>10</discount>
                <discount_end_date>2024-08-01</discount_end_date>
                <price_with_discount>900.00</price_with_discount>
            </list-item>
            <list-item>
                <id>2</id>
                <name>Tariff 2</name>
                <base_price>2000.00</base_price>
                <discount>20</discount>
                <discount_end_date>2024-08-01</discount_end_date>
                <price_with_discount>1600.00</price_with_discount>
            </list-item>
        </tariffs>
    </list-item>
    <list-item>
        <id>2</id>
        <name>Product 2</name>
        <tariffs>
            <list-item>
                <id>3</id>
                <name>Tariff 3</name>
                <base_price>3000.00</base_price>
                <discount>30</discount>
                <discount_end_date>2024-08-01</discount_end_date>
                <price_with_discount>2100.00</price_with_discount>
            </list-item>
        </tariffs>
    </list-item>
</root>
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/ekbdizzy/ue_products.git
```

2. Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Change credentials in the `Makefile` if needed
5. Run the project

```bash
make run
```

## Testing

To run tests, use the following command:

```bash
make test
```
