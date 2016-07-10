// Trying out promises

const promise = new Promise((res, rej) => {
    setTimeout(() => {
        console.log('promise');
        res('15');
    }); 
});


promise
    .then(
        res => {
            console.log('success: ' + res);
            return res;
        },
        err => {
            console.log('fail');
        }
    )
    .then(
        res => {
            console.log('Second then: ' + res);
        }
    );
