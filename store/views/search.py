from django.shortcuts import render
from django.views import View
from store.models.product import Products


class Search(View):


    
    def get(self, request):
        query = request.GET.get('query')
        if query:
            result_products = Products.objects.filter(name__icontains=query)
        else:
            result_products = Products.get_all_products()

        context = {
            'result_products': result_products,
            'query': query
        }
        return render(request, 'search.html', context)