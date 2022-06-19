import deepl
translator = deepl.Translator("7adebb8d-2ff7-5a2e-0fa5-b626408c1606:fx")
result = translator.translate_text("Hello, world!", target_lang="FR")
print(type(str(result)))
