import openai

openai.api_key = "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"

class Gpt():
    def __init__(self):
        pass

    def query_gpt(self, excerpt):
        question = 'Create 2 flashcards for revision summarising the following text, each with a front and back. They should be formatted in a Python 2D array, where for each element el, el[0] is the front of the card, and el[1] is the back:' + excerpt
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": question}]   
        )
        return completion.choices[0].message["content"].lower().strip('"')

if __name__ == "__main__":
    gpt = Gpt()
    print(gpt.query_gpt("""The mobility of factors of production
    The mobility of factors of production refers to the extent to which resources
    can be changed for one another in the production process. For example, farming
    can be very traditional in some parts of the world and rely heavily on labour
    resources. However, in other countries, farming is predominantly mechanised,
    with a heavy reliance of capital resources.
    Economists usually talk about labour mobility, although factor mobility can
    apply to any factor of production. For example:
    » Land might be used for various competing purposes, such as to grow certain
    fruits and/or vegetables, or to construct buildings such as housing, hospitals
    or schools.
    » Capital equipment might be used for different purposes too. For example, the
    same machinery in the Coca-Cola factory can be used to produce Coca-Cola,
    Sprite and/or Fanta.
    » Entrepreneurs can also be mobile. For example, Meg Whitman, chief executive
    offi cer (CEO) of Hewlett-Packard, was previously a vice president of the Walt
    Disney Company and CEO of eBay."""))