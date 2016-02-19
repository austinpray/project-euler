var assert = require('assert');

var sumMultiples = require('./multiples');

assert.equal(sumMultiples([3, 5], 10), 23);

console.log(sumMultiples([3, 5], 1000));
