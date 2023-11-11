# from products.models import Product


# def wishlist_access(request):
#     ''' Wishlist data access across entire site '''

#     products = 0
#     if request.user.is_authenticated:
#         products = Product.objects.filter(user_wishlist=request.user)

#     return {"user_wishlist: products"}