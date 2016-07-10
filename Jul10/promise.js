// Trying out promises

const p = new Promise((res, rej) => {
    setTimeout(() => {
        console.log('promise');
        res('15');
    }); 
});


p.then(
    res => {
        console.log('success: ' + res);
    },
    err => {
        console.log('fail');
    }
);
