const express = require('express');
const bp = require('body-parser');

const app = express();

const jsonParser = bp.json();
const urlEncParser = bp.urlencoded({extended: true});


// Set up middleware.
app.use(urlEncParser);
app.use(jsonParser);

/**
 * Middleware which displays information for each request.
 */
app.use((req, res, next) => {
    console.log(`\nurl: ${req.url}`);
    console.log(`params: ${JSON.stringify(req.params)}`);
    console.log(`query: ${JSON.stringify(req.query)}`);
    next();
});

/**
 * App root with a baked frontend code into a response.
 */
app.get('/', (req, res) => {
    res.send(`
        <html>
            <head>
                <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
            </head>
            <body>
                <a href="#" id="link1">link 1</a>
                <a href="#" id="link2">link 2</a>
                <a href="#" id="link3">link 3</a>
                <a href="#" id="link4">link 4</a>
                <script>
                    
                    /**
                     * Link 1 ajax call event
                     */
                    const l1 = $('#link1');
                    l1.click(event => {
                        event.preventDefault();
                        console.log('link 1 clicked');

                        $.ajax({                        
                            type: 'POST',
                            data: JSON.stringify({
                                'foo-key': 'foo-val'
                            }),
                            url: '/api/endpoint',
                            contentType: 'application/json',
                        })
                        .done(msg => {
                            console.log('succes');
                        })
                        .fail((xhr, status, err) => {
                            console.log('err ' + err);
                            console.log(status);
                        })
                        .always((xhr, status) => {
                            console.log('link processed. status: ' + status);
                        });
                    });

                    /**
                     * Link 2 ajax call event
                     */
                    const l2 = $('#link2');
                    l2.click(event => {
                        event.preventDefault();
                        console.log('link 2 clicked');
                        
                        $.ajax({
                            type: 'GET',
                            url: '/ajax',
                        })
                        .done(data => {
                            console.log(data);
                        });
                    });

                    /**
                     * Link 3 ajax call event
                     */
                    const l3 = $('#link3');
                    l3.click(event => {
                        event.preventDefault();
                        console.log('link 3 clicked');

                        $.get('/ajax', res => {
                            console.log(res);
                        });
                    });

                    /**
                     * Link 4 ajax call event
                     */
                    const l4 = $('#link4');
                    l4.click(event => {
                        event.preventDefault();
                        console.log('link 4 clicked');

                        $.get('/ajax', res => {
                            console.log(res);
                        })
                        .then(success => {
                            console.log('success: ' + success);
                        },
                        fail => {
                            console.log('fail: ' + fail);
                        });
                    });
                </script>
            </body>
            `);
});

/**
 * Post API endpoint.
 */
app.post('/api/endpoint', (req, res) => {
    console.log(`body: ${JSON.stringify(req.body)}`);
    if (req.body) {
        res.send('success');
    } else {
        res.send('failed');
    }
});

/**
 * Get for AJAX
 */
app.get('/ajax', (req, res) => {
    if (req.xhr) {
        res.json({
            id: '15'
        });
    } else {
        res.json({
            error: 'ajax calls only'
        });
    }
});


app.listen(25000, 'localhost');
