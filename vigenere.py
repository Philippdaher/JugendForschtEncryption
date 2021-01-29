def vig(txt='', key='', typ='enc'):
    if not txt:
        print ('Needs text')
        return
    if not key:
        print ('Needs key')
        return
    if typ not in ('dec', 'enc'):
        print ('Type must be "dec" or "enc"')
        return

    k_len = len(key)
    k_ints = [ord(i) for i in key]
    txt_ints = [ord(i) for i in txt]
    ret_txt = ''
    for i in range(len(txt_ints)):
        adder = k_ints[i % k_len]
        if typ == 'dec':
            adder *= -1

        v = (txt_ints[i] - 32 + adder) % 95

        ret_txt += chr(v + 32)

    print (ret_txt)
    return ret_txt
text="Die folgenden vier Texte werden jeweils mithilfe einer der vorherig erklärten Verschlüsselungsmethoden codiert, wobei dies der erste dieser Texte ist. Wir fügen unserer Arbeit diese Texte als Ergänzung hinzu, da wir der Ansicht waren, dass diese ein schönes Endprodukt dieses Projektes darstellen."
vig(text, "JugendForscht")
