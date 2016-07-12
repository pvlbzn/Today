'use strict';

const rq = require('request');


const url = "https://github.com";

function call(url, callback) {
  rq(url, (err, resp, data) => {
    if (err) throw err;
    let status = resp.statusCode;
    let body = data.toString();
    callback(body);
    return;
  });
}

call(url, (body) => {
  console.log(body);
});
