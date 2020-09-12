from django.shortcuts import render
import ast
from random import shuffle
from .models import Score
import random

# Create your views here.
def shuffle_list(lst):
    lst2 = lst.copy()
    shuffle(lst2)
    return lst2

def home(request):
    user = request.user
    context = {}
    context['show'] = True
    if user.is_active:
        if request.method == 'POST':
            if request.POST['number']:
                num = request.POST['number']
                context['show'] = False
                context['number'] = num
                words = user.word_set.all()
                all_words = []
                for word in words:
                    meaning = []
                    temp = ''
                    for mean in word.meaning_set.all():
                        temp = mean.pos
                        meaning.append((ast.literal_eval(mean.meaning), temp))
                    all_words.append((word, meaning))
                k = shuffle_list(all_words)[:int(num)]
                context['words'] = k
                context['total_number'] = len(k)
    return render(request, 'practice.html', context)

motivation = ["All our dreams can come true, if we have the courage to pursue them.” – Walt Disney",
"“The secret of getting ahead is getting started.” – Mark Twain",
"“I’ve missed more than 9,000 shots in my career. I’ve lost almost 300 games. 26 times I’ve been trusted to take the game winning shot and missed. I’ve failed over and over and over again in my life and that is why I succeed.” – Michael Jordan",
"“Don’t limit yourself. Many people limit themselves to what they think they can do. You can go as far as your mind lets you. What you believe, remember, you can achieve.” – Mary Kay Ash",
"“The best time to plant a tree was 20 years ago. The second best time is now.” – Chinese Proverb",
"“Only the paranoid survive.” – Andy Grove",
"“It’s hard to beat a person who never gives up.” – Babe Ruth",
"“I wake up every morning and think to myself, ‘how far can I push this company in the next 24 hours.’” – Leah Busque",
"“If people are doubting how far you can go, go so far that you can’t hear them anymore.” – Michele Ruiz",
"“We need to accept that we won’t always make the right decisions, that we’ll screw up royally sometimes – understanding that failure is not the opposite of success, it’s part of success.” – Arianna Huffington",
"“Write it. Shoot it. Publish it. Crochet it, sauté it, whatever. MAKE.” – Joss Whedon"
]
def result(request):
    user = request.user
    context = {}
    user = request.user
    if user.is_active:
        if request.method == 'POST':
            score = request.POST['score_input']
            total = request.POST['max-score']
            score = int(score)
            total = int(total)
            context['score'] = score
            context['total'] = total
            obj, created = Score.objects.get_or_create(score=score, total=total, percent=(score*100)/total)
            obj.user.add(user)
            context['history'] = user.score_set.all()
            ind = random.randint(0,len(motivation))
            context['quote'] = motivation[ind]
    return render(request, 'result.html', context)