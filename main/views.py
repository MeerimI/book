from django.shortcuts import render, redirect
from .models import Book


def book(request):
    book_list = Book.objects.all()
    return render(request, "index.html", {"book_list": book_list})


def add_book(request):
    form = request.POST
    title = form["book_title"]
    subtitle = form["book_subtitle"]
    description = form["book_description"]
    price = form["book_price"]
    genre = form["book_genre"]
    author = form["book_author"]
    year = form["book_year"]
    bookItem = Book(title=title, subtitle=subtitle, description=description,
                    price=price, genre=genre, author=author, year=year)
    bookItem.save()
    return redirect(book)


def unmark_book(request, id):
    book_unmark = Book.objects.get(id=id)
    book_unmark.is_favorites = False
    book_unmark.save()
    return redirect(book)


def mark_book(request, id):
    book_unmark = Book.objects.get(id=id)
    book_unmark.is_favorites = True
    book_unmark.save()
    return redirect(book)


def delete_book(request, id):
    book_unmark = Book.objects.get(id=id)
    book_unmark.delete()
    return redirect(book)


def BooksDetail(request, id):
    book_ = Book.objects.get(id=id)
    # book_.save()
    return render(request, "books_detail.html")
