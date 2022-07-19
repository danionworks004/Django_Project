from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'gambar':'img/udb.png',
        'judul':'blog',
        'sub_klm':'Selamat datang di Halaman terakhir',
        'btn':'/',
        'blg':'/home',
        
       
        
        
       
       
        

           'nav3':[
            ['/','Home'],
            ['/blogs','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'base_3.html',context)
