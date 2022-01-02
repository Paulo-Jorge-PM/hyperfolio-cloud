from django.http import HttpResponse, JsonResponse

def index(request):
    #return HttpResponse("Hello world from auth!")
    return JsonResponse({'data':
        [{
        'id': '1',
        'createdAt': '27/03/2019',
        'description': 'Dropbox is a file hosting service that offers cloud storage, file synchronization, a personal cloud.',
        'media': '/static/images/products/product_1.png',
        'title': 'Dropbox',
        'totalDownloads': '594'
        }]
    })

