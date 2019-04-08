var assert = require('assert');
describe('Pagina Principal', function() {
    it('should return -1 when the value is not present', function() {
      assert.equal("42 é a resposta do universo!!!!!!", document.getElementById("resposta").innerHTML);
    });
});