const expect = require('chai').expect;

const x = 'hello';

describe('x test description', () => {
    it('expect to be a string type', () => {
        expect(x).to.be.a('string');
    });
    it('expect to have a length of 5', () => {
        expect(x).to.have.length(5);
    })
})
