from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Joy
from .models import Joy1
from .serializers import JoySerializer
from .serializers import Serializer
# from rest_framework.response import responses
from rest_framework.response import Response
from rest_framework import status
from django.template import loader
from django.http import HttpResponse



# resposes r Response er moddhe diffrence ashe .. Response dile ami json data dekhty parbo new created data tar 
#  for deal with multiple get,post,put,delete request we use @api_view([ .... ]) decorator


# create end point here


@api_view(['GET', 'POST'])

def Items(request,format=None):

    if request.method == 'GET':

        # get all data using this method. we need to work like this => get all the data => serialize them => send those data using a json response
        items = Joy.objects.all()
        # many=true assign korsi cz amra akta full list ke serialize korbo ajonno eita list er sob gula object ke eita serialize korbe .
        serializer = JoySerializer(items, many=True)
        # return jsonresponse and set safe=false cz we want to  serialize a non-dictionary object
        # return JsonResponse(serializer.data,safe=False)
        # or eivabe korle safe nah dilau kno issue hobe nah
        # return JsonResponse({"Data": serializer.data})
        return Response(serializer.data)




    if request.method == 'POST':
        # akn amra database a new akta obj create korbo to sei jonno upr er kaj gulai revarse a korbo .
        # first a json data ke deserialize korbo => check dibo eita valid ki nah , valid hole save korbo then akta response send korbo je sucessfully created , invalid hole akta error msg dibo  just
        serializer = JoySerializer(data=request.data)
        # checking valid or not 
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            # or eivabeu dite pari .. eita aktu besi secure karon djngo nije rapup korbe ei jaigai 
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])

def item(request, id,format=None):

    try:
    # ami akta data niye ashbo just, seijonno get diye fatch kore amr request er parameter er songe match korbo 
       item=Joy.objects.get(pk=id);
    except Joy.DoesNotExist:
        # id jodi nah pai tkn ei status show korbe 
        return Response(status=status.HTTP_404_NOT_FOUND)



    if request.method == 'GET':
        serializer = JoySerializer(item)
        # Response ta holo django er akta function jeita r o kisu functinality add kore data send kore
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer=JoySerializer(item,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer._errors,status=status.HTTP_404_NOT_FOUND)



    if request.method == 'DELETE':
        Joy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])

def alls(request,format=None):

    if request.method == 'GET':

        # get all data using this method. we need to work like this => get all the data => serialize them => send those data using a json response
        items = Joy1.objects.all()
        # many=true assign korsi cz amra akta full list ke serialize korbo ajonno eita list er sob gula object ke eita serialize korbe .
        serializer = Serializer(items, many=True)
        # return jsonresponse and set safe=false cz we want to  serialize a non-dictionary object
        # return JsonResponse(serializer.data,safe=False)
        # or eivabe korle safe nah dilau kno issue hobe nah
        # return JsonResponse({"Data": serializer.data})
        # return Response(serializer.data)
        template = loader.get_template('jo.html',{'hotel' : serializer.data})
        return HttpResponse(template.render())
     