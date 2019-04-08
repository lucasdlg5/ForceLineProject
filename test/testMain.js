describe('Pagina Principal', function() {
    it('Deve retornar o texto caso ele esteja presente.', function() {
      assert.equal("42 é a resposta do universo!!!!!!", document.getElementById("resposta").innerHTML);
    });
});