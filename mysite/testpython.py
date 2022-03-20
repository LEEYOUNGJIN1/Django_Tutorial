class Text:
    # pass # 아무것도 안하겠다는 의미
    def __init__(self, str):
        self.text = str

    def __str__(self):
        return "Text Class: " + self.text

t = Text("hi")
print(t) # Text Class: hi
print(t.text) # hi