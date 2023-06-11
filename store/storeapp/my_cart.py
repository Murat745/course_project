from cart.cart import Cart


class MyCart(Cart):

    def add(self, product, quantity=1, action=None):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = product.id
        new_item = True
        if str(product.id) not in self.cart.keys():

            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': product_id,
                'title': product.title,
                'quantity': 1,
                'price': str(product.price),
            }
        else:
            new_item = True

            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    new_item = False
                    self.save()
                    break
            if new_item:
                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'title': product.title,
                    'quantity': 1,
                    'price': str(product.price),
                }

        self.save()
