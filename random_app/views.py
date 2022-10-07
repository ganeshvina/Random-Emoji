from django.shortcuts import render,HttpResponse
import requests

# Create your views here.
def initial(request):
    return render(request,"index.html")


def home(request):
    k=[]
    
    URL = "https://emojihub.herokuapp.com/api/random"
    r = requests.get(URL)
    c=r.json()
    k=c["htmlCode"][0]
    return render(request,"index.html",{"k":k})
def searchs(request):
    output=[]
    data=request.POST.get("emojis")
    url="https://emojihub.herokuapp.com/api/all"
    r=requests.get(url)
    c=r.json()
    for i in range(len(c)):
        if data in c[i]["name"]:
            output.append(c[i]["htmlCode"])

    return render(request,"index.html",{"output":output})



    
    

