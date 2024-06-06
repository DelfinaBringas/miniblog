from django.urls import path

from product.views.product_view import (
    product_list,
    product_create,
    product_delete,
    product_detail,
    product_update,
    
)
from product.views.category_view import (
     category_create,
     category_delete,
     category_detail,
      category_list,
     category_update,
)

from product.views.supplier_view import(
    supplier_create,
    supplier_delete,
    supplier_detail,
    supplier_list,
    supplier_update
)

from product.views.product_review_view import(
    ProductReviewCreateView,
    ProductReviewView,
)

urlpatterns = [
    path(route='', view=product_list, name='product_list'),
    path(route='create/',view=product_create, name='product_create'),
    path(route='<int:id>/',view=product_detail,name="product_detail"),
    path(route='<int:id>/update/',view=product_update,name="product_update"),
    path(route='<int:id>/delete/',view=product_delete,name="product_delete"),

    path (route='category/', view=category_list, name='category_list'),
    path(route='category/create/',view=category_create,name="category_create"), 
    path(route='category/<int:id>/delete/',view=category_delete,name="category_delete"),
    path(route='category/<int:id>/',view=category_detail,name="category_detail"),
    path(route='category/<int:id>/update/',view=category_update,name="category_update"),

    path(route='supplier/', view=supplier_list, name='supplier_list'),
    path(route='supplier/create/',view=supplier_create, name='supplier_create'),
    path(route='supplier/<int:id>/',view=supplier_detail,name="supplier_detail"),
    path(route='supplier/<int:id>/update/',view=supplier_update,name="supplier_update"),
    path(route='supplier/<int:id>/delete/',view=supplier_delete,name="supplier_delete"),

    path(route='product_reviews/', view=ProductReviewView.as_view(), name='product_reviews'),
    path(route='product_reviews/create', view=ProductReviewCreateView.as_view(), name='product_reviews_create')

] #siempre usar product adelante