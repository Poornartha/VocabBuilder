from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Word, Meaning, Note
import json, ast
import datamuse
from PyDictionary import PyDictionary

api = datamuse.Datamuse()
dic = PyDictionary() 

# Create your views here.
def search(request):
    context = {}
    context['save'] = False
    if request.method == 'POST':
        term = request.POST['term']
        if term != '':
            context['term'] = term
        similar = api.words(ml=term, max=5)
        context['similar'] = similar
        context['term'] = term
        definition = dic.meaning(term)
        temp = []
        if definition:
            for dkey in definition:
                temp.append((dkey, definition[dkey]))
        else:
            temp = ['Meaning Not Found']
        context['definition'] = temp
    return render(request, 'form.html', context)


def save(request):
    context = {}
    context['saved'] = False
    context['save'] = True
    if request.method == 'POST':
        term = request.POST['term']
        if term != '':
            context['term'] = term
            user = request.user
            similar = dic.meaning(term)
            if user.is_active:
                word, created = Word.objects.get_or_create(word=term)
                word.user.add(user)
                if created:
                    for s in similar:
                        meaning, mcreated = Meaning.objects.get_or_create(meaning=(similar[s]), pos=s, word=word)
                    context['saved'] = True
                note = request.POST['text']
                Note.objects.create(word=word, user=user, text=note)
            context['similar'] = similar
            context['term'] = term
    return render(request, 'form.html', context)

def show_words(request):
    user = request.user
    context = {}
    context['words'] = []
    if user.is_active:
        temp = []
        for word in user.word_set.all():
            temp2 = []
            for mean in word.meaning_set.all():
                temp2.append((mean.pos, ast.literal_eval(mean.meaning)))
            temp.append((word, tuple(temp2)))
        context['words'] = temp
        for c in context['words']:
            print(c)
    return render(request, 'listings.html', context)




