<?php
    // JSON
    $data = '{"str":"str","int":123,"obj":{"detail":"detail"},"arr":["a","b","c"]}';
    $json = json_decode($data);
    echo $json->{'str'};
    echo "\n".$json->{'int'};
    echo "\n".$json->{'obj'}->{'detail'};
    $arr = $json->{'arr'};
    foreach($arr as $value){
        echo "\nvalue=$value";
    }

    // Unixtimestamp
    $uts = strval((int)(microtime(true) * 1000));

    // Sort url GET parameters
    private function sortGETParameters($array){
        ksort($array);
        $rsp = '';
        foreach($array as $key => $value){
            if($rsp != ''){
                $rsp .= "&";
            }
            $rsp .= $key."=".$value;
        }
        return $rsp;
    }

    // RSA Sign & Verify
    private function getSignature($data){
        $signPriKey = openssl_get_privatekey(file_get_contents(SIGN_PRI_PATH));
        openssl_sign(base64_encode($data), $signature, $signPriKey, OPENSSL_ALGO_SHA256);
        $signature = base64_encode($signature);
        openssl_free_key($signPriKey);
        return $signature;
    }

    private function verify($data, $signature){
        $signPubKey = openssl_pkey_get_public(file_get_contents(SERVER_SIGN_PUB_PATH));
        $s1 = base64_decode($signature);
        $d1 = base64_encode($data);
        $isVerify = openssl_verify($d1, $s1, $signPubKey, OPENSSL_ALGO_SHA256);
        openssl_free_key($signPubKey);
        return $isVerify;
    }

    private function getHeaders($data){
        return array(
            'Content-Type:application/json',
            'X-XXX-TOKEN:'."XXX",
            'X-XXX-SIGNATURE:'."XXX"
        );
    }

    private function handleResponseHeaders($rspHeader){
        $rows = explode(PHP_EOL, $rspHeader);
        $map = [];
        foreach($rows as $row){
            list($key, $value) = explode(":", $row);
            $map[$key] = trim($value);
        }
        return $map;
    }

    // curl
    private function request($method, $path, $data){
        $url = HOST.$path;
        
        if($method == 'GET'){
            $url = $url."?".$data;
        }

        echo "\nmethod:$method";
        echo "\nurl:$url:";
        echo "\ndata:$data";

        // Header
        $headers = $this->getHeaders($data);

        $curl = curl_init();
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($curl, CURLOPT_URL, $url);
        
        if($method == 'POST'){
            curl_setopt($curl, CURLOPT_POST, true);
            curl_setopt($curl, CURLOPT_CUSTOMREQUEST, 'POST');
            curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
        }

        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($curl, CURLOPT_HEADER, 1);
        curl_setopt($curl, CURLOPT_TIMEOUT, 0);

        $rsp = curl_exec($curl);

        $statusCode = curl_getinfo($curl, CURLINFO_HTTP_CODE);
        $headerSize = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
        echo "\nstatusCode:".$statusCode;

        $rspHeader = $this->handleResponseHeaders(substr($rsp, 0, $headerSize));
        $rspBody = substr($rsp, $headerSize);
        echo "\nrspBody:".$rspBody;

        if(200 <= $statusCode && $statusCode <= 299){
            // verify signature
            $signature = $rspHeader['X-XXX-SIGNATURE'];
            if(!$this->verify($rspBody, $signature)){
                throw new Exception('Invalid signature.');
            }
        }

        return $rspBody;
    }

    // Split String
    explode(" ", "a b c"); // ["a", "b", "c"]
    $rows = explode(PHP_EOL, $rspHeader); // for http response headers
    list($key, $value) = explode(":", $row);

    // Array to json string
    $parameters = array(
        'a' => 'a',
        'b' => 'b',
        'c' => 'c'
    );
    json_encode($parameters);  // "{"a":"a","b":"b","c":"c"}"
?>