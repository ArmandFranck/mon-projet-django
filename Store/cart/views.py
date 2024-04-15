from django.shortcuts import render
from .cart import Cart 

def cart_summary(resquest):
    return render(resquest, "cart_summary.html",{})




def cart_add(resquest):
    # Get the cart
	cart = Cart(request)
	# test for POST
	if request.POST.get('action') == 'post':
		# Get stuff
		product_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		# lookup product in DB
		product = get_object_or_404(Product, id=product_id)
		
		# Save to session
		cart.add(product=product, quantity=product_qty)

		# Get Cart Quantity
		cart_quantity = cart.__len__()

		# Return resonse
		response = JsonResponse({'Product Name: ': product.name})
		messages.success(request, ("Product Added To Cart..."))
		return response



def cart_delete(resquest):
    pass

def cart_update(resquest):
    pass

