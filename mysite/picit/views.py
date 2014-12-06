from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
import pdb

from picit.models import Image


class ImageForm(ModelForm):
    class Meta:
        model = Image


def index(request):
    if request.method == 'POST':
        form = request.POST
        tags_text = form["tags"]
        tags = tags_text.split(",")
        image = Image(title=form["title"], url=form["url"])
        image.save()
        for tag in tags:
            tag = tag.strip()
            tag = tag.lower()
            image.tag_set.create(text=tag)
    else:
        form = Image()
    images = Image.objects.all()

    #tags = images[4].tags.all()
    pdb.set_trace()
    context = {'images': images}
    return render(request, 'picit/index.html', context)

"""
def update(request):
    image = Image(name=request["name"], url=request["url"])
    image.save()
    return HttpResponseRedirect(reverse('polls:index'))
"""