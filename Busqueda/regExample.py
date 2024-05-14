import re

class RegExample:
    def __init__(self) -> None:
        pass

    @staticmethod
    def buscar(texto:str) -> list:
        #patron palabras que empiezan en vocal minúscula
        patron = "\\b[aeiou][^\\s.,]*"
        result = re.findall(patron, texto)
        return result
    
    @staticmethod
    def validURL(url:str) -> bool:
        r"^https?://([a-z].+)+.[a-z]{2}"
    

if __name__ == "__main__":
    text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id bibendum metus, sit amet accumsan nisi. Suspendisse sed tristique ligula. Morbi eu posuere sapien. Pellentesque non nisl nunc. Mauris euismod augue ut turpis dignissim, sed sollicitudin ligula malesuada. Nullam cursus nibh nisl, sed aliquam dui lobortis eget. Vestibulum elementum tortor massa, quis tempus neque gravida eu. Duis diam nulla, lobortis at dolor sit amet, interdum consectetur nisi.

Integer molestie erat ac neque malesuada, ut volutpat justo suscipit. Sed pellentesque gravida libero non rhoncus. Etiam sit amet egestas ante. Nam nec sodales ante. Fusce in purus lobortis, volutpat urna in, malesuada turpis. In porta cursus libero, quis rhoncus purus laoreet vitae. Nulla ullamcorper ex et vestibulum varius. Quisque tempus quam sed imperdiet imperdiet. Morbi nec dapibus sapien.

Proin viverra libero in hendrerit lacinia. Duis congue cursus nisi et malesuada. Proin commodo urna est, at auctor nisl posuere vel. Fusce purus ligula, tempus non tristique sed, gravida sit amet ipsum. Sed in nulla tincidunt purus tempus facilisis. Phasellus tempor consequat tortor id feugiat. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Praesent feugiat ultricies massa, quis ornare orci molestie ut. Sed sodales consequat risus at semper. Morbi a erat quis quam imperdiet mattis et viverra quam. Suspendisse interdum, odio sit amet egestas finibus, dui nisl mollis neque, in dictum magna lacus sed nunc.

Nulla quis semper lacus. Donec sed imperdiet magna. Proin fermentum malesuada ultrices. Etiam metus turpis, sagittis a lorem sed, iaculis imperdiet magna. Donec quis neque vitae diam aliquet tempor non a metus. Etiam dignissim, metus sed aliquet sollicitudin, lorem nulla auctor lacus, id blandit nibh felis in justo. Nam sollicitudin interdum mattis. Fusce nec ipsum eleifend, feugiat tellus non, mollis metus. Sed eu malesuada nibh. Nam pretium accumsan tincidunt. Aenean nec felis at nisl gravida interdum sed et eros. Nulla aliquam dapibus orci vel viverra. Nam condimentum odio ac tempor luctus. In hac habitasse platea dictumst. Donec scelerisque massa sed libero rhoncus, eget ultrices lectus ornare. Ut quis venenatis massa.

Ut mi sem, laoreet sagittis dignissim non, semper a velit. Curabitur et arcu justo. Etiam semper sem ut sem cursus, quis gravida nibh faucibus. Proin tincidunt, libero a luctus faucibus, quam ex finibus nisl, et aliquam nunc ante vel risus. Vestibulum quis felis quis orci consectetur vehicula sit amet in metus. Vivamus interdum sagittis elit ut efficitur. Nulla iaculis libero ac ultricies placerat. Vestibulum sollicitudin luctus maximus.
'''
    print(RegExample.buscar(text))