from Crypto.Cipher import AES
import base64
import os
# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32
BLOCK_SZ = 14

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64
EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
secret = "332SECRETabc1234"
iv = "HELLOWORLD123456"
cipher=AES.new(key=secret,mode=AES.MODE_CBC,IV=iv)
my_text_to_encode = "password"
encoded = EncodeAES(cipher, my_text_to_encode)
print 'Encrypted string:', encoded

##
#####
#######
########
### PHP ###
#############

<?php
$enc = "x3OZjCAL944N/awRHSrmRBy9P4VLTptbkFdEl2Ao8gk=";
$secret = "332SECRETabc1234"; // same secret as python
$iv="HELLOWORLD123456";  // same iv as python
$padding = "{";  //same padding as python
function decrypt_data($data, $iv, $key) {
    $cypher = mcrypt_module_open(MCRYPT_RIJNDAEL_128, '', MCRYPT_MODE_CBC, '');

    if(is_null($iv)) {
        $ivlen = mcrypt_enc_get_iv_size($cypher);
        $iv = substr($data, 0, $ivlen);
        $data = substr($data, $ivlen);
    }

    // initialize encryption handle
    if (mcrypt_generic_init($cypher, $key, $iv) != -1) {
            // decrypt
            $decrypted = mdecrypt_generic($cypher, $data);

            // clean up
            mcrypt_generic_deinit($cypher);
            mcrypt_module_close($cypher);

            return $decrypted;
    }

    return false;
}



$res = decrypt_data(base64_decode($enc), $iv, $secret);
print rtrim($res,$padding);
?>
