
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from skippings.forms import RegisterForm
from skippings.query import PostgresWrapper
from django.shortcuts import redirect
from .models import Product

def add(request):
    dbconn = PostgresWrapper()
    dbconn.connect()
    response = dbconn.get_data("SELECT * FROM skippings_person")
    print("request.method")
    print(request.method)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        found = False
        for field in form:
         print("Field Error:",field.errors)
        if  (form.is_valid()):
            print("valid")
            for i in response:
              if(form.cleaned_data['firstname'] == i['firstname']):
                  found = True
                  break
            print("found value")
            print(found)
            if(found == False):
             form.save()
             form = RegisterForm()
             dbconn.create_table(''' DELETE FROM skippings_product ''')
             dbconn.create_table( '''INSERT INTO skippings_product (productname, productimage, productprice) 
           VALUES ('Normal Rope', 'https://m.media-amazon.com/images/I/71A3nb-QzcL._SX425_.jpg', 100)''', )
             dbconn.create_table( '''INSERT INTO skippings_product (productname, productimage, productprice) 
           VALUES ('Professional Rope', 'https://m.media-amazon.com/images/I/41Gs-4ydhoL.jpg', 100)''', )
             dbconn.create_table( '''INSERT INTO skippings_product (productname, productimage, productprice) 
           VALUES ('Expert Rope', 'https://m.media-amazon.com/images/I/61DteV3hXqL._SL1000_.jpg', 100)''', )
             return redirect("productdata")
            #  return render(request,'registration/register.html',{'form':form,
            #               "message" : "User registered successfully"
            #  }) 
            else:     
             form = RegisterForm()      
             return render(request,'registration/register.html',{'form':form,
             "message" : "User already exists"
             })
        else:
            print("not valid")
            form = RegisterForm()
            return render(request, 'registration/register.html',{'form':form})
    else:
        print("found value")
        form = RegisterForm()
        return render(request, 'registration/register.html',{'form':form})

def products(request):
    dbconn = PostgresWrapper()
    dbconn.connect()
    print("Product.objects")
    print(Product.objects)
    return render(request, 'products/products.html',{
        "productData" : Product.objects
    })

def optionsPage(request):
    return render(request, 'options/options.html')


    