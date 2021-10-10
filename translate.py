def translator():
  text = input("Enter a text in any language to translate: ")
  langugo = input("Enter which language you would like to translate to: ")
  translated = GoogleTranslator(source="auto",target=langugo).translate(text)
  print(text + " translated to " + langugo + " is " + translated)
  pass
