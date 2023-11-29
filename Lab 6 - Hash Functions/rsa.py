import hashlib
from sympy import mod_inverse

def generate_keypair(p, q):
    n = p * q
    
    phi = (p - 1) * (q - 1)
    
    # choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537

    # compute d, the modular multiplicative inverse of e (mod phi)
    # d = e^-1 mod phi
    d = mod_inverse(e, phi)

    public_key = (e, n)    
    private_key = (d, n)   
    
    return public_key, private_key

def rsa_sign(h, private_key):
    d, n = private_key
    signature = pow(h, d, n)
    
    return signature

def rsa_verify(h, signature, public_key):
    e, n = public_key
    decrypted_signature = pow(signature, e, n) # signature ^ e mod n
    print(f"\nDecrypyed Signature: {hex(decrypted_signature)}\n")
    
    return h == decrypted_signature


p = 16315179614398580533624766726177540006576924199483510513561631756401428150940590287056704752120562777121686156279368804805949124204205870842371105143710779920000034464877715256952641199409814136301296562250302949099198438490303773428454472919384275490334954935351264568336896033129562916584432379808734519797081127865115974417511263352617129182541698911646475597152171461674668321922208842232187748232259475824071845215426911810481371467484594610249630560617809460909612508347159944730929501341567563694574712308333813785769643917707940978625444874330441839484189774145279098897557673725425741056189461
q = 102685921210957809071697882861691680650042071790443317026554940301679958224563904365315194873296311549746036194212409436929972028097586135988473434006402368001399215030848289794227688529790101868656676836255208394065883271672369078772910295901896868643812518709340611752499520318124380450322139494809113281359704227710797625278106161757605895125534358290944066110679834705596417370058078921259483152885478269020423443781714721658698094493178288848804134138557473563137771318075124198315868582984602556463198742670239260792990197926927149790510934519410140959541694820120750909771438331326059579573975987

public_key, private_key = generate_keypair(p, q)

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
hashed_message = hashlib.sha512() 
hashed_message.update(message.encode('utf-8'))
hashed_message = hashed_message.hexdigest()

# convert hex hash to int
hash_int = int(hashed_message, 16)

signature = rsa_sign(hash_int, private_key)
print(f"\nMessage: {message}")
print(f"\nHash of message: {hashed_message}")
print(f"\nSignature: {signature}")

verification_result = rsa_verify(hash_int, signature, public_key)
print(f"Verification Result: {verification_result}")

