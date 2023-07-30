from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    reg_date = models.DateField(auto_now=True)

    def __str__(self):
        return (f'Customer:\n{self.name}\n{self.email}\n'
                f'{self.phone}\n{self.address}\n'
                f'{self.reg_date}')


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.EmailField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField()
    add_date = models.DateField(auto_now=True)

    def __str__(self):
        return (f'{self.name}:\n'
                f'{"Price":<15}{self.price:>20}\n'
                f'{"added on:":<15}{self.add_date:>20}\n'
                f'{"amount left:":<15}{self.amount:>20}\n'
                f'{"Description:":<15}{self.description}\n')


class Order(models.Model):
    customer: Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product: Product = models.ManyToManyField(Product)
    order_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return (f'{self.customer.name} {self.customer.email} '
                f'{self.product.name} {self.total_price} '
                f'{self.order_date}')