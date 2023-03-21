from django.shortcuts import render, redirect
from googletrans import Translator
from django.conf import settings
import os
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import requests
import replicate
import random
import string
import uuid

os.environ['REPLICATE_API_TOKEN'] = '8e44bbd5185528fc50035af942ea475e795b18ed'
model = replicate.models.get("prompthero/openjourney")
version = model.versions.get("9936c2001faa2194a261c01381f90e65261879985476014a0a37a334593a05eb")

def translate(request):
    if request.method == 'POST':
        text_to_translate = request.POST['text_to_translate']
        translator = Translator()
        translation = translator.translate(text_to_translate, src='ru', dest='en')
        translated_text = translation.text
        inputs =  {
            'prompt': "mdjrny-v4," + translated_text + ", volumetric lighting, octane render, 4 k resolution, trending on artstation, masterpiece",
            'width': 512,
            'height': 512,
            'num_outputs': 1,
            'num_inference_steps': 50,
            'guidance_scale': 6,
        }
        output = version.predict(**inputs)

        generated_image_url = output[len(output) - 1]
        request.session['generated_image_url'] = generated_image_url
        return redirect('translate')
    else:
        generated_image_url = request.session.pop('generated_image_url', '')
        context = {'generated_image_url': generated_image_url}
        return render(request, 'translation_form.html', context)