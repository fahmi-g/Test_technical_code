from flask import Flask, request

app = Flask(__name__)

@app.route('/generateSegitiga/<angka>')
def generate_segitiga(angka):
    input_angka = str(angka)
    index = 0
    segitiga = []

    while index < len(input_angka):
        segitiga.append(input_angka[index] + ("0" * (index + 1)))
        index += 1

    return segitiga

@app.route('/generateBilanganGanjil/<angka>')
def generate_bilangan_ganjil(angka):
    bilangan_input = range(0, int(angka) + 1)
    bilangan_ganjil = []

    for bilangan in bilangan_input:
        if bilangan % 2 != 0:
            bilangan_ganjil.append(bilangan)

    return  bilangan_ganjil

@app.route('/generateBilanganPrima/<angka>')
def generate_bilangan_prima(angka):
    bilangan_input = range(3, int(angka) + 1)
    prima = [3]

    for bilangan in bilangan_input:

        pembagi = bilangan
        while pembagi > 1:
            # print(bilangan, pembagi-1)
            if bilangan % (pembagi - 1) == 0:
                break
            else:
                pembagi -= 1

            if (pembagi - 1) == 2 and bilangan % 2 != 0:
                prima.append(bilangan)

    return prima

if __name__ == '__main__':
    app.run()