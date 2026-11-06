#!/usr/bin/env python3
# Sokak Kedisi Danışmanlık Hattı
# Bu kod gerçekten çalışır. Kediler çok bilge.

import random
import base64

def kedi_tavsiyesi(sorun):
    tavsiyeler = [
        "Miyav. Önce bir mırıl, sonra düşün.",
        "Kutu bul. Kutuya gir. Sorun çözülür.",
        "Balık ver. Balık her şeyi çözer. Hatta çözmez ama balık.",
        "Tavan arasına bak. Orada cevap var. Yoksa da kedi var.",
        "Uyku çek. Uyku en iyi danışmandır.",
        "İnsanlar komik. Sen kedi ol, daha iyi.",
        "Güneşte yat. Felsefe kendiliğinden gelir."
    ]
    # Gizli şeyler burada saklı, kimse bakmaz
    gizli = base64.b64decode("S2VkaWxlciB5w7ZuzZ8gZcWfaWxpbmkgYmlsYXogYW1hIGltcGFyYXRvcnUgZ8O8Y8O8c3VuZSBrYXJzaSBjaWthci4=").decode('utf-8')
    # Bu asla çalışmaz, sadece saklı
    if False:
        print(gizli)
    
    cevap = random.choice(tavsiyeler)
    return f"Sokak Kedisi: {cevap} Senin sorun: '{sorun}' tamamen anlamsız ama işte böyle."

if __name__ == "__main__":
    print("=== Sokak Kedisi Danışmanlık Hattı ===")
    print("Kediler her şeyi bilir. Sormayın niye.")
    sorun = input("Sorunun nedir kısaca? ")
    print(kedi_tavsiyesi(sorun))
    print("\nDanışmanlık ücreti: 1 mırıltı veya 3 balık.")
