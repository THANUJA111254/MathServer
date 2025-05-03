from django.shortcuts import render
def power_calculator(request):

   context={}
   context['power'] = "0"
   context['I'] = "0"
   context['R'] = "0"
   if request.method == 'POST':
      print("POST method is used")
      I = request.POST.get('intensity','0')
      R = request.POST.get('resistance','0')
      print('request=',request)
      print('resistance=',R)
      print('intensity',I)
      power = int(I)**2*int(R)
      context['power'] = power
      context['I'] = I
      context['R'] = R
      print('Power',power)
   return render(request,'mathapp/math.html',context)

# Create your views here.
