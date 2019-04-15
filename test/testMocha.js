var assert = require('assert');

var phantom = require('phantomjs');

//const phantom = require('phantom');

var content = '';

describe('Pagina Principal', function() {
    it('Deve retornar o texto caso ele esteja presente.', function() {
      assert.equal(true, false)
    });
});
    
(async function() {
    const instance = await phantom.create();
    const page = await instance.createPage();
    await page.on("onResourceRequested", function(requestData) {
        console.info('Requesting', requestData.url)
    });

    await page.open('http://206.81.8.182:8000');    
    content = await page.property('content');
    await instance.exit();

}());
// describe('Mocha and phantom', function () {

//     this.timeout(150);

//     it('Tweeking with phantomjs', function (done) {
//         phantom.create(function (ph) {
//             ph.createPage(function (page) {
//                 page.open('http://206.81.8.182:8000', function (status) {


//                     page.evaluate(function () {
//                        return document.all[0].outerHTML      //can check different elements
//                     }, function (result) {
//                         console.log('----------->>>>result',result);
//                         assert.equal(status,'success','Not appropriate status');
//                         //done();
//                     })
//                 })
//             })
//         })
//     })
// })