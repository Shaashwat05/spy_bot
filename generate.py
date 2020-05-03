from Crypto.PublicKey import RSA

def gen():

    new_key = RSA.generate(4096, e=65537)

    private_key = new_key.exportKey("PEM")

    public_key = new_key.publickey().exportKey("PEM")



    fd = open("private_key.pem", "wb")
    fd.write(private_key)
    fd.close()

    print(public_key)
    fd = open("public_key.pem", "wb")
    fd.write(public_key)
    fd.close()
