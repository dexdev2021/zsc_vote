import reqwest from "reqwest";

export default {
    httpGet: function (url, data, succFn) {
        reqwest({
            url: url,
            method: "get",
            data: data,
            type: "json",
            success: (resp) => {
                succFn(resp);
            }
        });
    },

    httpPost: function (url, data, succFn) {
        reqwest({
            url: url,
            method: "post",
            data: data,
            type: "json",
            success: (resp) => {
                succFn(resp);
            }
        });
    },

    httpJson: function (url, data, succFn) {
        reqwest({
            url: url,
            method: "post",
            data: JSON.stringify(data),
            type: "json",
            contentType: "application/json",
            success: (resp) => {
                succFn(resp);
            }
        });
    }
}