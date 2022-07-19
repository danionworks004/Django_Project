from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={
        'gambar':'img/udb.png',
        'judul':'blog',
        'sub_judul':'Selamat datang di Profil Kelompok kami',
        'subb_12':'Django',
        'profile1': 'home/img/profile.jpg',
        'nama1':'Andreas Adiputra Marpaung',
        'nim1':'210101050',
        'kelas1':'SIA2',
        'mana1':'Dia cuma mampir harusnya kamu sediain kopi bukan hati',
        'profile2': 'home/img/dani3.jpg',
        'nama2':'Dani Nugroho Wicaksono',
        'nim2':'210101056',
        'kelas2':'SIA2',
        'mana2':'Ikuti kata hatimu, jika pemikiranmu tak bisa sejalan dengan apa yang kamu mau',
        'profile3': 'home/img/zulfi4.jpg',
        'nama3':'Zulfia Mufidatul Ummah',
        'nim3':'210101107',
        'kelas3':'SIA2',
        'mana3':'Im  not perfect, but iam always myself ',
        'profile4':'home/img/savio2.jpg',
        'nama4':'Savio',
        'nim4':'2101010107',
        'kelas4':'SIA2',
        'name4':'Lebih baik melangkah,  dari pada tidak melangkah  ',
       
        
    
        'nav':[
            ['/','Home'],
            ['/home','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'base.html',context)
