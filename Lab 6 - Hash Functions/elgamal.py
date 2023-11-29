import hashlib, math

def sha384_hash(message):
    hash_object = hashlib.sha384(message.encode('utf-8'))
    return int(hash_object.hexdigest(), 16)

def elgamal_sign(m, z):
    # step 1: select a secret random integer k such that GCD(k, p - 1) = 1
    k = 11
    # step 2: compute r ≡ g^k (mod p)
    r = pow(g, k, p)

    # step 3: compute s ≡ k^(-1)(h(m) - zr) (mod p-1)
    h_m = sha384_hash(m)
    s = (pow(k, -1, p-1) * (h_m - z * r)) % (p - 1)

    # Signed message is the triplet (m, r, s)
    return m, r, s

def elgamal_verify(signature, beta):
    m, r, s = signature

    # step 1: v1 = beta^(r)s (mod p)
    v1 = pow(beta, r, p) * pow(r, s, p) % p

    h_m = sha384_hash(m)
    print(h_m)
    v2 = pow(g, h_m, p)

    return v1 % p, v2 % p

message = '''
vigenere was born in the village of saint-pourcain, about half way between paris and marseilles, on april 5, 1523. at 
24, he entered the service of the duke of nevers, to whose house he remained attached the rest of his life, except for 
periods at court and as a diplomat. in 1549, at 26, he went to rome on a two-year diplomatic mission.it was here that 
he was first thrown into contact with cryptology, and he seems to have steeped himself in it. he read the books of 
trithemius,belaso, and other writers, and the unpublished manuscript of alberti. he evidently conversed with the experts 
of the papal curia, for he tells anecdotes that he could have heard only in the shoptalk of thesecryptologists. at 47, 
vigenere quit the court, turned over his annuity of 1,000 livres a year to the poor of paris, married the much younger 
marievare, and devoted himself to his writing. his traicte des chiffres, which was written in 1585 despite the distraction 
of a year-old baby daughter,appeared, elegantly rubricated, in 1586, and was reprinted the following year. his autokey 
system used the plaintext as the key. it provided apriming key. this consisted of a single letter, known to both 
enciphererand decipherer, with which the decipherer could decipher the first cryptogram letter and so get a start on 
his, work. with this, he would get the first plaintext letter, then use this as the key to decipher the second cryptogram 
letter, use that plaintext as the key to decipher the third cryptogram letter, and so on.the system works well and affords 
fair guarantees of security; it has been embodied in a number of modern cipher machines.in spite of vigenere's clear 
exposition of his technique, it was entirely forgotten and only entered the stream of cryptology late in the 19th century 
after it had been reinvented. writers on cryptology then added insult to injury by degrading vigenere's system into one 
much more elementary.the cipher now universally called the vigenere employs only standard alphabets and a short 
repeating keyword—a system far more susceptible to solution than vigenere's autokey. its tableauconsists of a modern 
tabula recta: 26 standard horizontal alphabets,each slid one space to the left of the one above. these are the cipher 
alphabets. a normal alphabet for the plaintext stands at the top. another normal alphabet, which merely repeats the 
initial letters of the horizontal ciphertext alphabets, runs down the left side. this is the key alphabet.both correspondents 
must know the keyword. the encipherer repeats this above the plaintext letters until each one has a keyletter. he seeks 
the plaintext letter in the top alphabet and the key letter in the side. then he traces down from the top and in from the 
side. the ciphertext letter stands at the intersection of the column and the row. the encipherer repeats this process with 
all the letters of the plaintext. to decipher, the clerk begins with the key letter, runs in along the ciphertext alphabet 
until he strikes the cipher letter, then follows the column of letters upward until he emerges at the plaintext letter at 
the top.polyalphabetic ciphers were, when used with mixed alphabets and without word divisions, unbreakable to the 
cryptanalysts of the renaissance. why, then, did the nomenclator reign supreme for 300 years? why did cryptographers 
not use the polyalphabetic system instead?
'''

g = 2
p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
z = math.floor(sha384_hash(message)/2)

beta = pow(g, z, p)

signature = elgamal_sign(message, z)
v1, v2 = elgamal_verify(signature, beta)

print("Message:", message)
print("Signature: \n r = ", signature[1], "\n s = ", signature[2])
print("\nValidation: \n v1 = ", v1, "\n v2 = ", v2)

if (v1 == v2):
    print("\nSignature is valid")