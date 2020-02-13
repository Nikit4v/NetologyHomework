bgctemplate = "background-color: "
from django import template

register = template.Library()

@register.tag()
class Year:
    number = None
    def __repr__(self):
        return f"Year: {self.number};"

    class val:
        val = None
        bgc = None

        def setBgc(self, color):
            self.bgc = f"{bgctemplate}{color};"

        def getVal(self):
            return self.val

        def getBgc(self, value):
            if value != "":
                value = float(value)
                self.val = value
                if value < 0:
                    self.setBgc(self, "green")
                elif value < 1:
                    self.setBgc(self, "white")
                else:
                    if value < 2:
                        self.setBgc(self, "ff6666")
                    elif value < 5:
                        self.setBgc(self, "#ff3333")
                    else:
                        self.setBgc(self, '#ff0000')


        def __str__(self):
            return self.val

        def __init__(self, value):
            self.val = value

        def __repr__(self):
            return f"{self.val}"

    class j(val):
        pass

    class f(val):
        pass

    class m(val):
        pass

    class a(val):
        pass

    class my(val):
        pass

    class jn(val):
        pass

    class jl(val):
        pass

    class ag(val):
        pass

    class s(val):
        pass

    class o(val):
        pass

    class n(val):
        pass

    class d(val):
        pass

    class all(val):
        pass

    def __init__(self, value):
        self.val.val = value
        self.number = value
