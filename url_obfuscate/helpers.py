from django.conf import settings
from Crypto.Cipher import AES
import binascii

def generate_url_pattern(url, params=[], leaf=True):
    url_array = url.split('/')
    url_array = [url for url in url_array if url != str()]
    response_array = list()
    for url_fragment in url_array:
        response_array.append(obfuscate(url_fragment))
    response = str()
    if len(response_array) > 0:
        response = '/'.join(str(el) for el in response_array)
    if params:
        for arg in params:

            response = '{0}/{1}'.format(response, arg)
    if len(response_array) > 0:
        if not response.endswith('/'):
            response = '{0}/'.format(response)
    if leaf:
        response = '{0}$'.format(response)
    return r'^' + response

def _padd(secret, blocksize=16, padding=' '):
    """Pads secret if not legal AES block size (16, 24, 32)"""
    if not len(secret) in (16, 24, 32):
        return secret + (blocksize - len(secret)) * padding
    return secret

def obfuscate(value):
    secret = _padd(settings.SECRET_KEY[0:16])
    encobj = AES.new(secret)

    value = unicode(value, 'utf-8')
    value = value.encode('utf-8') + (' ' * (16 - (len(value.encode('utf-8')) % 16)))
    encrypted = encobj.encrypt(value)
    hex_value = binascii.hexlify(encrypted)
    response = binascii.b2a_base64(hex_value)[:-1].replace('+', '-').replace('/', '_').replace('=', '')
    return response

def deobfuscate(value):
    secret = _padd(settings.SECRET_KEY[0:16])
    encobj = AES.new(secret)

    value = unicode(value, 'utf-8')
    value = value.replace('-', '+').replace('_', '/')
    value = value.encode('utf-8') + ('=' * (16 - (len(value.encode('utf-8')) % 16)))
    decoded = binascii.a2b_base64(value)
    unhex = binascii.unhexlify(decoded.encode('utf-8'))
    return encobj.decrypt(unhex).rstrip()
