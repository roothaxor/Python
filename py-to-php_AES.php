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
