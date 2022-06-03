from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView

from myapp.models import Work, URN


def login(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if not request.user.is_authenticated:
        return render(request, 'registration/login.html')


def get_works(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'myapp/index.html', {'works': Work.nodes.all()})


def works_index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    works = Work.nodes.all()
    return render(request, 'myapp/index.html', {
        'works': works
    })


def graph_show(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    nodes = []
    rels = []
    works = Work.nodes.all()

    for work in works:
        nodes.append({'id': work.id, 'name': work.name})

    return render(request, 'myapp/index.html', {
        "nodes": nodes, "links": rels
    })


def work_in_progress(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'myapp/building.html')


def graph(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    nodes = []
    rels = []
    works = Work.nodes.all()

    for work in works:
        nodes.append({'id': work.id, 'name': work.name})

        for job in work.incoming:
            print(job)
            rels.append({"source": job.id, "target": work.id})
        for job in work.outcoming:
            rels.append({"source": work.id, "target": job.id})
    print(rels)
    return JsonResponse({"nodes": nodes, "links": rels})


def work_by_id(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    print(id, "id")
    for node in Work.nodes.all():
        if int(id) == node.id:
            return JsonResponse({
                'id': node.id,
                'name': node.name,
            })
    # work = Work.nodes.get(id=int(id))


def search(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    try:
        q = request.GET["q"]
        print(q, "q")
        print(request.path)
    except KeyError:
        return JsonResponse([])
    goodNodes = []
    for node in Work.nodes.all():
        print(node.id)

        if int(q) == node.id:
            goodNodes.append(node)
            # return JsonResponse({
            #     'id': node.id,
            #     'name': node.name,
            # })
    # print(works[0].id, 'works')
    return JsonResponse([{
        'id': work.id,
        'name': work.name,

    } for work in goodNodes], safe=False)


def new_graph(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'myapp/test.html')


def model_load(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'myapp/model_load.html')


def file_upload(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'myapp/model_load.html')


def urn_show(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    urns = URN.objects.all()
    return render(request, "myapp/cdn_model.html", {"urns": urns, "user": request.user})


def urn_index(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    urns = URN.objects.all()
    return render(request, "myapp/urn_index.html", {"urns": urns})


# сохранение данных в бд
def urn_create(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    if request.method == "POST":
        urn = URN()
        urn.type = request.POST.get("type")
        urn.urn = request.POST.get("urn")
        urn.isActive = True
        urn.userId = request.user.id
        urn.save()
    return HttpResponseRedirect("/urn_index/")


# изменение данных в бд
def urn_edit(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    try:
        urn = URN.objects.get(id=id)
        if urn.userId != request.user.id:
            return HttpResponseNotFound("<h2>It's not your URN</h2>")
        if request.method == "POST":
            urn.type = request.POST.get("type")
            urn.urn = request.POST.get("urn")
            urn.save()
            return HttpResponseRedirect("/urn_index/")
        else:
            return render(request, "myapp/urn_edit.html", {"urn": urn})
    except URN.DoesNotExist:
        return HttpResponseNotFound("<h2>URN not found</h2>")


# удаление данных из бд
def urn_delete(request, id):
    if not request.user.is_authenticated:
        return redirect('/login/')
    try:
        urn = URN.objects.get(id=id)
        if urn.userId != request.user.id:
            return HttpResponseNotFound("<h2>It's not your URN</h2>")
        urn.delete()
        return HttpResponseRedirect("/urn_index/")
    except URN.DoesNotExist:
        return HttpResponseNotFound("<h2>URN not found</h2>")
