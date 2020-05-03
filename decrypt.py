from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import zlib

def decrypt_blob(encrypted_blob, private_key):

    rsakey = RSA.importKey(private_key)
    rsakey = PKCS1_OAEP.new(rsakey)

    encrypted_blob = base64.b64decode(encrypted_blob)

    chunk_size = 512
    offset = 0
    decrypted = b""

    while(offset < len(encrypted_blob)):

        chunk = encrypted_blob[offset:offset +chunk_size]

        decrypted += rsakey.decrypt(chunk)

        offset  += chunk_size

    return zlib.decompress(decrypted)


