from django.shortcuts import render, redirect

products = [
    {'id':0, 'name':'Dojo Tshirt', 'price':19.99},
    {'id':1, 'name':'Dojo Sweater','price':29.99},
    {'id':2, 'name':'Dojo Cup','price':4.99},
    {'id':3, 'name':'Algorithm Book','price':49.99},
]

def index(request):
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'lastpurchase' not in request.session:
        request.session['lastpurchase'] = 0
    if 'itemsordered' not in request.session:
        request.session['itemsordered'] = 0
    context = {
        'items': products
    }
    return render(request, "index.html", context)

def buy(request):
    if request.method != "POST":
        return redirect("/")
    if 'total' not in request.session:
        request.session['total'] = 0
    if 'lastpurchase' not in request.session:
        request.session['lastpurchase'] = 0
    if 'itemsordered' not in request.session:
        request.session['itemsordered'] = 0
    i = int(request.POST['id'])
    request.session['itemsordered'] += int(request.POST['quantity'])
    request.session['lastpurchase'] = products[i]['price'] * float(request.POST['quantity'])
    request.session['total'] += request.session['lastpurchase']
    return redirect('/checkout/')

def checkout(request):
    return render(request, "checkout.html")

def clear(request):
    request.session['total'] = 0
    request.session['lastpurchase'] = 0
    request.session['itemsordered'] = 0
    return redirect('/')
