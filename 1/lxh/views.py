from django.shortcuts import render_to_response
from django.http import HttpResponse
from bookdb.models import Author,Book

#Author:lxh
#b3
#e
def main_sight(request):
    return render_to_response('main.html')

def search(request):
    return render_to_response('search.html')

def show(request):
    books = Book.objects.all()
    return render_to_response('show.html',{'books' : books})

def look(request):
    thekey = request.GET['thekey']
    books = Book.objects.filter(Title__icontains = thekey)
    return render_to_response('look.html',{'books' : books[0]})

def add(request):
    return render_to_response('add.html')

def addbook(request):
    error = []
    a = []
    errorflag = True
    if 'a0' in request.GET:
        a.append(request.GET['a0'])
    if 'a1' in request.GET:
        a.append(request.GET['a1'])
    if 'a2' in request.GET:
        a.append(request.GET['a2'])
    if 'a3' in request.GET:
        a.append(request.GET['a3'])
    if 'a4' in request.GET:
        a.append(request.GET['a4'])
    if 'a5' in request.GET:
        a.append(request.GET['a5'])
    for i in range(0,len(a)):
        if not a[i]:
            errorflag = False
    judge = Author.objects.filter(AuthorID__icontains = a[2])
    if judge and errorflag:
        newbook = Book(ISBN = a[0],Title = a[1],AuthorID = judge[0],Publisher = a[3],PublishDate = a[4],Price = a[5])
        newbook.save()
        return render_to_response('success.html')
    elif not judge:
        return render_to_response('addauthorconfirm.html',{'AuthorID' : a[2]})
    else:
        error.append('信息不完善哦')
    return render_to_response('add.html',{'error' : error})

def author(request):
    id = request.GET['id']
    return render_to_response('addauthor.html',{'AuthorID' : id})

def addauthor(request):
    error = []
    b = []
    errorflag = True
    if 'b0' in request.GET:
        b.append(request.GET['b0'])
    if 'b1' in request.GET:
        b.append(request.GET['b1'])
    if 'b2' in request.GET:
        b.append(request.GET['b2'])
    for i in b:
        if not i:
            errorflag = False
    id = request.GET['id']
    if errorflag:
        newauthor = Author(AuthorID = id,Name = b[0],Age = b[1],Country = b[2])
        newauthor.save()
        return render_to_response('success.html')
    else:
        error.append('信息不完善哦')
    return render_to_response('addauthor.html',{'AuthorID' : id,'error' : error})

def deleteconfirm(request):
    return render_to_response('deleteconfirm.html')        

def delete(request):
    delete = request.GET['delete']
    booklist = Book.objects.filter(ISBN__icontains = delete)
    books = booklist[0]
    books.delete()
    return render_to_response('deleteresult.html')

def edit(request):
    allbooks = Book.objects.all()
    if 'name' in request.GET:   
        name = request.GET['name']
        books = Book.objects.filter(Title__icontains = name)
        newbook = books[0]
        return render_to_response('edit.html',{'books' : newbook})
    return render_to_response('show.html',{'books' : allbooks})

def editbooks(request):
    error = []
    c = []
    errorflag = True
    if 'c0' in request.GET:
        c.append(request.GET['c0'])
    if 'c1' in request.GET:
        c.append(request.GET['c1'])
    if 'c2' in request.GET:
        c.append(request.GET['c2'])
    name = request.GET['title']
    for i in range(0,len(c)):
        if not c[i]:
            errorflag = False
    books = Book.objects.filter(Title__icontains = name)
    newbook = books[0]
    if errorflag:
        newbook.Publisher = c[0]
        newbook.PublishDate = c[1]
        newbook.Price = c[2]
        newbook.save()
        return render_to_response('editsuccess.html',{'books' : newbook})
    else:
        error.append('信息不完善哦')
    return render_to_response('edit.html',{'books' : newbook,'error' : error})

def author1(request):
    id = request.GET['id']
    return render_to_response('editauthors.html',{'AuthorID' : id})

def editauthors(request):
    error = []
    d = []
    errorflag = True
    if 'd0' in request.GET:
        d.append(request.GET['d0'])
    if 'd1' in request.GET:
        d.append(request.GET['d1'])
    if 'd2' in request.GET:
        d.append(request.GET['d2'])
    for i in range(0,len(d)):
        if not d[i]:
            errorflag = False
    id = request.GET['id']
    author = Author.objects.filter(AuthorID__icontains = id)
    if errorflag:
        newauthor = author[0]
        newauthor.Name = d[0]
        newauthor.Age = d[1]
        newauthor.Country = d[2]
        newauthor.save()
        return render_to_response('editsuccess.html')
    else:
        error.append('信息不完善哦')
    return render_to_response('editauthors.html',{'AuthorID' : id,'error' : error})

def searchbooks(request):
    error = []
    if 'q' in request.GET:
        q = request.GET['q']
        choice = request.GET['choice']
        if not q:
            error.append('内容必须完善哦')
        elif len(q)>40:
            error.append('内容太长')
        else:
            if choice == 'Name':
                books = Book.objects.filter(AuthorID__Name = q)
                return render_to_response('searchResults.html',{'books' : books,'query' :q})
            if choice == 'Title':
                books = Book.objects.filter(Title = q)
                return render_to_response('searchResults.html',{'books' : books,'query' :q})
            if choice == 'Publisher':
                books = Book.objects.filter(Publisher = q)
                return render_to_response('searchResults.html',{'books' : books,'query' :q})
    return render_to_response('search.html',{'error' : error})
