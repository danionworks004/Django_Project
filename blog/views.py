
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def welcome(request):
    context={
        'gambar':'img/udb.png',
        'judul':'home',
        'sub_judul':'Selamat datang di Profil Kelompok kami',
        'subb_12':'Django',
        
        'nama1':'Andreas Adiputra Marpaung',
        'nim1':'210101050',
        'kelas1':'SIA2',
        'mana1':'Dia cuma mampir harusnya kamu sediain kopi bukan hati',
        'profile1': 'home/img/profile.jpg',
        'nama2':'Dani Nugroho Wicaksono',
        'nim2':'210101056',
        'kelas2':'SIA2',
        'profile2': 'home/img/dani.jpg',
        'mana2':'Ikuti kata hatimu, jika pemikiranmu tak bisa sejalan dengan apa yang kamu mau',
        'nama3':'Zulfia Mufidatul Ummah',
        'nim3':'210101107',
        'kelas3':'SIA2',
        'mana3':'Im  not perfect, but iam always myself ',
        'profile3': 'home/img/julpi.jpg',
        'nama4':'Savio',
        'nim4':'2101010107',
        'kelas4':'SIA2',
        'profile4': 'home/img/savio.jpg',
       
        
        
        
        'nav':[
            ['/','Home'],
            ['/home','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'base_2.html',context)