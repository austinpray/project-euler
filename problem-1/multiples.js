function isMultipleOfAny(multiples, num) {
  return multiples.some(function (multiple) {
    return num % multiple === 0;
  });
}

var sumMultiples = function (multiples, upper) {
  var sum = 0;
  for(var i = 1; i < upper; i++) {
    if (isMultipleOfAny(multiples, i)) {
      sum += i;
    }
  }
  return sum;

};

module.exports = sumMultiples;
