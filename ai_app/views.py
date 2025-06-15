from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png'), FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, FileResponse
from .forms import SignupForm, LoginForm
from .utils import generate_quiz, tokenize_text, extract_keywords, recommend_similar, dynamic_plot, ar_process, tts
from PIL import Image
from io import BytesIO

def signup_view(request):
    form = SignupForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('ai_login')
    return render(request, 'ai_app/signup.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('ai_index')
    return render(request, 'ai_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('ai_login')

@login_required
def index(request):
    return render(request, 'ai_app/index.html')

@login_required
def quiz_api(request):
    return JsonResponse({'result': generate_quiz(request.POST.get('prompt',''))})

@login_required
def tokenize_api(request):
    return JsonResponse({'result': tokenize_text(request.POST.get('prompt',''))})

@login_required
def keywords_api(request):
    return JsonResponse({'result': extract_keywords(request.POST.get('prompt',''))})

@login_required
def similar_api(request):
    return JsonResponse({'result': recommend_similar(request.POST.get('prompt',''))})

@login_required
def tts_api(request):
    path = tts(request.POST.get('prompt',''))
    return FileResponse(open(path,'rb'), content_type='audio/mpeg')

@login_required
def plot_api(request):
    buf = dynamic_plot(request.POST.get('prompt',''))
    return FileResponse(buf, content_type='image/png')

@login_required
def ar_api(request):
    img = Image.open(request.FILES['image'])
    proc = ar_process(img)
    buf = BytesIO()
    proc.save(buf, 'PNG')
    buf.seek(0)
    return FileResponse(buf, content_type='image/png')
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
