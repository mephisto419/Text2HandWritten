import pywhatkit

text = input("Enter text to be converted into hand written note.")
try:
    pywhatkit.text_to_handwriting(text, rgb=(0, 0, 255))
    print("Converted, Check project file location")
except:
    print("An exception occurred")
