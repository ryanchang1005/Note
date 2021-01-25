class HttpService {
    constructor(host) {
        this.host = host;
    }

    get(callback) {
        callback();
    }

    post(path, data, callback) {
        let fullUrl = this.host + path;
        let postData = JSON.stringify(data);
        $.ajax({
            type: "POST",
            url: fullUrl,
            data: postData,
            success: function (response, status, xhr) {
                console.log(response);
                console.log(status);
                console.log(xhr.status);
                console.log(xhr.getAllResponseHeaders());
                callback(response);
            },
            error: function (err) {
                console.log(err);
            }
        });
    }
}

class LifeMapService {
    constructor(mHttpService) {
        this.mHttpService = mHttpService;
    }

    login(username, password, callback) {
        let path = '/user/login/';
        let data = {
            username: username,
            password: password,
        };
        this.mHttpService.post(path, data, callback);
    }

    logout() {

    }

    getOrderList() {

    }

    updateOrder() {

    }
}

class HttpBinService {
    constructor(mHttpService) {
        this.mHttpService = mHttpService;
    }

    post(name, age, callback) {
        let path = '/post';
        let data = {
            name: name,
            age: age,
        };
        this.mHttpService.post(path, data, callback);
    }

}


