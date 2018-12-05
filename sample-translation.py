# -*- coding: utf-8 -*-
import json
from watson_developer_cloud import LanguageTranslatorV3 as LanguageTranslator

language_translator = LanguageTranslator(
  version='2018-12-03',
  iam_apikey='JEUE5pCeaa8a9_0rNIwlSpbH8xP0uYVyhiEUGZZNqNag',
  url='https://gateway-tok.watsonplatform.net/language-translator/api'
)
# translation = language_translator.translate(
#     text='Hello',
#     model_id='en-ja').get_result()
# print(json.dumps(translation, indent=2, ensure_ascii=False))
num = 0
while (num < 1):
    text = input('和英翻訳するよ。日本語か英語を入力してね。\n')
    # 言語識別
    identify = language_translator.identify(text)
    language = identify.get_result()
    source = language['languages'][0]['language']
    if source == 'en':
        target = 'ja'
    elif source == 'ja':
        target = 'en'
    else :
        source = 'ja'
        target = 'en'
    # 翻訳
    translation = language_translator.translate(
        text=text,
        source=source,
        target=target)
    print(translation.result['translations'][0]['translation'])
    print()
    num += 1

