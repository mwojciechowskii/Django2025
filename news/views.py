from typing import Counter
from django.shortcuts import render
import requests
import re
from datetime import datetime

# Create your views here.
def newsView(request):
	return render(request, 'news/index.html')

def lottoView(request):

    """
    kiedys to poprawie na lepszy kod, bo zabraklo czasu
    """
    context = {}
    try:
        r = requests.get('http://www.mbnet.com.pl/dl.txt', timeout=10)
        r.raise_for_status()
        response = r.text.splitlines()

    except requests.RequestException as exc:
        lastwinner = f"Request failed: {exc}"
        context['lastWinner'] = lastwinner
        return render(request, 'news/lotto.html', context)
    
    counts = Counter()
    totalDraws = 0
    totalNumDrawn = 0
    for i in response:
        parts = i.split(None, 2)
        winningNumbers = parts[2]

        nums = [int(n) for n in re.findall(r'\b(?:[1-9]|[1-4][0-9])\b', winningNumbers)]
        if nums:
            totalDraws += 1
            counts.update(nums)
            totalNumDrawn += len(nums)

    numbersStats = []
    for n in range(1, 50):
        cnt = counts.get(n, 0)
        percent = (cnt / totalNumDrawn * 100) if totalNumDrawn else 0.0
        numbersStats.append({'number': n,
            'count': cnt,
            'percent': percent,})

    num, sep, lastwinner = r.text.splitlines()[-1].partition('.')
    lastWinDatecpy, sep, lastwinner = lastwinner.strip().partition(' ')      
    formatData = "%d.%m.%Y"
    
    lastWinDate = datetime.strptime(lastWinDatecpy, formatData)

    context = {'lastWinner': lastwinner,
        'totalDraws': totalDraws,
        'numbersStats': numbersStats,
               'lastWinDate': lastWinDate,
               'lastWinDatecpy': lastWinDatecpy}
    return render(request, 'news/lotto.html', context)

